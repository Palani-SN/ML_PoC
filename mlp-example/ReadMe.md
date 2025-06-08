
# Multi Layer Perceptron Example

- This is a simple example of a Multi Layer Perceptron (MLP) using PyTorch

## Requirements

- Python 3.11.6

```
C:\Workspace\Git_Repos\ML_PoC\mlp-example>conda create -n mlp-example python=3.11.6

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

  environment location: C:\Workspace\Softwares\Miniforge3\envs\mlp-example

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
#     $ conda activate mlp-example
#
# To deactivate an active environment, use
#
#     $ conda deactivate

C:\Workspace\Git_Repos\ML_PoC\mlp-example>conda activate mlp-example

(mlp-example) C:\Workspace\Git_Repos\ML_PoC\mlp-example>python -m pip install -r reqs.txt
Collecting contourpy==1.3.2 (from -r reqs.txt (line 1))
  Using cached contourpy-1.3.2-cp311-cp311-win_amd64.whl.metadata (5.5 kB)
Collecting cycler==0.12.1 (from -r reqs.txt (line 2))
  Using cached cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
Collecting filelock==3.18.0 (from -r reqs.txt (line 3))
  Using cached filelock-3.18.0-py3-none-any.whl.metadata (2.9 kB)
Collecting fonttools==4.57.0 (from -r reqs.txt (line 4))
  Using cached fonttools-4.57.0-cp311-cp311-win_amd64.whl.metadata (104 kB)
Collecting fsspec==2025.3.2 (from -r reqs.txt (line 5))
  Using cached fsspec-2025.3.2-py3-none-any.whl.metadata (11 kB)
Collecting Jinja2==3.1.6 (from -r reqs.txt (line 6))
  Using cached jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting joblib==1.4.2 (from -r reqs.txt (line 7))
  Using cached joblib-1.4.2-py3-none-any.whl.metadata (5.4 kB)
Collecting kiwisolver==1.4.8 (from -r reqs.txt (line 8))
  Using cached kiwisolver-1.4.8-cp311-cp311-win_amd64.whl.metadata (6.3 kB)
Collecting MarkupSafe==3.0.2 (from -r reqs.txt (line 9))
  Using cached MarkupSafe-3.0.2-cp311-cp311-win_amd64.whl.metadata (4.1 kB)
Collecting matplotlib==3.10.1 (from -r reqs.txt (line 10))
  Using cached matplotlib-3.10.1-cp311-cp311-win_amd64.whl.metadata (11 kB)
Collecting mpmath==1.3.0 (from -r reqs.txt (line 11))
  Using cached mpmath-1.3.0-py3-none-any.whl.metadata (8.6 kB)
Collecting networkx==3.4.2 (from -r reqs.txt (line 12))
  Using cached networkx-3.4.2-py3-none-any.whl.metadata (6.3 kB)
Collecting numpy==2.2.5 (from -r reqs.txt (line 13))
  Using cached numpy-2.2.5-cp311-cp311-win_amd64.whl.metadata (60 kB)
Collecting packaging==25.0 (from -r reqs.txt (line 14))
  Using cached packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
Collecting pandas==2.2.3 (from -r reqs.txt (line 15))
  Using cached pandas-2.2.3-cp311-cp311-win_amd64.whl.metadata (19 kB)
Collecting pillow==11.2.1 (from -r reqs.txt (line 16))
  Using cached pillow-11.2.1-cp311-cp311-win_amd64.whl.metadata (9.1 kB)
Collecting psutil==7.0.0 (from -r reqs.txt (line 17))
  Using cached psutil-7.0.0-cp37-abi3-win_amd64.whl.metadata (23 kB)
Collecting pyparsing==3.2.3 (from -r reqs.txt (line 18))
  Using cached pyparsing-3.2.3-py3-none-any.whl.metadata (5.0 kB)
Collecting python-dateutil==2.9.0.post0 (from -r reqs.txt (line 19))
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting pytz==2025.2 (from -r reqs.txt (line 20))
  Using cached pytz-2025.2-py2.py3-none-any.whl.metadata (22 kB)
Collecting scikit-learn==1.6.1 (from -r reqs.txt (line 21))
  Using cached scikit_learn-1.6.1-cp311-cp311-win_amd64.whl.metadata (15 kB)
Collecting scipy==1.15.2 (from -r reqs.txt (line 22))
  Using cached scipy-1.15.2-cp311-cp311-win_amd64.whl.metadata (60 kB)
Collecting seaborn==0.13.2 (from -r reqs.txt (line 23))
  Using cached seaborn-0.13.2-py3-none-any.whl.metadata (5.4 kB)
Collecting six==1.17.0 (from -r reqs.txt (line 24))
  Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting sympy==1.14.0 (from -r reqs.txt (line 25))
  Using cached sympy-1.14.0-py3-none-any.whl.metadata (12 kB)
Collecting threadpoolctl==3.6.0 (from -r reqs.txt (line 26))
  Using cached threadpoolctl-3.6.0-py3-none-any.whl.metadata (13 kB)
Collecting torch==2.7.0 (from -r reqs.txt (line 27))
  Using cached torch-2.7.0-cp311-cp311-win_amd64.whl.metadata (29 kB)
Collecting typing_extensions==4.13.2 (from -r reqs.txt (line 28))
  Using cached typing_extensions-4.13.2-py3-none-any.whl.metadata (3.0 kB)
Collecting tzdata==2025.2 (from -r reqs.txt (line 29))
  Using cached tzdata-2025.2-py2.py3-none-any.whl.metadata (1.4 kB)
Using cached contourpy-1.3.2-cp311-cp311-win_amd64.whl (222 kB)
Using cached cycler-0.12.1-py3-none-any.whl (8.3 kB)
Using cached filelock-3.18.0-py3-none-any.whl (16 kB)
Using cached fonttools-4.57.0-cp311-cp311-win_amd64.whl (2.2 MB)
Using cached fsspec-2025.3.2-py3-none-any.whl (194 kB)
Using cached jinja2-3.1.6-py3-none-any.whl (134 kB)
Using cached joblib-1.4.2-py3-none-any.whl (301 kB)
Using cached kiwisolver-1.4.8-cp311-cp311-win_amd64.whl (71 kB)
Using cached MarkupSafe-3.0.2-cp311-cp311-win_amd64.whl (15 kB)
Using cached matplotlib-3.10.1-cp311-cp311-win_amd64.whl (8.1 MB)
Using cached mpmath-1.3.0-py3-none-any.whl (536 kB)
Using cached networkx-3.4.2-py3-none-any.whl (1.7 MB)
Using cached numpy-2.2.5-cp311-cp311-win_amd64.whl (12.9 MB)
Using cached packaging-25.0-py3-none-any.whl (66 kB)
Using cached pandas-2.2.3-cp311-cp311-win_amd64.whl (11.6 MB)
Using cached pillow-11.2.1-cp311-cp311-win_amd64.whl (2.7 MB)
Using cached psutil-7.0.0-cp37-abi3-win_amd64.whl (244 kB)
Using cached pyparsing-3.2.3-py3-none-any.whl (111 kB)
Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Using cached pytz-2025.2-py2.py3-none-any.whl (509 kB)
Using cached scikit_learn-1.6.1-cp311-cp311-win_amd64.whl (11.1 MB)
Using cached scipy-1.15.2-cp311-cp311-win_amd64.whl (41.2 MB)
Using cached seaborn-0.13.2-py3-none-any.whl (294 kB)
Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
Using cached sympy-1.14.0-py3-none-any.whl (6.3 MB)
Using cached threadpoolctl-3.6.0-py3-none-any.whl (18 kB)
Using cached torch-2.7.0-cp311-cp311-win_amd64.whl (212.5 MB)
Using cached typing_extensions-4.13.2-py3-none-any.whl (45 kB)
Using cached tzdata-2025.2-py2.py3-none-any.whl (347 kB)
Installing collected packages: pytz, mpmath, tzdata, typing_extensions, threadpoolctl, sympy, six, pyparsing, psutil, pillow, packaging, numpy, networkx, MarkupSafe, kiwisolver, joblib, fsspec, fonttools, filelock, cycler, scipy, python-dateutil, Jinja2, contourpy, torch, scikit-learn, pandas, matplotlib, seaborn
Successfully installed Jinja2-3.1.6 MarkupSafe-3.0.2 contourpy-1.3.2 cycler-0.12.1 filelock-3.18.0 fonttools-4.57.0 fsspec-2025.3.2 joblib-1.4.2 kiwisolver-1.4.8 matplotlib-3.10.1 mpmath-1.3.0 networkx-3.4.2 numpy-2.2.5 packaging-25.0 pandas-2.2.3 pillow-11.2.1 psutil-7.0.0 pyparsing-3.2.3 python-dateutil-2.9.0.post0 pytz-2025.2 scikit-learn-1.6.1 scipy-1.15.2 seaborn-0.13.2 six-1.17.0 sympy-1.14.0 threadpoolctl-3.6.0 torch-2.7.0 typing_extensions-4.13.2 tzdata-2025.2
```

