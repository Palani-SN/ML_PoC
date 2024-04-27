# 2D Mask-RCNN

- clone the repo
- run **setup_dev.sh** for local wsl2 instance or **setup_rel.sh** for colab instance

```
output

(base) palani-sn@DESKTOP-EJPA9NB:~$ conda deactivate
palani-sn@DESKTOP-EJPA9NB:~$ cd /mnt/d/GitRepos/ML_PoC
palani-sn@DESKTOP-EJPA9NB:/mnt/d/GitRepos/ML_PoC$ source setup_dev.sh
conda 24.3.0
no change     /home/palani-sn/miniconda3/condabin/conda
no change     /home/palani-sn/miniconda3/bin/conda
no change     /home/palani-sn/miniconda3/bin/conda-env
no change     /home/palani-sn/miniconda3/bin/activate
no change     /home/palani-sn/miniconda3/bin/deactivate
no change     /home/palani-sn/miniconda3/etc/profile.d/conda.sh
no change     /home/palani-sn/miniconda3/etc/fish/conf.d/conda.fish
no change     /home/palani-sn/miniconda3/shell/condabin/Conda.psm1
no change     /home/palani-sn/miniconda3/shell/condabin/conda-hook.ps1
no change     /home/palani-sn/miniconda3/lib/python3.12/site-packages/xontrib/conda.xsh
no change     /home/palani-sn/miniconda3/etc/profile.d/conda.csh
no change     /home/palani-sn/.bashrc
No action taken.
close and reopen the shell to create and activate conda

```

- close and reopen the shell, then run **create_env.sh**

