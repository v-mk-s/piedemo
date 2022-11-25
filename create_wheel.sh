#!/usr/bin/env bash

rm -rf package_data
mkdir package_data
cp -r ./piedemo ./package_data/
if [[ $1 -eq "--cython" ]]
    then
        cp ./setup_with_cython.py ./package_data/setup.py
    else
        cp ./setup.py ./package_data/
fi
cp ./MANIFEST.in ./package_data/
cp ./requirements.txt ./package_data/
cp ./README.md ./package_data/

cd package_data && python setup.py build_ext --inplace && python setup.py bdist_wheel
cp ./dist/*.whl ../
rm -rf package_data
