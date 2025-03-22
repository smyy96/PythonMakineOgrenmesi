# Makine Öğrenimi  

Python programlama dili ve **Spyder IDE** kullanılmıştır.  
Temel ve ileri düzey veri görselleştirme yöntemleri için <span style="color:red">**Matplotlib**</span> ve <span style="color:red">**Seaborn**</span> kütüphaneleri kullanılmıştır.  
Analizler sırasında <span style="color:red">**NumPy**</span> ve <span style="color:red">**Pandas**</span> kütüphanelerinden faydalanılmıştır.  

## 3. Python ile Veri Görselleştirme  

### Uygulamaya Kütüphaneleri Dahil Etme  

```python
# Gerekli kütüphanelerin içe aktarılması
import numpy as np         # Sayısal işlemler için
import pandas as pd        # Veri analizi ve işleme için
import matplotlib.pyplot as plt  # Grafik çizimi için
import seaborn as sns      # Gelişmiş veri görselleştirme için
```


### 📌 Çizgi Grafiği (Line Plot)  

#### **Örnek - 1: İlk 35 müşterinin yaşı**  

```python
# İlk 35 müşterinin yaş verisini çizdirme
x = range(1, 36)
y = veriSeti.iloc[0:35, 0]

plt.plot(x, y, "o:r")  # Noktalı ve kırmızı renkte çizgi grafiği
plt.xlabel("Müşteri No")  
plt.ylabel("Yaş")  
plt.title("İlk 35 Müşterinin Yaşı")  
plt.show()
```
<img src="https://github.com/user-attachments/assets/9c08b507-2e92-4774-a93b-12284d5ec4b4" width="400">



#### **Örnek - 2: İlk ve ikinci 20'de yer alan musterilerin VKI karsilastirmasi**
```python
x1= np.arange(1,21)
y1=veriSeti.iloc[0:20,2]
y2=veriSeti.iloc[20:40,2]
plt.xticks(x1)
plt.plot(x1,y1,x1,y2)
```
<img src="https://github.com/user-attachments/assets/fb3e27a0-5ce2-40a6-956c-e63afd641243" width="400">

### 📌 Sütun Grafiği (Line Plot)  

#### **Örnek - 1: Musterilerin sigortaya odeme miktarlarinin sigara icme durumlarina gore ortalamasini bulma**  

```python
ozet=veriSeti.groupby("sigaraDurum")["odemeMiktari"].mean()

plt.bar(x=ozet.index, height=ozet.values, color="purple")
plt.xlabel("Sigara İçme Durumu")  
plt.ylabel("Ödeme Miktarı") 

```
<img src="https://github.com/user-attachments/assets/1c97930b-d958-4b3c-8fcf-7b7abd17412f" width="400">


### 📌 Pasta Grafiği (Line Plot)  

#### **Örnek - 1: Sigortaya yapılan toplam ödeme miktarının bölgeler arasında yüzdesel dağılımı**  

```python
ozet = veriSeti.groupby("bolge")["odemeMiktari"].sum()

etiketler=ozet.index
degerler=ozet.values
renkler=sns.color_palette("viridis",4)
secim=(0.2,0,0,0)

plt.pie(degerler,explode=secim,labels=etiketler, autopct="%%%4.1f", shadow=True, startangle=360, colors=renkler)

```
<img src="https://github.com/user-attachments/assets/8c511612-5c75-444a-97ba-ac57aec9f6aa" width="400">






































