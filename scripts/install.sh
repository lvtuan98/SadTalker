cd SadTalker 
conda create -n sadtalker python=3.8
conda activate sadtalker
# pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113
pip install torch==2.0.0 torchvision==0.15.1 torchaudio==2.0.1 --index-url https://download.pytorch.org/whl/cu118
conda install ffmpeg
pip install -r requirements.txt
# pip install gTTS
pip install tts