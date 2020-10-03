#!/usr/bin/env bash

# download data from kaggle
kaggle datasets download -d ruiqurm/lianjia -p price_prediction_model/data/
# unzip data archive
unzip data/lianjia.zip -d data/
# delete zip file
rm data/lianjia.zip
# rename file
mv -v data/new.csv data/beijing_house_prices_2012_2017.csv

