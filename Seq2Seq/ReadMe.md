
# Sequence to Sequence (Seq2Seq) Model for Translation

- **Dataset**: The model is trained on a dataset of English to Morse code translations.
- **Model**: A simple Seq2Seq model

## Requirements

- Python 3.11.6

```
C:\Workspace\Git_Repos\ML_PoC\Seq2Seq>conda create -n seq2seq python=3.11.6

Channels:
 - conda-forge
Platform: win-64
Collecting package metadata (repodata.json): done
Solving environment: done

==> WARNING: A newer version of conda exists. <==
    current version: 24.9.0
    latest version: 25.5.1

Please update conda by running

    $ conda update -n base -c conda-forge conda

## Package Plan ##

  environment location: C:\Workspace\Softwares\Miniforge3\envs\seq2seq

  added / updated specs:
    - python=3.11.6

The following NEW packages will be INSTALLED:

  bzip2              conda-forge/win-64::bzip2-1.0.8-h2466b09_7
  ca-certificates    conda-forge/noarch::ca-certificates-2025.4.26-h4c7d964_0
  libexpat           conda-forge/win-64::libexpat-2.7.0-he0c23c2_0
  libffi             conda-forge/win-64::libffi-3.4.6-h537db12_1
  liblzma            conda-forge/win-64::liblzma-5.8.1-h2466b09_2
  liblzma-devel      conda-forge/win-64::liblzma-devel-5.8.1-h2466b09_2
  libsqlite          conda-forge/win-64::libsqlite-3.50.1-h67fdade_0
  libzlib            conda-forge/win-64::libzlib-1.3.1-h2466b09_2
  openssl            conda-forge/win-64::openssl-3.5.0-ha4e3fda_1
  pip                conda-forge/noarch::pip-25.1.1-pyh8b19718_0
  python             conda-forge/win-64::python-3.11.6-h2628c8c_0_cpython
  setuptools         conda-forge/noarch::setuptools-80.9.0-pyhff2d567_0
  tk                 conda-forge/win-64::tk-8.6.13-h2c6b04d_2
  tzdata             conda-forge/noarch::tzdata-2025b-h78e105d_0
  ucrt               conda-forge/win-64::ucrt-10.0.22621.0-h57928b3_1
  vc                 conda-forge/win-64::vc-14.3-h2b53caa_26
  vc14_runtime       conda-forge/win-64::vc14_runtime-14.42.34438-hfd919c2_26
  wheel              conda-forge/noarch::wheel-0.45.1-pyhd8ed1ab_1
  xz                 conda-forge/win-64::xz-5.8.1-h208afaa_2
  xz-tools           conda-forge/win-64::xz-tools-5.8.1-h2466b09_2

Proceed ([y]/n)? y

Downloading and Extracting Packages:

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate seq2seq
#
# To deactivate an active environment, use
#
#     $ conda deactivate

C:\Workspace\Git_Repos\ML_PoC\Seq2Seq>conda activate seq2seq

(seq2seq) C:\Workspace\Git_Repos\ML_PoC\Seq2Seq>python -m pip install -r reqs.txt
Collecting certifi==2025.4.26 (from -r reqs.txt (line 1))
  Using cached certifi-2025.4.26-py3-none-any.whl.metadata (2.5 kB)
Collecting charset-normalizer==3.4.2 (from -r reqs.txt (line 2))
  Using cached charset_normalizer-3.4.2-cp311-cp311-win_amd64.whl.metadata (36 kB)
Collecting colorama==0.4.6 (from -r reqs.txt (line 3))
  Using cached colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)
Collecting filelock==3.18.0 (from -r reqs.txt (line 4))
  Using cached filelock-3.18.0-py3-none-any.whl.metadata (2.9 kB)
Collecting fsspec==2025.5.1 (from -r reqs.txt (line 5))
  Using cached fsspec-2025.5.1-py3-none-any.whl.metadata (11 kB)
Collecting idna==3.10 (from -r reqs.txt (line 6))
  Using cached idna-3.10-py3-none-any.whl.metadata (10 kB)
Collecting Jinja2==3.1.6 (from -r reqs.txt (line 7))
  Using cached jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting MarkupSafe==3.0.2 (from -r reqs.txt (line 8))
  Using cached MarkupSafe-3.0.2-cp311-cp311-win_amd64.whl.metadata (4.1 kB)
Collecting mpmath==1.3.0 (from -r reqs.txt (line 9))
  Using cached mpmath-1.3.0-py3-none-any.whl.metadata (8.6 kB)
Collecting networkx==3.5 (from -r reqs.txt (line 10))
  Using cached networkx-3.5-py3-none-any.whl.metadata (6.3 kB)
Collecting numpy==2.3.0 (from -r reqs.txt (line 11))
  Using cached numpy-2.3.0-cp311-cp311-win_amd64.whl.metadata (60 kB)
Collecting requests==2.32.3 (from -r reqs.txt (line 12))
  Using cached requests-2.32.3-py3-none-any.whl.metadata (4.6 kB)
Collecting sympy==1.14.0 (from -r reqs.txt (line 13))
  Using cached sympy-1.14.0-py3-none-any.whl.metadata (12 kB)
Collecting torch==2.7.1 (from -r reqs.txt (line 14))
  Using cached torch-2.7.1-cp311-cp311-win_amd64.whl.metadata (28 kB)
Collecting torchtext==0.18.0 (from -r reqs.txt (line 15))
  Using cached torchtext-0.18.0-cp311-cp311-win_amd64.whl.metadata (7.9 kB)
Collecting tqdm==4.67.1 (from -r reqs.txt (line 16))
  Using cached tqdm-4.67.1-py3-none-any.whl.metadata (57 kB)
Collecting typing_extensions==4.14.0 (from -r reqs.txt (line 17))
  Using cached typing_extensions-4.14.0-py3-none-any.whl.metadata (3.0 kB)
Collecting urllib3==2.4.0 (from -r reqs.txt (line 18))
  Using cached urllib3-2.4.0-py3-none-any.whl.metadata (6.5 kB)
Using cached certifi-2025.4.26-py3-none-any.whl (159 kB)
Using cached charset_normalizer-3.4.2-cp311-cp311-win_amd64.whl (105 kB)
Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Using cached filelock-3.18.0-py3-none-any.whl (16 kB)
Using cached fsspec-2025.5.1-py3-none-any.whl (199 kB)
Using cached idna-3.10-py3-none-any.whl (70 kB)
Using cached jinja2-3.1.6-py3-none-any.whl (134 kB)
Using cached MarkupSafe-3.0.2-cp311-cp311-win_amd64.whl (15 kB)
Using cached mpmath-1.3.0-py3-none-any.whl (536 kB)
Using cached networkx-3.5-py3-none-any.whl (2.0 MB)
Using cached numpy-2.3.0-cp311-cp311-win_amd64.whl (13.0 MB)
Using cached requests-2.32.3-py3-none-any.whl (64 kB)
Using cached urllib3-2.4.0-py3-none-any.whl (128 kB)
Using cached sympy-1.14.0-py3-none-any.whl (6.3 MB)
Using cached torch-2.7.1-cp311-cp311-win_amd64.whl (216.1 MB)
Using cached torchtext-0.18.0-cp311-cp311-win_amd64.whl (1.9 MB)
Using cached tqdm-4.67.1-py3-none-any.whl (78 kB)
Using cached typing_extensions-4.14.0-py3-none-any.whl (43 kB)
Installing collected packages: mpmath, urllib3, typing_extensions, sympy, numpy, networkx, MarkupSafe, idna, fsspec, filelock, colorama, charset-normalizer, certifi, tqdm, requests, Jinja2, torch, torchtext
Successfully installed Jinja2-3.1.6 MarkupSafe-3.0.2 certifi-2025.4.26 charset-normalizer-3.4.2 colorama-0.4.6 filelock-3.18.0 fsspec-2025.5.1 idna-3.10 mpmath-1.3.0 networkx-3.5 numpy-2.3.0 requests-2.32.3 sympy-1.14.0 torch-2.7.1 torchtext-0.18.0 tqdm-4.67.1 typing_extensions-4.14.0 urllib3-2.4.0
```

