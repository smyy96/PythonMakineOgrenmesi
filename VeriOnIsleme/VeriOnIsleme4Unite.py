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


# VERI OZETLEME
pd.set_option("display.max_columns", 20)
veriSeti.describe(include="all") # tum niteliklerin ozet bilgisi



# GRUPLANDIRMA (Aggregate)

# Farkli foksiyonlar ile denemeler
veriSeti.groupby("durum")["mpg"].mean()
veriSeti[["mpg", "durum"]].groupby("durum").mean()


veriSeti.groupby("durum")["mpg"].sum()
veriSeti.groupby("durum")["mpg"].count()
veriSeti.groupby("durum")["mpg"].mean()
veriSeti.groupby("durum")["mpg"].std()
veriSeti[["mpg", "durum"]].groupby("durum").min()
veriSeti[["mpg", "durum"]].groupby("durum").max()
veriSeti[["mpg", "durum"]].groupby("durum").describe()


# TEKRAR EDEN SATIRLARIN BULUNMASI (duplicated rows)
tekrarlar_f = veriSeti.duplicated(keep="first")
tekrarlar_l = veriSeti.duplicated(keep="last")



# Tekrar eden tum gozlemleri gorebilmek icin
indislerim = tekrarlar_f | tekrarlar_l
veriSeti[indislerim]



# Veri setinden tekrar eden degerleri kaldirma
veriSeti2 = veriSeti.drop_duplicates()



# IQR
q1 = veriSeti["horsepower"].quantile(0.25)
q3 = veriSeti["horsepower"].quantile(0.75)
IQR = q3 - q1
alt = q1 - 1.5*IQR
ust = q3 + 1.5*IQR

ust_aykiriDegerInd = np.where(veriSeti["horsepower"]>=ust)[0]
alt_aykiriDegerInd = np.where(veriSeti["horsepower"]<=alt)[0]


sns.boxplot(y=veriSeti["horsepower"],data=veriSeti,palette="magma")


veriSeti.drop(index=ust_aykiriDegerInd, inplace=True)
veriSeti.drop(index=alt_aykiriDegerInd, inplace=True)




# II.yol
boxplot_stats(veriSeti.horsepower)
aykiriDegerler = boxplot_stats(veriSeti.horsepower).pop(0)["fliers"]
aykiriDegerIndeksleri = veriSeti.index[veriSeti.horsepower.isin(aykiriDegerler) == True]
veriSeti = veriSeti.drop(aykiriDegerIndeksleri, axis=0)


# ORNEKLEME (Sampling)
listem = list(np.arange(1,21))

sample(listem, 10) # Kod 1. kez calistiriliyor
sample(listem, 10) # Kod 2. kez calistiriliyor

listem = list(np.arange(1,21))

random.seed(123)
sample(listem, 10) # Kod 3. kez calistiriliyor
random.seed(123)
sample(listem, 10) # Kod 4. kez calistiriliyor

random.seed(5)
sample(listem, 10)
random.seed(5)
sample(listem, 10)


# yerine koyarak secim
random.choices(listem, k = 10) 


egitim = veriSeti.sample(frac=0.7, replace=False, random_state=1)
ind = veriSeti.index.isin(egitim.index)

test=veriSeti[~ind]




# Tabakalı Örnekleme (stratified sampling)
egitim1, test1 = train_test_split(veriSeti, train_size = 0.7, stratify = veriSeti["durum"], random_state=1)

veriSeti.durum.value_counts()
egitim1.durum.value_counts()
test1.durum.value_counts()


# YAPAY KODLAMA (DUMMY CODING)
veriSeti["durum_s1"] = veriSeti["durum"].cat.codes 
veriSeti.durum.value_counts()
veriSeti.durum_s1.value_counts()

durum_s2 = pd.get_dummies(veriSeti.durum, columns = ["durum"], dtype=int)
veriSeti = pd.concat([veriSeti, durum_s2], axis=1) 



# VERI NORMALIZASYONU (Data Normalization)
# min-max normalizasyon yontemi
veri = veriSeti.iloc[:,0:8]
scaler = MinMaxScaler()
scaler.fit(veri)
n_veriSeti = scaler.transform(veri)
n_veriSeti = pd.DataFrame(n_veriSeti, columns = veri.columns)

# standardizasyon (z-score)
stScaler = StandardScaler()
s_veriSeti = stScaler.fit_transform(veri)
s_veriSeti = pd.DataFrame(s_veriSeti, columns = veri.columns) 


































