Sentiment Analysis – Oscars 2025

Bu proje, Reddit platformundan Oscars 2025 hashtag’i ile toplanan veriler kullanılarak yapılan bir duygu analizi (sentiment analysis) çalışmasını içermektedir. 
Python ile gerçekleştirilmiş olup, analiz sonuçları histogram grafikleri ile görselleştirilmiştir.


Projenin Amacı:

Bu çalışmanın amacı, Oscars 2025 hakkında yapılan yorumların genel duygu durumunu analiz etmek ve bunları pozitif, negatif ve nötr olarak sınıflandırmaktır. 
Duygu analizi, metin verilerindeki duygusal tonu belirlemek için kullanılır ve sosyal medya gibi platformlarda geniş uygulama alanına sahiptir.


Kullanılan Teknolojiler & Kütüphaneler:

Proje, Python programlama dili ile geliştirilmiştir. Aşağıdaki kütüphaneler kullanılmıştır:

PRAW → Reddit API’si ile veri çekmek için
TextBlob veya VADER → Metinlerin duygu analizini yapmak için
Matplotlib & Seaborn → Verileri görselleştirmek için
Pandas & NumPy → Veri işleme ve analiz için


Dosya Yapısı:

Sentiment-Analysis  
 ┣ sentiment_analysis.py   # Sentiment analizi kodu  
 ┣ requirements.txt        # Gerekli kütüphaneler listesi  
 ┣ README.md               # Proje açıklaması  
 ┣ data/                   # İşlenen verilerin saklandığı klasör  
 ┣ images/                 # Grafik ve görseller  
 ┗ results/                # Çıktılar ve analiz sonuçları  


Analiz Sonuçları:

Histogram grafikleri ile duygu skorlarının dağılımı görselleştirilmiştir.
Çoğu yorum nötr (0.0) duygu skoruna sahiptir.
Pozitif ve negatif yorumlar dengeli şekilde dağılmıştır.

Örnek grafik:
![Sentiment Distribution](images/sentiment_distribution.png)



Lisans

Bu proje MIT Lisansı ile lisanslanmıştır.


















