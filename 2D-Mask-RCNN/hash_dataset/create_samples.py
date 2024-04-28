import cv2
import random
import numpy as np
import os
import json

def conf(region_id, region_shape_attributes, region_attributes):

    return {
        'region_id': region_id,
        'region_shape_attributes': json.dumps({
            'name': 'polygon',
            'all_points_x': region_shape_attributes['x'],
            'all_points_y': region_shape_attributes['y'] 
        }),
        'region_attributes': region_attributes
    }

class Template:

    def __init__(self, x:int=4096, y:int=2160, folder={'jpg': 'samples', 'csv': 'annos'}) -> None:
        
        self.__blank = np.zeros((y, x, 3), dtype=np.uint8)
        self.__reserved = []
        self.__margin = 30
        self.__annos = []
        self._region_id = 0
        self.select_mode = 'DEV'
        self.folder = folder
        os.makedirs(name=f'{self.folder["jpg"]}', exist_ok=True)
        os.makedirs(name=f'{self.folder["csv"]}', exist_ok=True)

    def affix(self, img_no):

        img = cv2.imread(f'identicons{os.sep}hash_{img_no}.png')
        self._rad_y, self._rad_x = int((img.shape[0])/2), int((img.shape[1])/2)
        ran_y, ran_x = random.randint(0+self._rad_y, self.__blank.shape[0]-self._rad_y), random.randint(0+self._rad_x, self.__blank.shape[1]-self._rad_x)
        return self.validate_and_affix(img, inp_y=ran_y, inp_x=ran_x, hash=img_no)
    
    def validate_and_affix(self, img, inp_x, inp_y, hash):

        result = True
        for space in self.__reserved:
            comparison = ((space[1]-(self._rad_x+self.__margin)) < inp_x < (space[1]+(self._rad_x+self.__margin))) and ((space[0]-(self._rad_y+self.__margin)) < inp_y < (space[0]+(self._rad_y+self.__margin)))
            if comparison:
                result = False
                break

        if result == True:
            self.__blank[(inp_y-self._rad_y):(inp_y+self._rad_y), (inp_x-self._rad_x):(inp_x+self._rad_x)] = img
            self.__reserved.append((inp_y, inp_x))
            all_points = {
                'x': [inp_x-self._rad_x, inp_x+self._rad_x, inp_x+self._rad_x, inp_x-self._rad_x],
                'y': [inp_y-self._rad_y, inp_y-self._rad_y, inp_y+self._rad_y, inp_y+self._rad_y]
            }
            self.__annos.append(conf(region_id=self._region_id, region_shape_attributes=all_points, region_attributes=json.dumps({'name': f'hash_{hash}'})))
            self._region_id += 1

        return result
    
    def close(self, fname:str='blank'):

        if self.select_mode == 'REL':
            cv2.imwrite(f'{self.folder["jpg"]}{os.sep}{fname}.jpg', self.__blank)
        else:
            cv2.imwrite(f'{fname}.jpg', self.__blank)
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
                        'filename': f'{fname}.jpg', 
                        'file_size': os.path.getsize(f'{self.folder["jpg"]}{os.sep}{fname}.jpg'), 
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
                        'filename': f'{fname}.jpg', 
                        'file_size': os.path.getsize(f'{fname}.jpg'), 
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
    for sample in range(0, 10):
        print(f'Creating Sample_{sample}...')
        template = Template(x=256, y=256, folder={'jpg': 'samples', 'csv': 'annos'})
        template.select_mode = 'REL'
        for identicon in range(0, 10):
            template.affix(identicon)
        for identicon in range(0, 10):
            template.affix(identicon)
        for identicon in range(0, 10):
            template.affix(identicon)
        template.close(f'sample_{sample}')
        print('Done')

    # Training Set
    for sample in range(0, 10):
        print(f'Creating Sample_{sample}...')
        template = Template(x=256, y=256, folder={'jpg': 'train_samples', 'csv': 'train_annos'})
        template.select_mode = 'REL'
        for identicon in range(0, 10):
            template.affix(identicon)
        for identicon in range(0, 10):
            template.affix(identicon)
        for identicon in range(0, 10):
            template.affix(identicon)
        template.close(f'sample_{sample}')
        print('Done')

    # Test Set
    for sample in range(0, 10):
        print(f'Creating Sample_{sample}...')
        template = Template(x=256, y=256, folder={'jpg': 'test_samples', 'csv': 'test_annos'})
        template.select_mode = 'REL'
        for identicon in range(0, 10):
            template.affix(identicon)
        for identicon in range(0, 10):
            template.affix(identicon)
        for identicon in range(0, 10):
            template.affix(identicon)
        template.close(f'sample_{sample}')
        print('Done')

    consolidate_csv(['train_annos/', 'test_annos/', 'annos/'])