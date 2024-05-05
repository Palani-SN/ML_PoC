import os
import cv2
import json
import pandas as pd
import numpy as np
from mrcnn import utils
import mrcnn
import mrcnn.visualize

class DotTrainDataset(utils.Dataset):

    def load_dataset(self):

        # class definitions
        dots = sorted([file[:-8] for file in os.listdir(f'dot_dataset{os.sep}identicons{os.sep}') if file.endswith('.ome.tif')])
        for dot in dots:
            self.add_class(source='dataset', class_id=int(dot.replace('dot_', '')), class_name=dot)

        # dataset definitions
        samples = [file for file in os.listdir(f'dot_dataset{os.sep}train_samples{os.sep}') if file.endswith('.ome.tif')]
        for i, fname in enumerate(samples):
            self.add_image(source='dataset',
                           image_id=i,
                           path=os.path.join(f'dot_dataset{os.sep}train_samples', fname),
                           annotation=os.path.join(f'dot_dataset{os.sep}train_annos', fname.replace('.ome.tif', '.csv')))
            
    def extract_masks(self, fname):

        DF = pd.read_csv(fname)
        masks = np.zeros([64, 64, 64, len(DF.index)], dtype='uint8')
        classes = []
        for idx, row in DF.iterrows():
            mask = np.zeros([64, 64], dtype=np.uint8)
            # region shape attributes
            region_shape_attributes = json.loads(row['region_shape_attributes'])
            all_points_x = region_shape_attributes['all_points_x']
            all_points_y = region_shape_attributes['all_points_y']
            z_min, z_max = region_shape_attributes['all_points_z']
            all_points_x_y = [list(x) for x in zip(all_points_x, all_points_y)]
            cv2.fillPoly(mask, np.array([all_points_x_y], dtype=np.int32), 1)
            masks[z_min:z_max, :, :, idx] = [mask]*(z_max-z_min)
            # region attributes
            region_attributes = json.loads(row['region_attributes'])
            class_name = region_attributes['name']
            classes.append(self.class_names.index(class_name))
        return masks, classes
    
    # load the masks for an image
    def load_mask(self, image_id):
        # get details of image
        info = self.image_info[image_id]
        # define box file location
        path = info['annotation']
        # load XML
        masks, classes = self.extract_masks(path)
        return masks, np.asarray(classes, dtype='int32')
    
    def image_reference(self, image_id):
        info = self.image_info[image_id]
        return info['path']
    
class DotTestDataset(utils.Dataset):

    def load_dataset(self):

        # class definitions
        dots = sorted([file[:-8] for file in os.listdir(f'dot_dataset{os.sep}identicons{os.sep}') if file.endswith('.ome.tif')])
        for dot in dots:
            self.add_class(source='dataset', class_id=int(dot.replace('dot_', '')), class_name=dot)

        # dataset definitions
        samples = [file for file in os.listdir(f'dot_dataset{os.sep}test_samples{os.sep}') if file.endswith('.ome.tif')]
        for i, fname in enumerate(samples):
            self.add_image(source='dataset',
                           image_id=i,
                           path=os.path.join(f'dot_dataset{os.sep}test_samples', fname),
                           annotation=os.path.join(f'dot_dataset{os.sep}test_annos', fname.replace('.ome.tif', '.csv')))
            
    def extract_masks(self, fname):

        DF = pd.read_csv(fname)
        masks = np.zeros([64, 64, 64, len(DF.index)], dtype='uint8')
        classes = []
        for idx, row in DF.iterrows():
            mask = np.zeros([64, 64], dtype=np.uint8)
            # region shape attributes
            region_shape_attributes = json.loads(row['region_shape_attributes'])
            all_points_x = region_shape_attributes['all_points_x']
            all_points_y = region_shape_attributes['all_points_y']
            z_min, z_max = region_shape_attributes['all_points_z']
            all_points_x_y = [list(x) for x in zip(all_points_x, all_points_y)]
            cv2.fillPoly(mask, np.array([all_points_x_y], dtype=np.int32), 1)
            masks[z_min:z_max, :, :, idx] = [mask]*(z_max-z_min)
            # region attributes
            region_attributes = json.loads(row['region_attributes'])
            class_name = region_attributes['name']
            classes.append(self.class_names.index(class_name))
        return masks, classes
    
    # load the masks for an image
    def load_mask(self, image_id):
        # get details of image
        info = self.image_info[image_id]
        # define box file location
        path = info['annotation']
        # load XML
        masks, classes = self.extract_masks(path)
        return masks, np.asarray(classes, dtype='int32')
    
    def image_reference(self, image_id):
        info = self.image_info[image_id]
        return info['path']
    
if __name__ == '__main__':

    # train
    hash_traindataset = DotTrainDataset()
    hash_traindataset.load_dataset()
    hash_traindataset.prepare()

    # load and display random samples
    image_ids = np.random.choice(hash_traindataset.image_ids, 4)
    for image_id in image_ids:
        images = hash_traindataset.load_image(image_id)
        mask, class_ids = hash_traindataset.load_mask(image_id)
        # print(image.shape)
        mrcnn.visualize.display_top_masks(images, mask, class_ids, hash_traindataset.class_names)

    # test
    hash_testdataset = DotTestDataset()
    hash_testdataset.load_dataset()
    hash_testdataset.prepare()

    # load and display random samples
    image_ids = np.random.choice(hash_testdataset.image_ids, 4)
    for image_id in image_ids:
        images = hash_testdataset.load_image(image_id)
        mask, class_ids = hash_testdataset.load_mask(image_id)
        mrcnn.visualize.display_top_masks(images, mask, class_ids, hash_testdataset.class_names)