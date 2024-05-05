import os
import mrcnn.model
import mrcnn.config

from prepare_dots import DotTrainDataset, DotTestDataset

class DotConfig(mrcnn.config.Config):
    NAME = "dot_cfg"

    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

    NUM_CLASSES = 1 + len(sorted([file[:-8] for file in os.listdir(f'dot_dataset{os.sep}identicons{os.sep}') if file.endswith('.ome.tif')]))

    STEPS_PER_EPOCH = 10

# Train
hash_train_dataset = DotTrainDataset()
hash_train_dataset.load_dataset()
hash_train_dataset.prepare()

# Test
hash_test_dataset = DotTestDataset()
hash_test_dataset.load_dataset()
hash_test_dataset.prepare()

# Model Configuration
hash_config = DotConfig()

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
    epochs=2,
    layers='heads')

model_path = 'hash_mask_rcnn_trained.h5'
model.keras_model.save_weights(model_path)