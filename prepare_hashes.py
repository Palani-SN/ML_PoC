import os
import cv2
import json
import pandas as pd
import numpy as np
from mrcnn import utils
import mrcnn
import mrcnn.visualize

class HashTrainDataset(utils.Dataset):

    def load_dataset(self):

        # class definitions
        hashes = sorted([file for file in os.listdir(f'hash_dataset{os.sep}identicons{os.sep}') if file.endswith('.png')])
        for hash in hashes:
            self.add_class(source='dataset', class_id=int(hash[:-4].replace('hash_', '')), class_name=hash[:-4])

        # dataset definitions
        samples = [file for file in os.listdir(f'hash_dataset{os.sep}train_samples{os.sep}') if file.endswith('.jpg')]
        for i, fname in enumerate(samples):
            self.add_image(source='dataset',
                           image_id=i,
                           path=os.path.join(f'hash_dataset{os.sep}train_samples', fname),
                           annotation=os.path.join(f'hash_dataset{os.sep}train_annos', fname.replace('.jpg', '.csv')))
            
    def extract_masks(self, fname):

        DF = pd.read_csv(fname)
        masks = np.zeros([512, 512, len(DF.index)], dtype='uint8')
        classes = []
        for idx, row in DF.iterrows():
            mask = np.zeros([512, 512], dtype=np.uint8)
            # region shape attributes
            region_shape_attributes = json.loads(row['region_shape_attributes'])
            all_points_x = region_shape_attributes['all_points_x']
            all_points_y = region_shape_attributes['all_points_y']
            all_points_x_y = [list(x) for x in zip(all_points_x, all_points_y)]
            cv2.fillPoly(mask, np.array([all_points_x_y], dtype=np.int32), 1)
            masks[:, :, idx] = mask
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
    
class HashTestDataset(utils.Dataset):

    def load_dataset(self):

        # class definitions
        hashes = sorted([file for file in os.listdir(f'hash_dataset{os.sep}identicons{os.sep}') if file.endswith('.png')])
        for hash in hashes:
            self.add_class(source='dataset', class_id=int(hash[:-4].replace('hash_', '')), class_name=hash[:-4])

        # dataset definitions
        samples = [file for file in os.listdir(f'hash_dataset{os.sep}test_samples{os.sep}') if file.endswith('.jpg')]
        for i, fname in enumerate(samples):
            self.add_image(source='dataset',
                           image_id=i,
                           path=os.path.join(f'hash_dataset{os.sep}test_samples', fname),
                           annotation=os.path.join(f'hash_dataset{os.sep}test_annos', fname.replace('.jpg', '.csv')))
            
    def extract_masks(self, fname):

        DF = pd.read_csv(fname)
        masks = np.zeros([512, 512, len(DF.index)], dtype='uint8')
        classes = []
        for idx, row in DF.iterrows():
            mask = np.zeros([512, 512], dtype=np.uint8)
            # region shape attributes
            region_shape_attributes = json.loads(row['region_shape_attributes'])
            all_points_x = region_shape_attributes['all_points_x']
            all_points_y = region_shape_attributes['all_points_y']
            all_points_x_y = [list(x) for x in zip(all_points_x, all_points_y)]
            cv2.fillPoly(mask, np.array([all_points_x_y], dtype=np.int32), 1)
            masks[:, :, idx] = mask
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
    hash_traindataset = HashTrainDataset()
    hash_traindataset.load_dataset()
    hash_traindataset.prepare()

    # load and display random samples
    image_ids = np.random.choice(hash_traindataset.image_ids, 4)
    for image_id in image_ids:
        image = hash_traindataset.load_image(image_id)
        mask, class_ids = hash_traindataset.load_mask(image_id)
        mrcnn.visualize.display_top_masks(image, mask, class_ids, hash_traindataset.class_names)

    # test
    hash_testdataset = HashTestDataset()
    hash_testdataset.load_dataset()
    hash_testdataset.prepare()

    # load and display random samples
    image_ids = np.random.choice(hash_testdataset.image_ids, 4)
    for image_id in image_ids:
        image = hash_testdataset.load_image(image_id)
        mask, class_ids = hash_testdataset.load_mask(image_id)
        mrcnn.visualize.display_top_masks(image, mask, class_ids, hash_testdataset.class_names)