# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 02:18:37 2025

@author: Sumeyye
"""




import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.cbook import boxplot_stats
import random
from random import sample 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler


# VERI OKUMA
nitelikAdlari = ["mpg", 	"cylinders", 	"displacement", 	"horsepower", 	"weight", 	"acceleration", 	"model_year", 	"origin", 	"car_name"]

veriSeti = pd.read_csv("auto-mpg.data", sep = "\s+", header = None, names = nitelikAdlari, decimal=".")


veriSeti.dtypes

veriSeti.loc[veriSeti.horsepower=="?","horsepower"]=np.nan # ? işareti olanlara nan değer atandı
veriSeti.horsepower=veriSeti.horsepower.astype("float64")

print(veriSeti.isnull().sum())

veriSeti["horsepower"].fillna(veriSeti["horsepower"].mean().round(0), inplace = True) # horsepower'daki nan değerlere diğer bütün değerlerin ortalamasını atadık.

"""
#VERİ AYIKLAMA
veriSeti["durum"]=veriSeti.mpg.map(lambda x:"Düşük" if x<23.5 else "Orta" if(x>=23.5 and x<30) else "Yüksek").astype("category")

veriSeti.durum.value_counts()


bolmeKategorileri=["Düşük","Orta","Yüksek"]
bolmeler=[8,23.4,29.9,46.6]
veriSeti["durum"] = pd.cut(veriSeti["mpg"], bins=bolmeler,labels=bolmeKategorileri)
veriSeti.durum.value_counts()

# Eşit frekan Her aralıkta yaklaşık eşit sayıda örneğin yer almasına odaklanılır.
durum_ef = pd.qcut(veriSeti["mpg"], q=3)
durum_ef.value_counts()


# Eşit Aralık her aralığın boyunun eşit olması sağlanır
durum_ef = pd.cut(veriSeti["mpg"], bins=3)
durum_ef.value_counts()

"""



































