```
output

(base) palani-sn@DESKTOP-EJPA9NB:~$ conda deactivate
palani-sn@DESKTOP-EJPA9NB:~$ cd /mnt/d/GitRepos/ML_PoC
palani-sn@DESKTOP-EJPA9NB:/mnt/d/GitRepos/ML_PoC$ source create_env.sh
WARNING: A conda environment already exists at '/home/palani-sn/miniconda3/envs/hash_dataset'
Remove existing environment (y/[n])? y

Channels:
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/palani-sn/miniconda3/envs/hash_dataset

  added / updated specs:
    - python=3.7.3


The following NEW packages will be INSTALLED:

  _libgcc_mutex      pkgs/main/linux-64::_libgcc_mutex-0.1-main
  _openmp_mutex      pkgs/main/linux-64::_openmp_mutex-5.1-1_gnu
  ca-certificates    pkgs/main/linux-64::ca-certificates-2024.3.11-h06a4308_0
  certifi            pkgs/main/linux-64::certifi-2022.12.7-py37h06a4308_0
  libedit            pkgs/main/linux-64::libedit-3.1.20230828-h5eee18b_0
  libffi             pkgs/main/linux-64::libffi-3.2.1-hf484d3e_1007
  libgcc-ng          pkgs/main/linux-64::libgcc-ng-11.2.0-h1234567_1
  libgomp            pkgs/main/linux-64::libgomp-11.2.0-h1234567_1
  libstdcxx-ng       pkgs/main/linux-64::libstdcxx-ng-11.2.0-h1234567_1
  ncurses            pkgs/main/linux-64::ncurses-6.4-h6a678d5_0
  openssl            pkgs/main/linux-64::openssl-1.1.1w-h7f8727e_0
  pip                pkgs/main/linux-64::pip-22.3.1-py37h06a4308_0
  python             pkgs/main/linux-64::python-3.7.3-h0371630_0
  readline           pkgs/main/linux-64::readline-7.0-h7b6447c_5
  setuptools         pkgs/main/linux-64::setuptools-65.6.3-py37h06a4308_0
  sqlite             pkgs/main/linux-64::sqlite-3.33.0-h62c20be_0
  tk                 pkgs/main/linux-64::tk-8.6.12-h1ccaba5_0
  wheel              pkgs/main/linux-64::wheel-0.38.4-py37h06a4308_0
  xz                 pkgs/main/linux-64::xz-5.4.6-h5eee18b_0
  zlib               pkgs/main/linux-64::zlib-1.2.13-h5eee18b_0


Proceed ([y]/n)? y


Downloading and Extracting Packages:

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate hash_dataset
#
# To deactivate an active environment, use
#
#     $ conda deactivate

Collecting pydenticon
  Using cached pydenticon-0.3.1-py3-none-any.whl
Collecting Pillow
  Using cached Pillow-9.5.0-cp37-cp37m-manylinux_2_28_x86_64.whl (3.4 MB)
Installing collected packages: Pillow, pydenticon
Successfully installed Pillow-9.5.0 pydenticon-0.3.1
Collecting opencv-python
  Using cached opencv_python-4.9.0.80-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (62.2 MB)
Collecting numpy>=1.17.0
  Using cached numpy-1.21.6-cp37-cp37m-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (15.7 MB)
Installing collected packages: numpy, opencv-python
Successfully installed numpy-1.21.6 opencv-python-4.9.0.80
Collecting pandas
  Using cached pandas-1.3.5-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (11.3 MB)
Collecting python-dateutil>=2.7.3
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Requirement already satisfied: numpy>=1.17.3 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from pandas) (1.21.6)
Collecting pytz>=2017.3
  Using cached pytz-2024.1-py2.py3-none-any.whl (505 kB)
Collecting six>=1.5
  Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: pytz, six, python-dateutil, pandas
Successfully installed pandas-1.3.5 python-dateutil-2.9.0.post0 pytz-2024.1 six-1.16.0
Requirement already satisfied: numpy in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (1.21.6)
Collecting scipy
  Using cached scipy-1.7.3-cp37-cp37m-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (38.1 MB)
Requirement already satisfied: numpy<1.23.0,>=1.16.5 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from scipy) (1.21.6)
Installing collected packages: scipy
Successfully installed scipy-1.7.3
Requirement already satisfied: Pillow in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (9.5.0)
Collecting cython
  Using cached Cython-3.0.10-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.6 MB)
Installing collected packages: cython
Successfully installed cython-3.0.10
Collecting matplotlib
  Using cached matplotlib-3.5.3-cp37-cp37m-manylinux_2_5_x86_64.manylinux1_x86_64.whl (11.2 MB)
Collecting cycler>=0.10
  Using cached cycler-0.11.0-py3-none-any.whl (6.4 kB)
Collecting pyparsing>=2.2.1
  Using cached pyparsing-3.1.2-py3-none-any.whl (103 kB)
Collecting packaging>=20.0
  Using cached packaging-24.0-py3-none-any.whl (53 kB)
Collecting fonttools>=4.22.0
  Using cached fonttools-4.38.0-py3-none-any.whl (965 kB)
Collecting kiwisolver>=1.0.1
  Using cached kiwisolver-1.4.5-cp37-cp37m-manylinux_2_5_x86_64.manylinux1_x86_64.whl (1.1 MB)
Requirement already satisfied: python-dateutil>=2.7 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from matplotlib) (2.9.0.post0)
Requirement already satisfied: pillow>=6.2.0 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from matplotlib) (9.5.0)
Requirement already satisfied: numpy>=1.17 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from matplotlib) (1.21.6)
Collecting typing-extensions
  Using cached typing_extensions-4.7.1-py3-none-any.whl (33 kB)
Requirement already satisfied: six>=1.5 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from python-dateutil>=2.7->matplotlib) (1.16.0)
Installing collected packages: typing-extensions, pyparsing, packaging, fonttools, cycler, kiwisolver, matplotlib
Successfully installed cycler-0.11.0 fonttools-4.38.0 kiwisolver-1.4.5 matplotlib-3.5.3 packaging-24.0 pyparsing-3.1.2 typing-extensions-4.7.1
Collecting scikit-image==0.16.2
  Using cached scikit_image-0.16.2-cp37-cp37m-manylinux1_x86_64.whl (26.5 MB)
Requirement already satisfied: matplotlib!=3.0.0,>=2.0.0 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from scikit-image==0.16.2) (3.5.3)
Requirement already satisfied: scipy>=0.19.0 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from scikit-image==0.16.2) (1.7.3)
Requirement already satisfied: pillow>=4.3.0 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from scikit-image==0.16.2) (9.5.0)
Collecting networkx>=2.0
  Using cached networkx-2.6.3-py3-none-any.whl (1.9 MB)
Collecting PyWavelets>=0.4.0
  Using cached PyWavelets-1.3.0-cp37-cp37m-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl (6.4 MB)
Collecting imageio>=2.3.0
  Using cached imageio-2.31.2-py3-none-any.whl (313 kB)
Requirement already satisfied: numpy in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from imageio>=2.3.0->scikit-image==0.16.2) (1.21.6)
Requirement already satisfied: packaging>=20.0 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from matplotlib!=3.0.0,>=2.0.0->scikit-image==0.16.2) (24.0)
Requirement already satisfied: fonttools>=4.22.0 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from matplotlib!=3.0.0,>=2.0.0->scikit-image==0.16.2) (4.38.0)
Requirement already satisfied: python-dateutil>=2.7 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from matplotlib!=3.0.0,>=2.0.0->scikit-image==0.16.2) (2.9.0.post0)
Requirement already satisfied: kiwisolver>=1.0.1 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from matplotlib!=3.0.0,>=2.0.0->scikit-image==0.16.2) (1.4.5)
Requirement already satisfied: pyparsing>=2.2.1 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from matplotlib!=3.0.0,>=2.0.0->scikit-image==0.16.2) (3.1.2)
Requirement already satisfied: cycler>=0.10 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from matplotlib!=3.0.0,>=2.0.0->scikit-image==0.16.2) (0.11.0)
Requirement already satisfied: typing-extensions in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from kiwisolver>=1.0.1->matplotlib!=3.0.0,>=2.0.0->scikit-image==0.16.2) (4.7.1)
Requirement already satisfied: six>=1.5 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from python-dateutil>=2.7->matplotlib!=3.0.0,>=2.0.0->scikit-image==0.16.2) (1.16.0)
Installing collected packages: PyWavelets, networkx, imageio, scikit-image
Successfully installed PyWavelets-1.3.0 imageio-2.31.2 networkx-2.6.3 scikit-image-0.16.2
Collecting tensorflow==2.0.0
  Using cached tensorflow-2.0.0-cp37-cp37m-manylinux2010_x86_64.whl (86.3 MB)
Collecting tensorflow-estimator<2.1.0,>=2.0.0
  Using cached tensorflow_estimator-2.0.1-py2.py3-none-any.whl (449 kB)
Collecting grpcio>=1.8.6
  Using cached grpcio-1.62.2-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (5.6 MB)
Requirement already satisfied: six>=1.10.0 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from tensorflow==2.0.0) (1.16.0)
Collecting protobuf>=3.6.1
  Using cached protobuf-4.24.4-cp37-abi3-manylinux2014_x86_64.whl (311 kB)
Requirement already satisfied: numpy<2.0,>=1.16.0 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from tensorflow==2.0.0) (1.21.6)
Collecting tensorboard<2.1.0,>=2.0.0
  Using cached tensorboard-2.0.2-py3-none-any.whl (3.8 MB)
Collecting opt-einsum>=2.3.2
  Using cached opt_einsum-3.3.0-py3-none-any.whl (65 kB)
Requirement already satisfied: wheel>=0.26 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from tensorflow==2.0.0) (0.38.4)
Collecting google-pasta>=0.1.6
  Using cached google_pasta-0.2.0-py3-none-any.whl (57 kB)
Collecting termcolor>=1.1.0
Collecting wrapt>=1.11.1-2.3.0-py3-none-any.whl (6.9 kB)
  Using cached wrapt-1.16.0-cp37-cp37m-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (77 kB)
Collecting keras-preprocessing>=1.0.5
  Using cached Keras_Preprocessing-1.1.2-py2.py3-none-any.whl (42 kB)
Collecting keras-applications>=1.0.8
  Using cached Keras_Applications-1.0.8-py3-none-any.whl (50 kB)
Collecting gast==0.2.2
  Using cached gast-0.2.2-py3-none-any.whl
Collecting absl-py>=0.7.0
  Using cached absl_py-2.1.0-py3-none-any.whl (133 kB)
Collecting astor>=0.6.0
  Using cached astor-0.8.1-py2.py3-none-any.whl (27 kB)
Collecting h5py
  Using cached h5py-3.8.0-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (4.3 MB)
Collecting google-auth<2,>=1.6.3
  Using cached google_auth-1.35.0-py2.py3-none-any.whl (152 kB)
Collecting markdown>=2.6.8
  Using cached Markdown-3.4.4-py3-none-any.whl (94 kB)
Collecting werkzeug>=0.11.15
  Using cached Werkzeug-2.2.3-py3-none-any.whl (233 kB)
Collecting requests<3,>=2.21.0
  Using cached requests-2.31.0-py3-none-any.whl (62 kB)
Requirement already satisfied: setuptools>=41.0.0 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from tensorboard<2.1.0,>=2.0.0->tensorflow==2.0.0) (65.6.3)
Collecting google-auth-oauthlib<0.5,>=0.4.1
  Using cached google_auth_oauthlib-0.4.6-py2.py3-none-any.whl (18 kB)
Collecting rsa<5,>=3.1.4
  Using cached rsa-4.9-py3-none-any.whl (34 kB)
Collecting cachetools<5.0,>=2.0.0
  Using cached cachetools-4.2.4-py3-none-any.whl (10 kB)
Collecting pyasn1-modules>=0.2.1
  Using cached pyasn1_modules-0.3.0-py2.py3-none-any.whl (181 kB)
Collecting requests-oauthlib>=0.7.0
  Using cached requests_oauthlib-2.0.0-py2.py3-none-any.whl (24 kB)
Collecting importlib-metadata>=4.4
  Using cached importlib_metadata-6.7.0-py3-none-any.whl (22 kB)
Collecting charset-normalizer<4,>=2
  Using cached charset_normalizer-3.3.2-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (136 kB)
Collecting urllib3<3,>=1.21.1
  Using cached urllib3-2.0.7-py3-none-any.whl (124 kB)
Requirement already satisfied: certifi>=2017.4.17 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from requests<3,>=2.21.0->tensorboard<2.1.0,>=2.0.0->tensorflow==2.0.0) (2022.12.7)
Collecting idna<4,>=2.5
  Using cached idna-3.7-py3-none-any.whl (66 kB)
Collecting MarkupSafe>=2.1.1
  Using cached MarkupSafe-2.1.5-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (25 kB)
Requirement already satisfied: typing-extensions>=3.6.4 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from importlib-metadata>=4.4->markdown>=2.6.8->tensorboard<2.1.0,>=2.0.0->tensorflow==2.0.0) (4.7.1)
Collecting zipp>=0.5
  Using cached zipp-3.15.0-py3-none-any.whl (6.8 kB)
Collecting pyasn1<0.6.0,>=0.4.6
  Using cached pyasn1-0.5.1-py2.py3-none-any.whl (84 kB)
Collecting oauthlib>=3.0.0
  Using cached oauthlib-3.2.2-py3-none-any.whl (151 kB)
Installing collected packages: tensorflow-estimator, zipp, wrapt, urllib3, termcolor, pyasn1, protobuf, opt-einsum, oauthlib, MarkupSafe, keras-preprocessing, idna, h5py, grpcio, google-pasta, gast, charset-normalizer, cachetools, astor, absl-py, werkzeug, rsa, requests, pyasn1-modules, keras-applications, importlib-metadata, requests-oauthlib, markdown, google-auth, google-auth-oauthlib, tensorboard, tensorflow
Successfully installed MarkupSafe-2.1.5 absl-py-2.1.0 astor-0.8.1 cachetools-4.2.4 charset-normalizer-3.3.2 gast-0.2.2 google-auth-1.35.0 google-auth-oauthlib-0.4.6 google-pasta-0.2.0 grpcio-1.62.2 h5py-3.8.0 idna-3.7 importlib-metadata-6.7.0 keras-applications-1.0.8 keras-preprocessing-1.1.2 markdown-3.4.4 oauthlib-3.2.2 opt-einsum-3.3.0 protobuf-4.24.4 pyasn1-0.5.1 pyasn1-modules-0.3.0 requests-2.31.0 requests-oauthlib-2.0.0 rsa-4.9 tensorboard-2.0.2 tensorflow-2.0.0 tensorflow-estimator-2.0.1 termcolor-2.3.0 urllib3-2.0.7 werkzeug-2.2.3 wrapt-1.16.0 zipp-3.15.0
Collecting keras==2.3.1
  Using cached Keras-2.3.1-py2.py3-none-any.whl (377 kB)
Requirement already satisfied: keras-preprocessing>=1.0.5 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from keras==2.3.1) (1.1.2)
Requirement already satisfied: keras-applications>=1.0.6 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from keras==2.3.1) (1.0.8)
Collecting pyyaml
  Using cached PyYAML-6.0.1-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (670 kB)
Requirement already satisfied: six>=1.9.0 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from keras==2.3.1) (1.16.0)
Requirement already satisfied: numpy>=1.9.1 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from keras==2.3.1) (1.21.6)
Requirement already satisfied: h5py in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from keras==2.3.1) (3.8.0)
Requirement already satisfied: scipy>=0.14 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from keras==2.3.1) (1.7.3)
Installing collected packages: pyyaml, keras
Successfully installed keras-2.3.1 pyyaml-6.0.1
Collecting h5py==2.10.0
  Using cached h5py-2.10.0-cp37-cp37m-manylinux1_x86_64.whl (2.9 MB)
Requirement already satisfied: numpy>=1.7 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from h5py==2.10.0) (1.21.6)
Requirement already satisfied: six in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from h5py==2.10.0) (1.16.0)
Installing collected packages: h5py
  Attempting uninstall: h5py
    Found existing installation: h5py 3.8.0
    Uninstalling h5py-3.8.0:
      Successfully uninstalled h5py-3.8.0
Successfully installed h5py-2.10.0
Collecting imgaug
  Using cached imgaug-0.4.0-py2.py3-none-any.whl (948 kB)
Requirement already satisfied: six in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from imgaug) (1.16.0)
Requirement already satisfied: scipy in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from imgaug) (1.7.3)
Requirement already satisfied: matplotlib in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from imgaug) (3.5.3)
Requirement already satisfied: scikit-image>=0.14.2 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from imgaug) (0.16.2)
Collecting Shapely
  Using cached shapely-2.0.4-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.4 MB)
Requirement already satisfied: opencv-python in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from imgaug) (4.9.0.80)
Requirement already satisfied: numpy>=1.15 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from imgaug) (1.21.6)
Requirement already satisfied: Pillow in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from imgaug) (9.5.0)
Requirement already satisfied: imageio in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from imgaug) (2.31.2)
Requirement already satisfied: PyWavelets>=0.4.0 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from scikit-image>=0.14.2->imgaug) (1.3.0)
Requirement already satisfied: networkx>=2.0 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from scikit-image>=0.14.2->imgaug) (2.6.3)
Requirement already satisfied: python-dateutil>=2.7 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from matplotlib->imgaug) (2.9.0.post0)
Requirement already satisfied: fonttools>=4.22.0 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from matplotlib->imgaug) (4.38.0)
Requirement already satisfied: cycler>=0.10 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from matplotlib->imgaug) (0.11.0)
Requirement already satisfied: packaging>=20.0 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from matplotlib->imgaug) (24.0)
Requirement already satisfied: pyparsing>=2.2.1 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from matplotlib->imgaug) (3.1.2)
Requirement already satisfied: kiwisolver>=1.0.1 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from matplotlib->imgaug) (1.4.5)
Requirement already satisfied: typing-extensions in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from kiwisolver>=1.0.1->matplotlib->imgaug) (4.7.1)
Installing collected packages: Shapely, imgaug
Successfully installed Shapely-2.0.4 imgaug-0.4.0
Collecting IPython[all]
  Using cached ipython-7.34.0-py3-none-any.whl (793 kB)
Collecting traitlets>=4.2
  Using cached traitlets-5.9.0-py3-none-any.whl (117 kB)
Collecting pexpect>4.3
  Using cached pexpect-4.9.0-py2.py3-none-any.whl (63 kB)
Collecting matplotlib-inline
  Using cached matplotlib_inline-0.1.6-py3-none-any.whl (9.4 kB)
Requirement already satisfied: setuptools>=18.5 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from IPython[all]) (65.6.3)
Collecting jedi>=0.16
  Using cached jedi-0.19.1-py2.py3-none-any.whl (1.6 MB)
Collecting pickleshare
  Using cached pickleshare-0.7.5-py2.py3-none-any.whl (6.9 kB)
Collecting decorator
  Using cached decorator-5.1.1-py3-none-any.whl (9.1 kB)
Collecting pygments
  Using cached pygments-2.17.2-py3-none-any.whl (1.2 MB)
Collecting backcall
  Using cached backcall-0.2.0-py2.py3-none-any.whl (11 kB)
Collecting prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0
  Using cached prompt_toolkit-3.0.43-py3-none-any.whl (386 kB)
Collecting nose>=0.10.1
  Using cached nose-1.3.7-py3-none-any.whl (154 kB)
Collecting qtconsole
  Using cached qtconsole-5.4.4-py3-none-any.whl (121 kB)
Collecting notebook
  Using cached notebook-6.5.6-py3-none-any.whl (529 kB)
Collecting ipyparallel
  Using cached ipyparallel-8.6.1-py3-none-any.whl (298 kB)
Collecting Sphinx>=1.3
  Using cached sphinx-5.3.0-py3-none-any.whl (3.2 MB)
Collecting nbformat
  Using cached nbformat-5.8.0-py3-none-any.whl (77 kB)
Collecting ipywidgets
  Using cached ipywidgets-8.1.2-py3-none-any.whl (139 kB)
Collecting testpath
  Using cached testpath-0.6.0-py3-none-any.whl (83 kB)
Requirement already satisfied: requests in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from IPython[all]) (2.31.0)
Requirement already satisfied: numpy>=1.17 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from IPython[all]) (1.21.6)
Collecting ipykernel
  Using cached ipykernel-6.16.2-py3-none-any.whl (138 kB)
Collecting nbconvert
  Using cached nbconvert-7.6.0-py3-none-any.whl (290 kB)
Collecting parso<0.9.0,>=0.8.3
  Using cached parso-0.8.4-py2.py3-none-any.whl (103 kB)
Collecting ptyprocess>=0.5
  Using cached ptyprocess-0.7.0-py2.py3-none-any.whl (13 kB)
Collecting wcwidth
  Using cached wcwidth-0.2.13-py2.py3-none-any.whl (34 kB)
Collecting docutils<0.20,>=0.14
  Using cached docutils-0.19-py3-none-any.whl (570 kB)
Collecting babel>=2.9
  Using cached Babel-2.14.0-py3-none-any.whl (11.0 MB)
Collecting sphinxcontrib-jsmath
  Using cached sphinxcontrib_jsmath-1.0.1-py2.py3-none-any.whl (5.1 kB)
Collecting imagesize>=1.3
  Using cached imagesize-1.4.1-py2.py3-none-any.whl (8.8 kB)
Collecting sphinxcontrib-applehelp
  Using cached sphinxcontrib_applehelp-1.0.2-py2.py3-none-any.whl (121 kB)
Collecting sphinxcontrib-htmlhelp>=2.0.0
  Using cached sphinxcontrib_htmlhelp-2.0.0-py2.py3-none-any.whl (100 kB)
Collecting alabaster<0.8,>=0.7
  Using cached alabaster-0.7.13-py3-none-any.whl (13 kB)
Requirement already satisfied: importlib-metadata>=4.8 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from Sphinx>=1.3->IPython[all]) (6.7.0)
Collecting sphinxcontrib-qthelp
  Using cached sphinxcontrib_qthelp-1.0.3-py2.py3-none-any.whl (90 kB)
Collecting sphinxcontrib-devhelp
  Using cached sphinxcontrib_devhelp-1.0.2-py2.py3-none-any.whl (84 kB)
Collecting Jinja2>=3.0
  Using cached Jinja2-3.1.3-py3-none-any.whl (133 kB)
Collecting sphinxcontrib-serializinghtml>=1.1.5
  Using cached sphinxcontrib_serializinghtml-1.1.5-py2.py3-none-any.whl (94 kB)
Requirement already satisfied: packaging>=21.0 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from Sphinx>=1.3->IPython[all]) (24.0)
Collecting snowballstemmer>=2.0
  Using cached snowballstemmer-2.2.0-py2.py3-none-any.whl (93 kB)
Requirement already satisfied: urllib3<3,>=1.21.1 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from requests->IPython[all]) (2.0.7)
Requirement already satisfied: charset-normalizer<4,>=2 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from requests->IPython[all]) (3.3.2)
Requirement already satisfied: certifi>=2017.4.17 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from requests->IPython[all]) (2022.12.7)
Requirement already satisfied: idna<4,>=2.5 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from requests->IPython[all]) (3.7)
Collecting pyzmq>=17
  Using cached pyzmq-26.0.2-cp37-cp37m-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (909 kB)
Collecting nest-asyncio
  Using cached nest_asyncio-1.6.0-py3-none-any.whl (5.2 kB)
Collecting debugpy>=1.0
  Using cached debugpy-1.7.0-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.2 MB)
Collecting jupyter-client>=6.1.12
  Using cached jupyter_client-7.4.9-py3-none-any.whl (133 kB)
Collecting psutil
  Using cached psutil-5.9.8-cp36-abi3-manylinux_2_12_x86_64.manylinux2010_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (288 kB)
Collecting tornado>=6.1
  Using cached tornado-6.2-cp37-abi3-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (423 kB)
Collecting entrypoints
  Using cached entrypoints-0.4-py3-none-any.whl (5.3 kB)
Collecting tqdm
  Using cached tqdm-4.66.2-py3-none-any.whl (78 kB)
Requirement already satisfied: python-dateutil>=2.1 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from ipyparallel->IPython[all]) (2.9.0.post0)
Collecting widgetsnbextension~=4.0.10
  Using cached widgetsnbextension-4.0.10-py3-none-any.whl (2.3 MB)
Collecting comm>=0.1.3
  Using cached comm-0.1.4-py3-none-any.whl (6.6 kB)
Collecting jupyterlab-widgets~=3.0.10
  Using cached jupyterlab_widgets-3.0.10-py3-none-any.whl (215 kB)
Requirement already satisfied: markupsafe>=2.0 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from nbconvert->IPython[all]) (2.1.5)
Collecting bleach!=5.0.0
  Using cached bleach-6.0.0-py3-none-any.whl (162 kB)
Collecting jupyterlab-pygments
  Using cached jupyterlab_pygments-0.2.2-py2.py3-none-any.whl (21 kB)
Collecting tinycss2
  Using cached tinycss2-1.2.1-py3-none-any.whl (21 kB)
Collecting defusedxml
  Using cached defusedxml-0.7.1-py2.py3-none-any.whl (25 kB)
Collecting mistune<4,>=2.0.3
  Using cached mistune-3.0.2-py3-none-any.whl (47 kB)
Collecting pandocfilters>=1.4.1
  Using cached pandocfilters-1.5.1-py2.py3-none-any.whl (8.7 kB)
Collecting beautifulsoup4
  Using cached beautifulsoup4-4.12.3-py3-none-any.whl (147 kB)
Collecting jupyter-core>=4.7
  Using cached jupyter_core-4.12.0-py3-none-any.whl (89 kB)
Collecting nbclient>=0.5.0
  Using cached nbclient-0.7.4-py3-none-any.whl (73 kB)
Collecting jsonschema>=2.6
  Using cached jsonschema-4.17.3-py3-none-any.whl (90 kB)
Collecting fastjsonschema
  Using cached fastjsonschema-2.19.1-py3-none-any.whl (23 kB)
Collecting terminado>=0.8.3
  Using cached terminado-0.17.1-py3-none-any.whl (17 kB)
Collecting Send2Trash>=1.8.0
  Using cached Send2Trash-1.8.3-py3-none-any.whl (18 kB)
Collecting argon2-cffi
  Using cached argon2_cffi-23.1.0-py3-none-any.whl (15 kB)
Collecting nbclassic>=0.4.7
  Using cached nbclassic-1.0.0-py3-none-any.whl (10.0 MB)
Collecting pyzmq>=17
  Using cached pyzmq-24.0.1-cp37-cp37m-manylinux_2_5_x86_64.manylinux1_x86_64.whl (1.1 MB)
Collecting ipython-genutils
  Using cached ipython_genutils-0.2.0-py2.py3-none-any.whl (26 kB)
Collecting prometheus-client
  Using cached prometheus_client-0.17.1-py3-none-any.whl (60 kB)
Collecting qtpy>=2.4.0
  Using cached QtPy-2.4.1-py3-none-any.whl (93 kB)
Requirement already satisfied: pytz>=2015.7 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from babel>=2.9->Sphinx>=1.3->IPython[all]) (2024.1)
Collecting webencodings
  Using cached webencodings-0.5.1-py2.py3-none-any.whl (11 kB)
Requirement already satisfied: six>=1.9.0 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from bleach!=5.0.0->nbconvert->IPython[all]) (1.16.0)
Requirement already satisfied: zipp>=0.5 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from importlib-metadata>=4.8->Sphinx>=1.3->IPython[all]) (3.15.0)
Requirement already satisfied: typing-extensions>=3.6.4 in /home/palani-sn/miniconda3/envs/hash_dataset/lib/python3.7/site-packages (from importlib-metadata>=4.8->Sphinx>=1.3->IPython[all]) (4.7.1)
Collecting importlib-resources>=1.4.0
  Using cached importlib_resources-5.12.0-py3-none-any.whl (36 kB)
Collecting pkgutil-resolve-name>=1.3.10
  Using cached pkgutil_resolve_name-1.3.10-py3-none-any.whl (4.7 kB)
Collecting pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0
  Using cached pyrsistent-0.19.3-py3-none-any.whl (57 kB)
Collecting attrs>=17.4.0
  Using cached attrs-23.2.0-py3-none-any.whl (60 kB)
Collecting notebook-shim>=0.2.3
  Using cached notebook_shim-0.2.4-py3-none-any.whl (13 kB)
Collecting jupyter-server>=1.8
  Using cached jupyter_server-1.24.0-py3-none-any.whl (347 kB)
Collecting argon2-cffi-bindings
  Using cached argon2_cffi_bindings-21.2.0-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (86 kB)
Collecting soupsieve>1.2
  Using cached soupsieve-2.4.1-py3-none-any.whl (36 kB)
Collecting websocket-client
  Using cached websocket_client-1.6.1-py3-none-any.whl (56 kB)
Collecting anyio<4,>=3.1.0
  Using cached anyio-3.7.1-py3-none-any.whl (80 kB)
Collecting cffi>=1.0.1
  Using cached cffi-1.15.1-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (427 kB)
Collecting exceptiongroup
  Using cached exceptiongroup-1.2.1-py3-none-any.whl (16 kB)
Collecting sniffio>=1.1
  Using cached sniffio-1.3.1-py3-none-any.whl (10 kB)
Collecting pycparser
  Using cached pycparser-2.21-py2.py3-none-any.whl (118 kB)
Installing collected packages: webencodings, wcwidth, snowballstemmer, ptyprocess, pickleshare, nose, ipython-genutils, fastjsonschema, backcall, widgetsnbextension, websocket-client, traitlets, tqdm, tornado, tinycss2, testpath, sphinxcontrib-serializinghtml, sphinxcontrib-qthelp, sphinxcontrib-jsmath, sphinxcontrib-htmlhelp, sphinxcontrib-devhelp, sphinxcontrib-applehelp, soupsieve, sniffio, Send2Trash, qtpy, pyzmq, pyrsistent, pygments, pycparser, psutil, prompt-toolkit, prometheus-client, pkgutil-resolve-name, pexpect, parso, pandocfilters, nest-asyncio, mistune, jupyterlab-widgets, jupyterlab-pygments, Jinja2, importlib-resources, imagesize, exceptiongroup, entrypoints, docutils, defusedxml, decorator, debugpy, bleach, babel, alabaster, terminado, Sphinx, matplotlib-inline, jupyter-core, jedi, comm, cffi, beautifulsoup4, attrs, anyio, jupyter-client, jsonschema, IPython, argon2-cffi-bindings, nbformat, ipywidgets, ipykernel, argon2-cffi, qtconsole, nbclient, ipyparallel, nbconvert, jupyter-server, notebook-shim, nbclassic, notebook
Successfully installed IPython-7.34.0 Jinja2-3.1.3 Send2Trash-1.8.3 Sphinx-5.3.0 alabaster-0.7.13 anyio-3.7.1 argon2-cffi-23.1.0 argon2-cffi-bindings-21.2.0 attrs-23.2.0 babel-2.14.0 backcall-0.2.0 beautifulsoup4-4.12.3 bleach-6.0.0 cffi-1.15.1 comm-0.1.4 debugpy-1.7.0 decorator-5.1.1 defusedxml-0.7.1 docutils-0.19 entrypoints-0.4 exceptiongroup-1.2.1 fastjsonschema-2.19.1 imagesize-1.4.1 importlib-resources-5.12.0 ipykernel-6.16.2 ipyparallel-8.6.1 ipython-genutils-0.2.0 ipywidgets-8.1.2 jedi-0.19.1 jsonschema-4.17.3 jupyter-client-7.4.9 jupyter-core-4.12.0 jupyter-server-1.24.0 jupyterlab-pygments-0.2.2 jupyterlab-widgets-3.0.10 matplotlib-inline-0.1.6 mistune-3.0.2 nbclassic-1.0.0 nbclient-0.7.4 nbconvert-7.6.0 nbformat-5.8.0 nest-asyncio-1.6.0 nose-1.3.7 notebook-6.5.6 notebook-shim-0.2.4 pandocfilters-1.5.1 parso-0.8.4 pexpect-4.9.0 pickleshare-0.7.5 pkgutil-resolve-name-1.3.10 prometheus-client-0.17.1 prompt-toolkit-3.0.43 psutil-5.9.8 ptyprocess-0.7.0 pycparser-2.21 pygments-2.17.2 pyrsistent-0.19.3 pyzmq-24.0.1 qtconsole-5.4.4 qtpy-2.4.1 sniffio-1.3.1 snowballstemmer-2.2.0 soupsieve-2.4.1 sphinxcontrib-applehelp-1.0.2 sphinxcontrib-devhelp-1.0.2 sphinxcontrib-htmlhelp-2.0.0 sphinxcontrib-jsmath-1.0.1 sphinxcontrib-qthelp-1.0.3 sphinxcontrib-serializinghtml-1.1.5 terminado-0.17.1 testpath-0.6.0 tinycss2-1.2.1 tornado-6.2 tqdm-4.66.2 traitlets-5.9.0 wcwidth-0.2.13 webencodings-0.5.1 websocket-client-1.6.1 widgetsnbextension-4.0.10
Collecting protobuf==3.20.1
  Using cached protobuf-3.20.1-cp37-cp37m-manylinux_2_5_x86_64.manylinux1_x86_64.whl (1.0 MB)
Installing collected packages: protobuf
  Attempting uninstall: protobuf
    Found existing installation: protobuf 4.24.4
    Uninstalling protobuf-4.24.4:
      Successfully uninstalled protobuf-4.24.4
Successfully installed protobuf-3.20.1

```

- Activate the environment & check the environment setup using **python test_cocomodel.py**

```
output

palani-sn@DESKTOP-EJPA9NB:/mnt/d/GitRepos/ML_PoC$ conda activate hash_dataset
(hash_dataset) palani-sn@DESKTOP-EJPA9NB:/mnt/d/GitRepos/ML_PoC$ python test_cocomodel.py
Using TensorFlow backend.
2024-04-27 14:08:11.860451: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
2024-04-27 14:08:11.865583: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 2995200000 Hz
2024-04-27 14:08:11.868317: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x55fb6e633e80 executing computations on platform Host. Devices:
2024-04-27 14:08:11.868348: I tensorflow/compiler/xla/service/service.cc:175]   StreamExecutor device (0): Host, Default Version

```

- Output Image will pop up with segmentation maasks applied as per pre-trained weights.

![](https://github.com/Palani-SN/ML_PoC/blob/main/output.png?raw=true)