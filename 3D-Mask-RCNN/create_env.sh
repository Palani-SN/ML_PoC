# conda create env
conda create -n dot_dataset python=3.7.3
# conda activate env
conda activate dot_dataset
# conda install libs for hash_dataset generation
python -m pip install pydenticon
python -m pip install opencv-python
python -m pip install pandas
python -m pip install numpy
python -m pip install scipy
python -m pip install Pillow
python -m pip install cython
python -m pip install matplotlib
python -m pip install scikit-image==0.16.2
python -m pip install tensorflow==2.0.0
python -m pip install keras==2.3.1
python -m pip install h5py==2.10.0
python -m pip install imgaug
python -m pip install IPython[all]
python -m pip install protobuf==3.20.1
python -m pip install tifffile
# conda deactivate env
conda deactivate