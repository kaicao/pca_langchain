
## Requirements
- Windows WSL installed.
- Python 3 installed.
- Pip 3 installed.
- Download [all-mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2) into model/all-mpnet-base-v2 folder.
- Download Llama2 model and update llama2_loader.py LLAMA2_MODEL_PATH with the path to the model.

## Run
### Prepare and build
```
conda create -n pca_langchain python=3.10
conda activate pca_langchain
pip install -r requirements.txt
```
Note: llama-cpp-python needs to installed seperately

### Execute application
```
python3 main.py
```

## Windows 11 Setup (Not updated)

Failed to install llama-cpp-python on Windows11
Error indicates nmake not available:
```
'nmake' '-?'
```
Install Visual Studio with C++ support (e.g. Destop app development)
https://visualstudio.microsoft.com/zh-hans/downloads/
Open Visual Studio
```
conda activate pca_langchain
pip install -r .\requirements.txt
```


llama.cpp CUDA (Not work)
Guide https://github.com/ggerganov/llama.cpp#cublas
CUDA installation
https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64&target_version=11&target_type=exe_local


llama.dll [WinError 193] %1 not Win32 


Setup
```
conda create --name=pca_langchain python=3.10
conda activate pca_langchain
pip install -r .\requirements.txt
```

Reference
Using llama 2 models for text embedding with LangChain
https://medium.com/@liusimao8/using-llama-2-models-for-text-embedding-with-langchain-79183350593d#:~:text=%23%25pip%20install%20--upgrade%20llama-cpp-python%20%23%25pip%20install%20--upgrade%20langchain,the%20context%20window%20size%20for%20embedding%2C%20e.g.%202048

