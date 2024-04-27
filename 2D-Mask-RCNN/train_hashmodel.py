import os
import mrcnn.model
import mrcnn.config

from prepare_hashes import HashTrainDataset, HashTestDataset

class HashConfig(mrcnn.config.Config):
    NAME = "hash_cfg"

    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

    NUM_CLASSES = 1 + len([file[:-4] for file in os.listdir(f'hash_dataset{os.sep}identicons{os.sep}') if file.endswith('.png')])

    STEPS_PER_EPOCH = 25

# Train
hash_train_dataset = HashTrainDataset()
hash_train_dataset.load_dataset()
hash_train_dataset.prepare()

# Test
hash_test_dataset = HashTestDataset()
hash_test_dataset.load_dataset()
hash_test_dataset.prepare()

# Model Configuration
hash_config = HashConfig()

model = mrcnn.model.MaskRCNN(mode='training',
                             model_dir='./',
                             config=hash_config)

model.load_weights(filepath='mask_rcnn_coco.h5',
                   by_name=True,
                   exclude=["mrcnn_class_logits", "mrcnn_bbox_fc", "mrcnn_bbox", "mrcnn_mask"])

model.train(
    train_dataset=hash_train_dataset,
    val_dataset=hash_test_dataset,
    learning_rate=hash_config.LEARNING_RATE,
    epochs=4,
    layers='heads')

model_path = 'hash_mask_rcnn_trained.h5'
model.keras_model.save_weights(model_path)