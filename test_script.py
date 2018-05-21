import os
import sys

test_cmd = "python -m nmt.nmt \
    --out_dir=" + sys.argv[1] + " \
    --inference_input_file=" + sys.argv[2] + " \
    --inference_output_file=" + sys.argv[3]

os.system(test_cmd)