- Execute train.py script to train the model based on dataset.

```
(seq2seq) C:\Workspace\Git_Repos\ML_PoC\Seq2Seq>python train.py
C:\Workspace\Softwares\Miniforge3\envs\seq2seq\Lib\site-packages\torch\nn\functional.py:5962: UserWarning: Support for mismatched key_padding_mask and attn_mask is deprecated. Use same type for both instead.
  warnings.warn(
Epoch 1 Loss: 39.3546
Epoch 2 Loss: 33.8759
Epoch 3 Loss: 32.1336
Epoch 4 Loss: 30.9753
Epoch 5 Loss: 30.1217
Epoch 6 Loss: 29.4750
Epoch 7 Loss: 28.9840
Epoch 8 Loss: 28.5536
Epoch 9 Loss: 28.1873
Epoch 10 Loss: 27.8609
Epoch 11 Loss: 27.5282
Epoch 12 Loss: 27.2465
Epoch 13 Loss: 27.2799
Epoch 14 Loss: 26.9927
Epoch 15 Loss: 26.5916
Epoch 16 Loss: 26.2629
Epoch 17 Loss: 25.9517
Epoch 18 Loss: 25.4721
Epoch 19 Loss: 25.0357
Epoch 20 Loss: 24.8091
Epoch 21 Loss: 24.6185
Epoch 22 Loss: 24.4527
Epoch 23 Loss: 23.9128
Epoch 24 Loss: 23.5125
Epoch 25 Loss: 23.1119
Epoch 26 Loss: 22.7437
Epoch 27 Loss: 22.1606
Epoch 28 Loss: 21.9880
Epoch 29 Loss: 21.5122
Epoch 30 Loss: 21.0833
Elapsed time: 0:25:43
```
