# TF-NMT
- Training/testing codes for using tf-nmt, based on https://github.com/tensorflow/nmt
- Detailed information can also be found inside the original repo.

# Tool and package used:
- Python 3.6
- tensorflow

# Pre-training setup & config file:
- Training and testing dataset need to be prepared and put into the path: datasets/L1-L2/
- L1, L2 stands for language type. Dataset requires vocab files, sentence pairs for both language as well 2 sets for testing data.
- Some sample data can be download from: https://nlp.stanford.edu/projects/nmt/
- Make a file named <config.txt> in the dataset dir, and adjust the training configuration based on the following sample:

## Dataset path:
 - VOCAB_PREFIX datasets/vi-en/vocab
 - TRAIN_PREFIX datasets/vi-en/train
 - DEV_PREFIX datasets/vi-en/tst2012
 - TEST_PREFIX datasets/vi-en/tst2013

## Training parameters:
- NUM_TRAIN_STEPS 12000
- STEPS_PER_STATS 100
- NUM_LYRS 2
- NUM_UNITS 128
- DROPOUT 0.2
- USE_ATTENTION Yes
- ATTENTION_FLAG scaled_luong

#### A sample config file is also provided as sample_config.txt in the root.

# Run the training script:

- python train_script.py <SRC_LANG> <TRT_LANG>

# Run the testing script:

- python test_script.py <MODEL_DIR_PATH> <SRC_TEST_FILE_PATH> <TGT_TEST_FILE_PATH>

# Addtional information:
- To be updated.
