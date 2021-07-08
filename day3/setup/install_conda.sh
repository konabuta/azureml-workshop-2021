#!/bin/bash
echo "conda env name : "
read envname

echo "yml filename : "
read filename

#envname="flaml_env"
conda env create -n $envname --file ../environments/$filename
/anaconda/envs/$envname/bin/python -m ipykernel install --user --name $envname --display-name $envname
