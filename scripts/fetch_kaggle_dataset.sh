#!/usr/bin/env bash

# download data from kaggle
kaggle datasets download -d ruiqurm/lianjia -p price_prediction_moddel/data/
# unzip data archive
unzip price_prediction_moddel/data/lianjia.zip -d price_prediction_moddel/data/
# delete zip file
rm price_prediction_moddel/data/lianjia.zip
# rename file
mv -v price_prediction_moddel/data/new.csv price_prediction_moddel/data/beijing_house_prices_2012_2017.csv


