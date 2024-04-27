:: conda create env
conda create -n hash_dataset python=3.7.3
:: conda activate env
conda activate hash_dataset
:: conda install libs for hash_dataset generation
python -m pip install pydenticon
python -m pip install opencv-python
python -m pip install pandas
:: conda deactivate env
conda deactivate