# ChatBot

## Set Up:

### Linux:
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


### Changing the cache directory:

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
