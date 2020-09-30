#!/usr/bin/env bash

# download data from kaggle
kaggle datasets download -d ruiqurm/lianjia -p price_prediction_model/data/
# unzip data archive
unzip price_prediction_model/data/lianjia.zip -d price_prediction_model/data/
# delete zip file
rm price_prediction_model/data/lianjia.zip
# rename file
mv -v price_prediction_model/data/new.csv price_prediction_model/data/beijing_house_prices_2012_2017.csv
# generate test set
python price_prediction_model/utils/generate_test_dataset.py