- Execute the script prep-data.py to prepare the training & evaluation data.

```
(mlp-example) C:\Workspace\Git_Repos\ML_PoC\mlp-example>python prep_data.py
         px        py        pz        ox        oy        oz         rd  class
0 -6.084694  4.791542 -3.927527  1.948192 -1.406630 -6.893320  32.150205      0
1  4.867498  6.513008  6.481351  8.473087 -6.607016  1.320428  86.604661      0
2  9.126541 -2.570015 -0.204060  6.196580  7.734641  5.316933  70.768757      0
3  6.295454  8.117869 -7.645229  2.883226 -3.425730 -9.160692  34.205931      0
4 -5.118269  0.581593  3.648440 -2.189916 -0.294536 -7.022426  24.110035      0
Dataframe created successfully!
         px        py        pz        ox        oy        oz         rd  class
0 -6.455661 -0.305464  9.901615 -6.399935  0.723484 -0.348646  80.958953      0
1 -3.090981  8.601454  4.434033  7.762782 -5.001719 -5.926420  78.160999      0
2 -5.942529 -3.328894 -0.217546 -3.569549  6.743810 -1.062922  44.925511      0
3  3.680177 -8.657767 -7.025662 -1.394438  3.928154  4.126940  44.533533      0
4 -0.172150  6.448633 -8.517429 -8.533419 -8.514572 -6.440129  93.277305      0
Dataframe created successfully!
```

