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


pd.set_option("display.max_columns", 20)
veriSeti.describe(include="all") # tum niteliklerin ozet bilgisi

x=range(1,51)
y=veriSeti.iloc[0:50,2]
plt.plot(x,y,"u:r")



## CIZGI GRAFIGI (Line Plot)
# Ornek - 1: Ilk 35 musterinin yasi
x=range(1,36)
y=veriSeti.iloc[0:35,0] # tablodaki ilk sütundaki(yas) 0-35 arasındaki satırları alır 
plt.plot(x,y,"o:r") #  "or" kirmizi yuvarlaklar
plt.xlabel("Müşteri No")  
plt.ylabel("Yaş")  
plt.title("İlk 35 Müşterinin Yaşı")  

plt.plot(x,y,"^k:")#  "^k:" bibirine noktalar ile baglanmis siyah ucgen işaretleyiciler

plt.plot(x,y,linestyle="dashed",color="purple",linewidth="5")

# Ornek - 2: İlk ve ikinci 20'de yer alan musterilerin VKI karsilastirmasi
x1= np.arange(1,21)
y1=veriSeti.iloc[0:20,2]
y2=veriSeti.iloc[20:40,2]
plt.xticks(x1)
plt.plot(x1,y1,x1,y2)

# grid stili belirleme
x=np.arange(1,51)
y=veriSeti.iloc[0:50,0] # tablodaki ilk sütundaki(yas) 0-35 arasındaki satırları alır 
plt.plot(x,y,"o:r") #  "or" kirmizi yuvarlaklar
plt.xlabel("Müşteri No")  
plt.ylabel("Yaş")  
plt.title("İlk 50 Müşterinin Yaşı")  
plt.grid(color = "red", linestyle = '--', linewidth = 0.5)

# ALT GRAFIKLER
# plot 1: Ilk 20 musterinin vki'si
x = np.arange(1,21)
y1 = veriSeti.iloc[0:20,2]

plt.subplot(2, 1, 1)
plt.plot(x,y1)
plt.xticks(x)
plt.title("İlk 20 Müşteri") # Ilk grafik basligi

#plot 2: Ikinci 20 musterinin vki'si
y2 = veriSeti.iloc[20:40,2]

plt.subplot(2, 1, 2)
plt.plot(x,y2)
plt.xticks(x)

plt.title("İkinci 20 Müşteri") # Ikinci grafigin basligi

plt.suptitle("VKİ KARŞILAŞTIRMASI") # Tum grafigin basligi
plt.tight_layout(pad=1) # Iki grafik arasindaki bosluk

## SUTUN GRAFIGI (Bar Plot)
# Musterilerin sigortaya odeme miktarlarinin sigara icme durumlarina gore ortalamasini bulma

def etiketEkle(x,y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha = "center")

ozet=veriSeti.groupby("sigaraDurum")["odemeMiktari"].mean()

plt.bar(x=ozet.index, height=ozet.values, color="purple")
plt.xlabel("Sigara İçme Durumu")  
plt.ylabel("Ödeme Miktarı") 
etiketEkle(ozet.index, ozet.values.round(2))

# Ornek - 2: Grafigin yatay hali
plt.barh(y=ozet.index, width=ozet.values, color="b")

# Ornek - 3
plt.bar(x=ozet.index, height=ozet.values, color="r", width = 0.95)

# Ornek - 4
plt.barh(y=ozet.index, width=ozet.values, color="b", height=0.2)

## PASTA GRAFIGI (Pie Chart)
ozet = veriSeti.groupby("bolge")["odemeMiktari"].sum()

etiketler=ozet.index
degerler=ozet.values
renkler=sns.color_palette("viridis",4)
secim=(0.2,0,0,0)

plt.pie(degerler,explode=secim,labels=etiketler, autopct="%%%4.1f", shadow=True, startangle=360, colors=renkler)



## SERPILME/SACILIM DIYAGRAMI (Scatter Plot)

# Ornek - 1: Serpilme diyagrami
x = veriSeti.yas
y = veriSeti.vki
plt.scatter(x, y)
plt.xlabel("Yaş")
plt.ylabel("Vücut Kitle İndeksi")

ozet = veriSeti.groupby("yas")["odemeMiktari"].mean()

plt.scatter(ozet.index, ozet.values)
plt.xlabel("Yaş")
plt.ylabel("Odeme Miktarı")


secim = [1072,548, 1032, 437, 154, 653, 645, 862, 25, 603]
altkume = veriSeti.iloc[secim,[0,6]] # 0 = yas sütununa denk geliyor 6 = ödeme miktarı sütununa 
x = altkume.yas
y = altkume.odemeMiktari
plt.scatter(x, y)
plt.xlabel("Yaş")
plt.ylabel("Ödeme Miktarı")
