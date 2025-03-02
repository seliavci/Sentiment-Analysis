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


Veri Toplama Yöntemi:

Bu proje, Reddit'teki "oscars 2025" konusuyla ilgili gönderileri çekerek sentiment analizi yapmaktadır.

Veri çekme adımları:

Reddit API kullanıldı: praw kütüphanesi ile Reddit'e bağlanıldı.

Arama terimi olarak "oscars 2025" seçildi: reddit.subreddit('all').search("oscars 2025", limit=1500) ile tüm subreddit’lerde bu terimle ilgili gönderiler çekildi.

Başlık ve içerik birleştirildi: submission.title + " " + submission.selftext

Boş içerikler filtrelendi: Yalnızca dolu metinler analiz için kullanıldı.


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


Lisans

Bu proje MIT Lisansı ile lisanslanmıştır.


















