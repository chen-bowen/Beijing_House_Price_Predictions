#!/usr/bin/env bash

# download data from kaggle
kaggle datasets download -d ruiqurm/lianjia -p beijing_house_price_predictions/data/
# unzip data archive
unzip beijing_house_price_predictions/data/lianjia.zip -d beijing_house_price_predictions/data/
# delete zip file
rm beijing_house_price_predictions/data/lianjia.zip
# rename file
mv -v beijing_house_price_predictions/data/new.csv beijing_house_price_predictions/data/beijing_house_prices_2012_2017.csv


