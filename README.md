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

### 📌 Serpilme Grafiği (Scatter Plot)  

#### **Örnek - 1: Müşterilerin yaşlarına göre vücut kitle indekslerinin verildiği serpilme diyagramı.**  

```python
x=veriSeti.yas
y=veriSeti.vki

plt.scatter(x, y)
plt.xlabel("Yaş")
plt.ylabel("Vücut Kitle İndeksi")

```
<img src="https://github.com/user-attachments/assets/11a77120-6624-4a74-a881-2eeaae9f990c" width="400">

#### **Örnek - 2: Sigortaya yapılan ödemenin yaşa göre incelendiği serpilme diyagramına vücut kitle indeksi niteliği üçüncü boyut olarak eklenirse.**  

```python
fig = plt.figure(figsize=(10, 6))
ax = plt.axes(projection ="3d")
ax.scatter(veriSeti.yas, veriSeti.odemeMiktari, veriSeti.vki, color="darkblue")
ax.set_xlabel("Yaş")
ax.set_ylabel("Ödeme Miktarı")
ax.set_zlabel("Vücut Kitle İndeksi", rotation=90)
ax.zaxis.labelpad=-0.7
plt.title("3-Boyutlu Serpilme Diyagramı")

```
<img src="https://github.com/user-attachments/assets/4a11fe8e-3be0-4c78-a11f-cd866686dd04" width="400">



### 📌 Histogram 

#### **Örnek - 1: Müşterilerin vücut kitle indeksleri**  

```python
sns.histplot(data=veriSeti,x="vki", color="hotpink")
sns.histplot(data=veriSeti,y="vki", color="lightgreen")

```
<img src="https://github.com/user-attachments/assets/ce16e21f-02dd-4878-b00f-bc111968dd64" width="200">
<img src="https://github.com/user-attachments/assets/46f3f468-1ec8-4295-8891-1409b2ea9e28" width="200">



### 📌 KUTU GRAFIGI (Box Plot) 

#### **Örnek - 1: Müşterilerin vücut kitle indeksleri**  

```python
# Tek bir degiskenin kutu grafigi
veriSeti["vki"].describe().round(2)
bp = plt.boxplot(veriSeti["vki"], 
                 vert=True, # Grafigin yonu
                 showmeans=True, # Ortalamanin gosterim secenegi
                 meanline=True, # Ortalamanin cizgisinin gosterim secenegi
                 labels=('x'), # etiket
                 patch_artist=True, # renk doldurulmasi
                 medianprops={'linewidth': 2, 'color': 'yellow'}, # orta deger cizgisi ozellikleri
                 meanprops={'linewidth': 2, 'color': 'red'}, # ortalama cizgisi ozellikleri
                 notch=True) # centik ekleme
plt.ylabel("Sigortaya Odenen Miktar")
plt.legend([bp['medians'][0], bp['means'][0]], ['median', 'mean'])

```
<img src="https://github.com/user-attachments/assets/03614f77-c9da-4dbb-a151-cf62893fd2d2" width="400">


#### **Örnek - 2: Müşterilerin sigara içip içmeme durumlarına göre sigortaya ödedikleri miktarlar karşılaştırılmıştır**  

```python
sns.boxplot(y="sigaraDurum", 
            x="odemeMiktari", 
            data=veriSeti, 
            palette="rainbow")


```
<img src="https://github.com/user-attachments/assets/77b54b02-27d3-4d4a-847b-9b18decfea55" width="400">



### 📌 Violin Grafiği

#### **Örnek - 1: Müşterilerin vücut kitle indeksleri**  

```python
sns.violinplot(y="sigaraDurum", 
               x="odemeMiktari", 
               data=veriSeti, 
               palette="coolwarm")

```
<img src="https://github.com/user-attachments/assets/0276ba7f-1701-4673-b6bd-cd5d524e2544" width="400">


### 📌 Isı Haritası

#### **Örnek - 1: Müşterilerin vücut kitle indeksleri**  

```python
korelasyon = veriSeti[["yas", "vki", "cocukSayisi", "odemeMiktari"]].corr()
sns.heatmap(
    korelasyon, 
    annot = True, # Korelasyon degerlerinin grafigin uzerine yazdirma
    square=True, # Kutularin kare bicimde gosterilmesi
    cmap="Reds" # Renklendirme secenegi
)

```
<img src="https://github.com/user-attachments/assets/17aaf930-ffe0-42ad-86a9-eab0d0a5f1b9" width="400">































