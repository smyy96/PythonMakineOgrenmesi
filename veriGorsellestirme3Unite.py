import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# pandas kutuphanesi ile bilgisayardaki csv dosyasindan veri seti okuma
veriSeti = pd.read_csv("insurance.csv")
veriSeti = veriSeti.rename(columns={"age": "yas", "sex": "cinsiyet", "bmi": "vki", "children": "cocukSayisi", "smoker": "sigaraDurum", "region": "bolge", "charges": "odemeMiktari"})

# Kategorik degiskenlerin veri tipinin category yapilmasi
veriSeti.dtypes
veriSeti["cinsiyet"] = veriSeti["cinsiyet"].astype("category")
veriSeti["sigaraDurum"] = veriSeti["sigaraDurum"].astype("category")
veriSeti["bolge"] = veriSeti["bolge"].astype("category")
veriSeti.dtypes

# Kategorik veri tipinde olan Turkcelestirilmesi
veriSeti["cinsiyet"]=veriSeti["cinsiyet"].replace(["male","female"], ["erkek","kadın"])
veriSeti["sigaraDurum"] = veriSeti["sigaraDurum"].replace(["no","yes"],["hayır","evet"])
veriSeti["bolge"]=veriSeti["bolge"].replace(["southeast","northwest","southwest","northeast"],["guneydogu","kuzeybati","guneybati","kuzeydogu"])

# Verisetinin ozet bilgisi
veriSeti.describe() # yalnizca sayisal niteliklerin ozet bilgisi

# Verisetinin ozet bilgisi
pd.set_option("display.max_columns",20)
veriSeti.describe(include="all") # tum niteliklerin ozet bilgisi


x=range(1,51)
y=veriSeti.iloc[0:50,2]
plt.plot(x,y,"u:r")