import mrcnn
import mrcnn.config
import mrcnn.model
import mrcnn.visualize
import cv2
import os
import random

# load the class label names from disk
CLASS_NAMES = ['BG'] + sorted([file[:-4] for file in os.listdir(f'hash_dataset{os.sep}identicons{os.sep}') if file.endswith('.png')])

class HashConfig(mrcnn.config.Config):

    NAME = "hash_cfg"

    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

    NUM_CLASSES = len(CLASS_NAMES)

# Initialize the Mask R-CNN model for inference and then load the weights.
# This step builds the keras model architecture
model = mrcnn.model.MaskRCNN(mode="inference",
                             config=HashConfig(),
                             model_dir='./')

# Load the weights into the model
model.load_weights(filepath="hash_mask_rcnn_trained.h5", by_name=True)

# load the input image, convert it from BGR to RGB channel
Test_Dir = os.listdir(f"hash_dataset{os.sep}samples") # lists images from a directory
image = cv2.imread(f"hash_dataset{os.sep}samples{os.sep}"+Test_Dir[random.randint(0, len(Test_Dir))]) # picks a random image from the directory
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Perform a forward pass of the network to obtain the results
r = model.detect([image], verbose=0)

# Get the results for the first image
r = r[0]

# Visualize the detected objects.
mrcnn.visualize.display_instances(image=image,
                                  boxes=r['rois'],
                                  masks=r['masks'],
                                  class_ids=r['class_ids'],
                                  class_names=CLASS_NAMES,
                                  scores=r['scores'])