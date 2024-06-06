* Torch install

```bash
* Collecting torch
  Obtaining dependency information for torch from [files.pythonhosted.org/packages/e1/24/f7fe3fe82583e6891cc3fceeb390f192f6c7f1d87e5a99a949ed33c96167/torch-2.1.0-cp38-cp38-manylinux1_x86_64.whl.metadata](https://files.pythonhosted.org/packages/e1/24/f7fe3fe82583e6891cc3fceeb390f192f6c7f1d87e5a99a949ed33c96167/torch-2.1.0-cp38-cp38-manylinux1_x86_64.whl.metadata)
  Downloading torch-2.1.0-cp38-cp38-manylinux1_x86_64.whl.metadata (25 kB)
* Collecting torchvision
  Obtaining dependency information for torchvision from [files.pythonhosted.org/packages/c9/52/d3f1c4253ad17e4ab08a2230fb184a3a180e2348db6c144c64977335b654/torchvision-0.16.0-cp38-cp38-manylinux1_x86_64.whl.metadata](https://files.pythonhosted.org/packages/c9/52/d3f1c4253ad17e4ab08a2230fb184a3a180e2348db6c144c64977335b654/torchvision-0.16.0-cp38-cp38-manylinux1_x86_64.whl.metadata)
  Downloading torchvision-0.16.0-cp38-cp38-manylinux1_x86_64.whl.metadata (6.6 kB)
* Requirement already satisfied: filelock in /root/.pyenv/versions/3.8.16/lib/python3.8/site-packages (from torch) (3.12.2)
* Requirement already satisfied: typing-extensions in /root/.pyenv/versions/3.8.16/lib/python3.8/site-packages (from torch) (4.8.0)
* Collecting sympy (from torch)
  Downloading sympy-1.12-py3-none-any.whl (5.7 MB)
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.7/5.7 MB 12.0 MB/s eta 0:00:00
* Collecting networkx (from torch)
  Downloading networkx-3.1-py3-none-any.whl (2.1 MB)
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 19.0 MB/s eta 0:00:00
* Collecting jinja2 (from torch)
  Downloading Jinja2-3.1.2-py3-none-any.whl (133 kB)
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 133.1/133.1 kB 12.7 MB/s eta 0:00:00
* Collecting fsspec (from torch)
  Obtaining dependency information for fsspec from [files.pythonhosted.org/packages/e8/f6/3eccfb530aac90ad1301c582da228e4763f19e719ac8200752a4841b0b2d/fsspec-2023.10.0-py3-none-any.whl.metadata](https://files.pythonhosted.org/packages/e8/f6/3eccfb530aac90ad1301c582da228e4763f19e719ac8200752a4841b0b2d/fsspec-2023.10.0-py3-none-any.whl.metadata)
  Downloading fsspec-2023.10.0-py3-none-any.whl.metadata (6.8 kB)
* Collecting nvidia-cuda-nvrtc-cu12==12.1.105 (from torch)
  Downloading nvidia_cuda_nvrtc_cu12-12.1.105-py3-none-manylinux1_x86_64.whl (23.7 MB)
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 23.7/23.7 MB 24.2 MB/s eta 0:00:00
* Collecting nvidia-cuda-runtime-cu12==12.1.105 (from torch)
  Downloading nvidia_cuda_runtime_cu12-12.1.105-py3-none-manylinux1_x86_64.whl (823 kB)
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 823.6/823.6 kB 22.8 MB/s eta 0:00:00
* Collecting nvidia-cuda-cupti-cu12==12.1.105 (from torch)
  Downloading nvidia_cuda_cupti_cu12-12.1.105-py3-none-manylinux1_x86_64.whl (14.1 MB)
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 14.1/14.1 MB 29.5 MB/s eta 0:00:00
* Collecting nvidia-cudnn-cu12==8.9.2.26 (from torch)
  Obtaining dependency information for nvidia-cudnn-cu12==8.9.2.26 from [files.pythonhosted.org/packages/ff/74/a2e2be7fb83aaedec84f391f082cf765dfb635e7caa9b49065f73e4835d8/nvidia_cudnn_cu12-8.9.2.26-py3-none-manylinux1_x86_64.whl.metadata](https://files.pythonhosted.org/packages/ff/74/a2e2be7fb83aaedec84f391f082cf765dfb635e7caa9b49065f73e4835d8/nvidia_cudnn_cu12-8.9.2.26-py3-none-manylinux1_x86_64.whl.metadata)
  Downloading nvidia_cudnn_cu12-8.9.2.26-py3-none-manylinux1_x86_64.whl.metadata (1.6 kB)
* Collecting nvidia-cublas-cu12==12.1.3.1 (from torch)
  Downloading nvidia_cublas_cu12-12.1.3.1-py3-none-manylinux1_x86_64.whl (410.6 MB)
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 410.6/410.6 MB 5.4 MB/s eta 0:00:00
* Collecting nvidia-cufft-cu12==11.0.2.54 (from torch)
  Downloading nvidia_cufft_cu12-11.0.2.54-py3-none-manylinux1_x86_64.whl (121.6 MB)
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 121.6/121.6 MB 16.4 MB/s eta 0:00:00
* Collecting nvidia-curand-cu12==10.3.2.106 (from torch)
  Downloading nvidia_curand_cu12-10.3.2.106-py3-none-manylinux1_x86_64.whl (56.5 MB)
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 56.5/56.5 MB 23.2 MB/s eta 0:00:00
* Collecting nvidia-cusolver-cu12==11.4.5.107 (from torch)
  Downloading nvidia_cusolver_cu12-11.4.5.107-py3-none-manylinux1_x86_64.whl (124.2 MB)
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 124.2/124.2 MB 16.6 MB/s eta 0:00:00
* Collecting nvidia-cusparse-cu12==12.1.0.106 (from torch)
  Downloading nvidia_cusparse_cu12-12.1.0.106-py3-none-manylinux1_x86_64.whl (196.0 MB)
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 196.0/196.0 MB 11.6 MB/s eta 0:00:00
* Collecting nvidia-nccl-cu12==2.18.1 (from torch)
  Downloading nvidia_nccl_cu12-2.18.1-py3-none-manylinux1_x86_64.whl (209.8 MB)
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 209.8/209.8 MB 11.1 MB/s eta 0:00:00
* Collecting nvidia-nvtx-cu12==12.1.105 (from torch)
  Downloading nvidia_nvtx_cu12-12.1.105-py3-none-manylinux1_x86_64.whl (99 kB)
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 99.1/99.1 kB 9.4 MB/s eta 0:00:00
* Collecting triton==2.1.0 (from torch)
  Obtaining dependency information for triton==2.1.0 from [files.pythonhosted.org/packages/72/98/34f43ed68ee6455ea874f749a5515c0600243186301ecd83819d942ce08a/triton-2.1.0-0-cp38-cp38-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata](https://files.pythonhosted.org/packages/72/98/34f43ed68ee6455ea874f749a5515c0600243186301ecd83819d942ce08a/triton-2.1.0-0-cp38-cp38-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata)
  Downloading triton-2.1.0-0-cp38-cp38-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (1.3 kB)
* Collecting nvidia-nvjitlink-cu12 (from nvidia-cusolver-cu12==11.4.5.107->torch)
  Obtaining dependency information for nvidia-nvjitlink-cu12 from [files.pythonhosted.org/packages/45/de/885b6d3e1fa07bf19124076b348d3cf30f68051f813cba99e103f53d2f75/nvidia_nvjitlink_cu12-12.3.52-py3-none-manylinux1_x86_64.whl.metadata](https://files.pythonhosted.org/packages/45/de/885b6d3e1fa07bf19124076b348d3cf30f68051f813cba99e103f53d2f75/nvidia_nvjitlink_cu12-12.3.52-py3-none-manylinux1_x86_64.whl.metadata)
  Downloading nvidia_nvjitlink_cu12-12.3.52-py3-none-manylinux1_x86_64.whl.metadata (1.5 kB)
* Collecting numpy (from torchvision)
  Obtaining dependency information for numpy from [files.pythonhosted.org/packages/98/5d/5738903efe0ecb73e51eb44feafba32bdba2081263d40c5043568ff60faf/numpy-1.24.4-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata](https://files.pythonhosted.org/packages/98/5d/5738903efe0ecb73e51eb44feafba32bdba2081263d40c5043568ff60faf/numpy-1.24.4-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata)
  Downloading numpy-1.24.4-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (5.6 kB)
* Requirement already satisfied: requests in /root/.pyenv/versions/3.8.16/lib/python3.8/site-packages (from torchvision) (2.31.0)
* Collecting pillow!=8.3.*,>=5.3.0 (from torchvision)
  Obtaining dependency information for pillow!=8.3.*,>=5.3.0 from [files.pythonhosted.org/packages/1e/74/638f982ab43fb3b19c8a151b1a0065cafefe436f8590c1c57d5fdf2475f1/Pillow-10.1.0-cp38-cp38-manylinux_2_28_x86_64.whl.metadata](https://files.pythonhosted.org/packages/1e/74/638f982ab43fb3b19c8a151b1a0065cafefe436f8590c1c57d5fdf2475f1/Pillow-10.1.0-cp38-cp38-manylinux_2_28_x86_64.whl.metadata)
  Downloading Pillow-10.1.0-cp38-cp38-manylinux_2_28_x86_64.whl.metadata (9.5 kB)
* Collecting MarkupSafe>=2.0 (from jinja2->torch)
  Obtaining dependency information for MarkupSafe>=2.0 from [files.pythonhosted.org/packages/de/e2/32c14301bb023986dff527a49325b6259cab4ebb4633f69de54af312fc45/MarkupSafe-2.1.3-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata](https://files.pythonhosted.org/packages/de/e2/32c14301bb023986dff527a49325b6259cab4ebb4633f69de54af312fc45/MarkupSafe-2.1.3-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata)
  Downloading MarkupSafe-2.1.3-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.0 kB)
* Requirement already satisfied: charset-normalizer<4,>=2 in /root/.pyenv/versions/3.8.16/lib/python3.8/site-packages (from requests->torchvision) (3.2.0)
* Requirement already satisfied: idna<4,>=2.5 in /root/.pyenv/versions/3.8.16/lib/python3.8/site-packages (from requests->torchvision) (3.4)
* Requirement already satisfied: urllib3<3,>=1.21.1 in /root/.pyenv/versions/3.8.16/lib/python3.8/site-packages (from requests->torchvision) (1.26.16)
* Requirement already satisfied: certifi>=2017.4.17 in /root/.pyenv/versions/3.8.16/lib/python3.8/site-packages (from requests->torchvision) (2023.7.22)
* Collecting mpmath>=0.19 (from sympy->torch)
  Downloading mpmath-1.3.0-py3-none-any.whl (536 kB)
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 536.2/536.2 kB 26.5 MB/s eta 0:00:00
* Downloading torch-2.1.0-cp38-cp38-manylinux1_x86_64.whl (670.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 670.2/670.2 MB 4.3 MB/s eta 0:00:00
* Downloading nvidia_cudnn_cu12-8.9.2.26-py3-none-manylinux1_x86_64.whl (731.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 731.7/731.7 MB 3.7 MB/s eta 0:00:00
* Downloading triton-2.1.0-0-cp38-cp38-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (89.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 89.2/89.2 MB 18.2 MB/s eta 0:00:00
* Downloading torchvision-0.16.0-cp38-cp38-manylinux1_x86_64.whl (6.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.9/6.9 MB 32.7 MB/s eta 0:00:00
* Downloading Pillow-10.1.0-cp38-cp38-manylinux_2_28_x86_64.whl (3.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.6/3.6 MB 31.9 MB/s eta 0:00:00
* Downloading fsspec-2023.10.0-py3-none-any.whl (166 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 166.4/166.4 kB 11.0 MB/s eta 0:00:00
* Downloading numpy-1.24.4-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (17.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 17.3/17.3 MB 34.0 MB/s eta 0:00:00
* Downloading MarkupSafe-2.1.3-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (25 kB)
* Downloading nvidia_nvjitlink_cu12-12.3.52-py3-none-manylinux1_x86_64.whl (20.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 20.5/20.5 MB 31.4 MB/s eta 0:00:00
* Installing collected packages: mpmath, triton, sympy, pillow, nvidia-nvtx-cu12, nvidia-nvjitlink-cu12, nvidia-nccl-cu12, nvidia-curand-cu12, nvidia-cufft-cu12, nvidia-cuda-runtime-cu12, nvidia-cuda-nvrtc-cu12, nvidia-cuda-cupti-cu12, nvidia-cublas-cu12, numpy, networkx, MarkupSafe, fsspec, nvidia-cusparse-cu12, nvidia-cudnn-cu12, jinja2, nvidia-cusolver-cu12, torch, torchvision
* Successfully installed MarkupSafe-2.1.3 fsspec-2023.10.0 jinja2-3.1.2 mpmath-1.3.0 networkx-3.1 numpy-1.24.4 nvidia-cublas-cu12-12.1.3.1 nvidia-cuda-cupti-cu12-12.1.105 nvidia-cuda-nvrtc-cu12-12.1.105 nvidia-cuda-runtime-cu12-12.1.105 nvidia-cudnn-cu12-8.9.2.26 nvidia-cufft-cu12-11.0.2.54 nvidia-curand-cu12-10.3.2.106 nvidia-cusolver-cu12-11.4.5.107 nvidia-cusparse-cu12-12.1.0.106 nvidia-nccl-cu12-2.18.1 nvidia-nvjitlink-cu12-12.3.52 nvidia-nvtx-cu12-12.1.105 pillow-10.1.0 sympy-1.12 torch-2.1.0 torchvision-0.16.0 triton-2.1.0
* WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: [pip.pypa.io/warnings/venv](https://pip.pypa.io/warnings/venv)

```
