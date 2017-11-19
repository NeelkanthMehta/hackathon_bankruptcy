#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 06:33:16 2017

@author: neelkanthmehta
"""
import pandas as pd
from scipy.io.arff import loadarff

attrs = pd.read_csv('Attributes.csv',index_col=0).to_dict()
attrs
df = loadarff('1year.arff')
yr1 = pd.DataFrame(df[0])
yr1.columns = attrs.values()