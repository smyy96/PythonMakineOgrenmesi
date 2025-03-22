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

