import os
import sys

def read_config_file(config_file_path):
    fin = open(config_file_path, 'r')
    config = dict()
    for line in fin:
        if line[0] == '#':
            continue
        line = line.strip().split(' ')
        config[line[0]] = line[1]
    
    fin.close()
    return config

def get_path_config(src, tgt):
    config = None
    
    if os.path.exists("datasets/" + src + '-' + tgt + '/config.txt'):
        config = read_config_file("datasets/" + src + '-' + tgt + '/config.txt')
        
    elif os.path.exists("datasets/" + tgt + '-' + src + '/config.txt'):
        config = read_config_file("datasets/" + tgt + '-' + src + '/config.txt')
        
    else:
        print ("Specified lang pair's dataset config file not exist, exiting...")
        sys.exit(0)
    
    return config
    

src = sys.argv[1]
tgt = sys.argv[2]

config = get_path_config(src, tgt)

train_cmd = "python -m nmt.nmt \
    --src=vi --tgt=en \
    --vocab_prefix=" + config['VOCAB_PREFIX'] + " \
    --train_prefix=" + config['TRAIN_PREFIX'] + " \
    --dev_prefix=" + config['DEV_PREFIX'] + " \
    --test_prefix=" + config['TEST_PREFIX'] + " \
    --out_dir=model/res \
    --num_train_steps=" + config['NUM_TRAIN_STEPS'] + " \
    --steps_per_stats=" + config['STEPS_PER_STATS'] + " \
    --num_layers=" + config['NUM_LYRS'] + " \
    --num_units=" + config['NUM_UNITS'] + " \
    --dropout=" + config['DROPOUT'] + " \
    --metrics=bleu"

if config['USE_ATTENTION'] == 'Yes':
    train_cmd += ' --attention=' + config['ATTENTION_FLAG']

os.system(train_cmd)

