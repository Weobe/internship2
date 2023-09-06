# ChatBot

## Set Up:

### Linux
  Make sure you have a Nvidia GPU with at least 16 GB RAM. Download and set up Cuda using [this guide](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html)

  Create a new python environment and activate it:
  ```
  python3 -m venv <environment_name>
  source <environment_name>/bin/activate
  ```

  Clone the repository:

  ```
  git clone https://github.com/Weobe/internship2.git
  cd internship2
  ```


### Changing the cache directory

  You can skip this step if you want to use the default cache.
  
  Replace '/mnt/tmp' in environ.sh with the desired directory.
  Then run

  ```
  source environ.sh
  ```

### Required python modules
  Download the required python modules: 
  
  (add the `--cache-dir=$TMPDIR` and `--build $TMPDIR` options if you changed the cache directory)
  ```
  pip install torch
  pip install git+https://github.com/huggingface/transformers
  pip install datasets loralib sentencepiece
  pip install bitsandbytes accelerate xformers einops
  pip install langchain
  pip install scipy
  pip install sentence_transformers
  pip install faiss-gpu
  pip install pypdf
  ```

### First run
  Log in or sign up to [Hugging Face](https://huggingface.co/) and get an access token following [this guide](https://huggingface.co/docs/hub/security-tokens)

  Run huggingface_login.py and enter your personal access token.

  Then run load_models.py and load_sentence_transformer.py. This might take some time depending on the download speed.

  Now that the models are stored in your cache directory, you can run main.py to start your Chat Bot!


### Usage
  Whenever you start a new chat, the bot will ask for the domain of your questions. This feature makes sure that the answers will meet your expectations. If not sure, type `general chat` for a casual conversation. 

  Once you specify the domain, you can ask as many questions as you like! If you want to start a different chat, type `exit`.
  
  In order to use the document understanding / Q&A feature, type `pdf` as your domain. The bot will then prompt you to type the pdf name. You can type the name with or without the `.pdf` extension. Make sure that the pdf documents are stored in the same directory with main.py.

  Once you enter the name, you can again ask as many questions as you like. When you are done, type `exit` to start a new chat.


### Additional tips:

  In case of "Permission denied" errors under `/mnt`: 
  Make a new directory and change its ownership to azrsrvadm. Perform all steps under this directory.
  
    ```
    sudo chown -R azrsrvadm:azrsrvadm /mnt/<new_directory>
    cd <new_directory>
    ```

  
  

  