- Execute the script train.py to train the MLP model on the prepared 

```
(mlp-example) C:\Workspace\Git_Repos\ML_PoC\mlp-example>python mlp-demo.py
PyTorch version: 2.7.0+cpu
PyTorch is using 14 CPU threads
Epoch 1: Train Loss = 0.2822, Val Acc = 0.9717
✅ New best model saved (val acc = 0.9717)
Epoch 2: Train Loss = 0.0931, Val Acc = 0.9771
✅ New best model saved (val acc = 0.9771)
Epoch 3: Train Loss = 0.0699, Val Acc = 0.9817
✅ New best model saved (val acc = 0.9817)
Epoch 4: Train Loss = 0.0574, Val Acc = 0.9824
✅ New best model saved (val acc = 0.9824)
Epoch 5: Train Loss = 0.0521, Val Acc = 0.9806
⚠️ No improvement. Patience: 1/5
Epoch 6: Train Loss = 0.0470, Val Acc = 0.9844
✅ New best model saved (val acc = 0.9844)
Epoch 7: Train Loss = 0.0424, Val Acc = 0.9844
⚠️ No improvement. Patience: 1/5
Epoch 8: Train Loss = 0.0407, Val Acc = 0.9834
⚠️ No improvement. Patience: 2/5
Epoch 9: Train Loss = 0.0381, Val Acc = 0.9880
✅ New best model saved (val acc = 0.9880)
Epoch 10: Train Loss = 0.0377, Val Acc = 0.9850
⚠️ No improvement. Patience: 1/5
Epoch 11: Train Loss = 0.0321, Val Acc = 0.9857
⚠️ No improvement. Patience: 2/5
Epoch 12: Train Loss = 0.0323, Val Acc = 0.9847
⚠️ No improvement. Patience: 3/5
Epoch 13: Train Loss = 0.0309, Val Acc = 0.9860
⚠️ No improvement. Patience: 4/5
Epoch 14: Train Loss = 0.0322, Val Acc = 0.9857
⚠️ No improvement. Patience: 5/5
⏹️ Early stopping triggered.
🎯 Training complete. Best validation accuracy: 0.9880

🧾 Classification Report:
              precision    recall  f1-score   support

           0      0.996     0.993     0.994      1000
           1      0.995     0.977     0.986      1000
           2      0.974     0.994     0.984      1000

    accuracy                          0.988      3000
   macro avg      0.988     0.988     0.988      3000
weighted avg      0.988     0.988     0.988      3000

Training took 54.39 seconds.
```