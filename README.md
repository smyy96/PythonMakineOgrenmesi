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
![Çizgi Grafiği](https://github.com/user-attachments/assets/9c08b507-2e92-4774-a93b-12284d5ec4b4)

