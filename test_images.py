import os
import glob
import subprocess
from tqdm import tqdm


if __name__ == "__main__":
    image_dir = "/localhome/local-tvle/workspace/SadTalker/examples/source_image"
    audio_path = "/localhome/local-tvle/workspace/SadTalker/examples/driven_audio/bus_chinese.wav"
    list_images = glob.glob(os.path.join(image_dir, "*.png"))
    error_list = []
    for img_path in list_images:
        print("="*20, img_path)
        try:
            subprocess.run(["python", 
                            "inference.py", 
                            "--driven_audio", 
                            audio_path,
                            "--source_image",
                            img_path,
                            "--result_dir",
                            "./results",
                            "--still",
                            "--preprocess",
                            "full",
                            "--enhancer",
                            "gfpgan"])
        except Exception as e:
            print(e)
            error_list.append(img_path)
    print("No. error list:", len(error_list))
    with open("error_list.txt", "w") as f:
        [f.write(line+'\r\n') for line in error_list]