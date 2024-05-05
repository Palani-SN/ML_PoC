import cv2

import tifffile as tif
import numpy as np

import numpy as np
import os
import json
from random import randrange

def conf(region_id, region_shape_attributes, region_attributes):

    return {
        'region_id': region_id,
        'region_shape_attributes': json.dumps({
            'name': 'polygon',
            'all_points_x': region_shape_attributes['x'],
            'all_points_y': region_shape_attributes['y'],
            'all_points_z':region_shape_attributes['z']
        }),
        'region_attributes': region_attributes
    }

class Template:

    def __init__(self, x:int=4096, y:int=2160, z:int=256, folder={'jpg': 'samples', 'csv': 'annos'}) -> None:
        
        self.__blank = np.zeros((z, y, x, 3), dtype=np.uint8)
        self.__shape = (z, y, x)
        self.__reserved = []
        self.__annos = []
        self._region_id = -1
        self.select_mode = 'DEV'
        self.folder = folder
        os.makedirs(name=f'{self.folder["jpg"]}', exist_ok=True)
        os.makedirs(name=f'{self.folder["csv"]}', exist_ok=True)

    def affix(self, img_no):

        z, y, x = self.__shape
        random_z_y_x = (randrange(z), randrange(y), randrange(x))
        return self.validate_and_affix(random_z_y_x, img_no)
    
    def validate_and_affix(self, random_z_y_x, img_no):

        result = False
        z, y, x = random_z_y_x
        img_dict = {}
        dots = tif.imread(f'identicons{os.sep}dot_{img_no}.ome.tif')
        for stack in [-4, -3, -2, -1, 0, 1, 2, 3, 4]:
            img_dict[z+stack] = dots[stack+4]
        _rad_y, _rad_x = int((img_dict[z].shape[0])/2), int((img_dict[z].shape[1])/2)
        filtered = list(filter(lambda point: (z-(4*3) < point[0] < z+(4*3)) and (y-(_rad_y+30) < point[1] < y+(_rad_y+30)) and (x-(_rad_x+30) < point[2] < x+(_rad_x+30)), self.__reserved))
        # print(filtered)
        if filtered == [] and (0 < z-4 < z+4 < self.__shape[0]) and (0 < y-_rad_y < y+_rad_y < self.__shape[1]) and (0 < x-_rad_x < x+_rad_x < self.__shape[2]):
            self.__reserved.append((z, y, x))
            # print(z, y, x)
            for layer in range(z-4, z+4):
                _rad_y, _rad_x = int((img_dict[layer].shape[0])/2), int((img_dict[layer].shape[1])/2)
                self.__blank[layer, (y-_rad_y):(y+_rad_y), (x-_rad_x):(x+_rad_x)] = img_dict[layer]
                result = True
            all_points = {
                'x': [x-_rad_x, x+_rad_x, x+_rad_x, x-_rad_x],
                'y': [y-_rad_y, y-_rad_y, y+_rad_y, y+_rad_y],
                'z': [z-4, z+4]
            }
            self._region_id += 1
            self.__annos.append(conf(region_id=self._region_id, region_shape_attributes=all_points, region_attributes=json.dumps({'name': f'dot_{img_no}'})))

        return result
    
    def close(self, fname:str='blank'):

        print(self.__reserved)
        if self.select_mode == 'REL':
            tif.imwrite(f'{self.folder["jpg"]}{os.sep}{fname}.ome.tif', self.__blank, photometric='rgb')
        else:
            tif.imwrite(f'{fname}.ome.tif', self.__blank, photometric='rgb')

        self.create_csv(fname=fname, datum=self.__annos)

    def create_csv(self, fname, datum):

        import csv
        datum_schema = ['filename', 'file_size', 'file_attributes', 'region_count'] + list(datum[0].keys())
        if self.select_mode == 'REL':
            with open(f'{self.folder["csv"]}{os.sep}{fname}.csv', 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=datum_schema)
                writer.writeheader()
                for data in datum:
                    data.update({
                        'filename': f'{fname}.ome.tif', 
                        'file_size': os.path.getsize(f'{self.folder["jpg"]}{os.sep}{fname}.ome.tif'), 
                        'file_attributes': {}, 
                        'region_count': (self._region_id+1)
                    })
                    writer.writerow(data)
        else:
            with open(f'{fname}.csv', 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=datum_schema)
                writer.writeheader()
                for data in datum:
                    data.update({
                        'filename': f'{fname}.ome.tif', 
                        'file_size': os.path.getsize(f'{fname}.ome.tif'), 
                        'file_attributes': {}, 
                        'region_count': (self._region_id+1)
                    })
                    writer.writerow(data)

def consolidate_csv(folders: list):

    import pandas as pd
    import glob

    files = []
    for folder in folders:
        files += glob.glob(folder + "*.csv") # get names of all CSV files under path

    consolidated_df = pd.concat([pd.read_csv(file) for file in files])
    # df_wo_index = consolidated_df.reset_index(drop=True)
    #save the DataFrame to a file
    consolidated_df.to_csv("consolidated.csv", index=False)


if __name__ == '__main__':

    # Validation Set
    for sample in range(0, 3):
        print(f'Creating Sample_{sample}...')
        template = Template(x=64, y=64, z=64, folder={'jpg': 'samples', 'csv': 'annos'})
        template.select_mode = 'REL'
        for iter in range(0, 100):
            for identicon in range(0, 5):
                template.affix(identicon)
        template.close(f'sample_{sample}')
        print('Done')

    # Training Set
    for sample in range(0, 3):
        print(f'Creating Sample_{sample}...')
        template = Template(x=64, y=64, z=64, folder={'jpg': 'train_samples', 'csv': 'train_annos'})
        template.select_mode = 'REL'
        for iter in range(0, 100):
            for identicon in range(0, 5):
                template.affix(identicon)
        template.close(f'sample_{sample}')
        print('Done')

    # Test Set
    for sample in range(0, 3):
        print(f'Creating Sample_{sample}...')
        template = Template(x=64, y=64, z=64, folder={'jpg': 'test_samples', 'csv': 'test_annos'})
        template.select_mode = 'REL'
        for iter in range(0, 100):
            for identicon in range(0, 5):
                template.affix(identicon)
        template.close(f'sample_{sample}')
        print('Done')

    consolidate_csv(['train_annos/', 'test_annos/', 'annos/'])