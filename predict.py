# -*- coding: utf-8 -*-
__author__ = 'luoqm6'
__date__ = '18-1-26 17:38 p.m'

import argparse
from engine.model_engine import ModelEngine
from galaxy.indicator_galaxy import IndicatorGalaxy
from fastresearchdata.fast_research_data import FastResearchData

if __name__ == "__main__":

    # argparse from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", 
                        "--stockID", 
                        type=str, 
                        default="000001", 
                        help="the directory of the .csv file.")
    parser.add_argument("-p", 
                        "--path", 
                        type=str, 
                        default="D:/code/python_code/project2_in_quant/data/1day/000001.csv", 
                        help="the directory of the .csv file.")
    parser.add_argument("-m",
                       "--model_name", 
                        type=str,
                        default='Linearregression', 
                        help="the model used to do the predict Linearregression, NuetrualNetwork, SVM, KNN, RNN supported.")
    parser.add_argument("-add", 
                        "--col_name", 
                        type=str, 
                        default='p_change', 
                        help="add some indicator according to the column in csv such as p_change.")
    parser.add_argument("-targ", 
                        "--target", 
                        type=str, 
                        default='p_change',  
                        help="the target column you want to predict such as p_change.")
    args = parser.parse_args()

    stockIDList = []
    stockIDList.append(args.stockID)

    fileNamesList = []
    fileNamesList.append(args.path)

    # read the csv to dataframe
    frdata = FastResearchData()
    frdata.loadFromCSV(stockIDList,fileNamesList)


    # 
    indtr = IndicatorGalaxy()
    indtr.loadDataframe(frdata.getDataFrame(stockIDList[0]))

    # add some indicator
    indtr.addColMean(args.col_name)
    indtr.addEMA(args.col_name)
    indtr.addDIF(args.col_name)
    indtr.addMACD(args.col_name)
    
    # build the model and predict
    pre = ModelEngine(indtr.getDtframe())

    # print(pre.get_xattri_array)
    pre.setDuration(10)
    pre.setYLabelArray(args.target)
    pre.setXAttriArray(pre.colHead)
    
    result = pre.predictFit(pre.getXAttriArray(), pre.getYLabelArray(), pre.getXPreArray(), args.model_name)
    pre.plotPredict()
    pre.compareModel()

    # #read the csv to dataframe
    # indtr = IndicatorGalaxy()
    # indtr.load_CSV("D:/code/python_code/project2_in_quant/1day/000001.csv")

    # # add some indicator
    # indtr.add_col_mean('p_change')
    # indtr.add_EMA('p_change')
    # indtr.add_DIF('p_change')
    # indtr.add_MACD('p_change')
    # indtr.add_col_mean('volume')
    # indtr.add_EMA('volume')
    # indtr.add_DIF('volume')
    # indtr.add_MACD('volume')
    
    # # build the model and predict
    # pre = ModelEngine(indtr.get_dtframe())

    # # print(pre.get_xattri_array)
    # pre.set_duration(10)
    # pre.set_ylabel_array('close')
    # pre.setXAttriArray(pre.colHead)
    
    # result = pre.predict_fit('Linearregression')
    # pre.plot_predict()
    # pre.compare_model()
    
    
    
    
