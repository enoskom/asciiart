# asciiart
ascii art generation
ASCII Sanatı ve Görseller

Bu proje, çeşitli şekillerde ASCII sanatı oluşturmayı sağlayan bir Python uygulamasıdır. Kullanıcılar, metinleri veya fotoğrafları ASCII sanatına dönüştürebilir. Ayrıca, önceden kaydedilmiş ASCII şekilleri de görüntüleyebilirsiniz.
Özellikler

    Fotoğrafı ASCII Sanatına Dönüştürme
    Kullanıcı, bir görseli yükleyerek bu görseli ASCII karakterleriyle temsil edilen bir sanat eserine dönüştürebilir.

    Metni ASCII Sanatına Dönüştürme
    Kullanıcı, istediği metni seçilen bir fontla ASCII sanatı olarak görselleştirebilir. Ayrıca metnin boyutu da ayarlanabilir.

    Önceden Tanımlanmış Şekillerin Görüntülenmesi
    Kullanıcılar, dosyadan yüklenen ASCII şekillerini görüntüleyebilirler. Mevcut şekiller arasında kare, yuvarlak, telefon, kalp gibi popüler şekiller bulunmaktadır.

Gereksinimler

    Python 3.x
    Pillow (PIL) - Görselleri işlemek için
    numpy - Görsellerin piksel verilerini işlemek için
    pyfiglet - Metin ASCII sanatı oluşturmak için
    colorama - Renkli çıktılar için

Bu kütüphaneleri yüklemek için aşağıdaki komutu kullanabilirsiniz:

pip install pillow numpy pyfiglet colorama

Kullanım
1. Fotoğrafı ASCII Sanatına Dönüştürme

Bir görseli ASCII sanatına dönüştürmek için:

    Uygulama açıldığında "1" seçeneğini seçin.
    Fotoğrafın yolunu girin.
    Görselin genişliğini belirleyin (varsayılan olarak 100 birim).

2. Kelimeyi ASCII Sanatına Dönüştürme

Bir kelimeyi ASCII sanatı olarak yazdırmak için:

    Uygulama açıldığında "2" seçeneğini seçin.
    Yazdırmak istediğiniz metni girin.
    ASCII yazı tipi seçin.
    Yazı boyutunu belirleyin (1-10 arasında).

3. Şekil ASCII Sanatını Görüntüleme

Önceden tanımlanmış şekilleri görüntülemek için:

    Uygulama açıldığında "3" seçeneğini seçin.
    Mevcut şekillerden birini seçin (örneğin: kare, kalp, emoji_smile vb.).

Dosya Yapısı

    nesne.txt: Önceden tanımlanmış ASCII şekillerini içeren dosya. Bu dosya, kare, yuvarlak, kalp, telefon gibi ASCII sanat şekillerini içerir.

Örnek Çıktılar
1. Fotoğraf ASCII Sanatı

@%%%##*++++++====-::::. . .
..%%%###@%###**+++++=::::...

2. Metin ASCII Sanatı

  ____  _           _    _               
 |  _ \| |__   __ _| | _| |__   __ _ _ __ 
 | |_) | '_ \ / _` | |/ / '_ \ / _` | '__|
 |  __/| | | | (_| |   <| | | | (_| | |   
 |_|   |_| |_|\__,_|_|\_\_| |_|\__,_|_|   

3. Şekil ASCII Sanatı (Örnek: Kalp)

   ******       ******
 **********   **********
************* *************
*****************************
 ***************************
   ***********************
     *******************
       ***************
         ***********
           *****
            ***
             *

