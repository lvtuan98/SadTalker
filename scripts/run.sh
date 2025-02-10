audio_path=/localhome/local-tvle/workspace/SadTalker/examples/driven_audio/bus_chinese.wav
img_path=/localhome/local-tvle/workspace/SadTalker/examples/source_image/full3.png

python inference.py --driven_audio ${audio_path} \
           --source_image ${img_path} \
           --result_dir ./results --still --preprocess full --enhancer gfpgan