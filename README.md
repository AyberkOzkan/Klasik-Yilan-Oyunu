# **Klasik Yılan Oyunu**

Hem eğlenerek hemde Python becerilerinizi geliştirmek için Klasik Yılan Oyunu yapmaya ne dersiniz? Python'da Turtle Grafiklerini kullanarak animasyonları nasıl kontrol ettiğimi, global değişkenlerin önemini, Lambda kullanımı ve bir yılan oyununun turtle grafiklerle nasıl yapıldığını öğrenebilirsiniz. Bu projede çok kısa bir sürede bilgilerinizi tazeleyebilecek ya da hiç bilmediğiniz bilgiler öğrenebileceksiniz. 

Bu oyunu yaparken her kodu satır satır açıklamaya çalıştım. İster kodların üzerinde değişiklik yaparak kendi tarzını yansıtabilirsiniz. İsterseniz adım adım benimle birlikte yapabilirsiniz tamamen size kalmış.

Hazırsanız öncelikle teorik olarak ne yapacağımızı tartışalım.

Bize 1 adet yılan lazım. Biz bu yılanı X ve Y koordinat çiftlerinde bir liste olarak temsil edebiliriz. Neden liste sorarsanız eğer, yılanın hareketini sağlamak için ekleme ve çıkarma işlemi yapmamız gerekiyor. Eğer biz Tuple olarak ayarlarsak yılanın başına ve sonuna ekleme çıkarma işlemleri yapamayız.



```py
yilan = [[0,0], [20,0], [40,0], [60,0]]
```
_Kuyruk -> [0,0]_ <br>
_Baş -> [60,0]_

Liste içinde liste oluşturduğumuz zaman yani [x,y] olarak oluşturursak, yılanımız bölümleriyle birlikte yatay olarak Y düzleminde uzanıyor. Bu yılanın hareket etmesi için öncelikle "Baş kısmına" [80,0]'i eklemeliyiz. Sonrasında ise [0,0]'ı çıkarmamız gerekiyor. Kısaca baş kısmına ekleme yap kuyruk kısmını sil.

Hareket için önce yeni bir baş kısmı oluşturmalıyız.

```py
yeni_bas = yilan[-1].copy()
```

Burada orijinalini kaybetmemek için kopyalıyoruz. "-1" ile baş kısmını kopyalıyoruz. (Listeden eleman çekerken -1 kullanmamızın nedeni ile aynı en sağdaki elemanı istiyoruz.)

yeni_bas artık [60,0]. Hareketi sağlaması için ekleme yapmamız gerekiyor.

```py
yeni_bas[0] += 20
```

X koordinatına 20 ekleyerek arttırıyoruz. [80,0] oluyor.
```py
yilan.pop(0)
```

komutuyla ise listenin başındaki yani en soldaki listeyi siliyoruz. Kafamızda bir şeyler oluştu değil mi? Hadi gelin birlikte kodlamaya başlayalım.

```py
# Turtle Grafik Modülünü içeriye aktarıyoruz.
import turtle

# Sabit değerleri tanımlıyoruz.

genislik = 900
yukseklik = 500
gecikme = 400                                   # Milisaniye



# Yılanın hareket edeceği ekranı yaratalım.
ekran = turtle.Screen()
ekran.setup(genislik, yukseklik)                # Boyut değerlerini girelim.
ekran.title('Klasik Yılan Oyunu')               # Başlık
ekran.bgcolor('purple')                         # Arkaplan rengini ayarlayalım. (HEX kodda kullanılabilir.)
ekran.tracer(0)                                 # Otomatik animasyonları devredışı bırakıyor.

bas = turtle.Turtle()
bas.shape("circle")
bas.penup()                                   # Hareket halinde çizim yapılmaması için.

# Yılanın koordinat listesi

yilan = [[0, 0], [20, 0], [40, 0] ,[60, 0]]     # Global değişkenler!
yilan_yon = 'up'

# Yılanı ilk defa çizdirelim.

for parca in yilan:
    bas.goto(parca[0], parca[1])              # X = 0 ve Y = 0 koordinatlarına
    bas.stamp()       

turtle.done()

```

![first](Görseller/ss1.JPG)


Şimdilik duran bir yılanımız var. Bu yılanı öncelikle hareket ettirmemiz gerekiyor. Bunu bir fonksiyon yardımıyla yapabiliriz. Yukarıda bahsettiğimiz teoriyi buraya uygulayalım.

```py
def hareket_yilan():
    bas.clearstamps()                           
    yeni_bas = yilan[-1].copy()                 # Kopyalamazsak eğer orijinal halini değiştirir.
    yeni_bas[0] += 20                           # Yılanın baş kısmına ekleme yapıyoruzki ilerleyebilsin.
    
    yilan.append(yeni_bas)
    yilan.pop(0)                                # En sonuncu listeyi siliyor.
    
    # Her şeyi tanımladık fakat yılanı çizdirmemiz gerekiyor.
    
    for parca in yilan:                         # Yılanı çizdirdiğimiz kodların aynısı.
        bas.goto(parca[0], parca[1])            
        bas.stamp()

    # Ekranı yenileyelim.
    ekran.update()
    # Tekrar Etmeli
    turtle.ontimer(hareket_yilan, gecikme)
```
Tabi fonksiyon yarattıysak onu programda çağırmamız gerekiyor. ```turtle.done()``` komutundan önce çağıralım.

```py

# Animasyon Kısmı
hareket_yilan()  

```
![second](Görseller/ss2.JPG)

Mor ve siyah uyumunu göz yorucu buldum. Sizde bu kısma geldiyseniz sorunsuz bir şekilde, Yılanınızı ve arkaplanınızı kişiselleştirmeyi unutmayın :)

Elimizde sadece sağa doğru giden bir yılanımız var. İstediğimiz yönde hareket etmesi için yeni 2 adet değer tanımlamalıyız. Yukarı, aşağı, sağ ve sol hareketlerini gerçekleştirebilmesi için bir adet sözlüğe yani dictionary'e ihtiyacımız var. Bu sözlük sayesinde hangi yöne ne kadar gideceğini ayarlayabileceğiz.

```py

yonler = {                                      # Yönleri belirlemek için sözlük oluşturuyorum.
    'yukarı': (0, 20),
    'aşağı': (0, -20),
    'sağ': (20, 0),
    'sol': (-20, 0),
}
```

Şimdi de global değişken olarak;
```py 
yilan_yon = 'yukarı' 
```
ekleyelim.

Buraya kadar yaptığımız ve yazdığımız kodlarda program bizim klavyeden tuşa basıp basmadığımızı anlayamıyor buda demek oluyor ki yılanı yönlendirmemiz için klavyeden girdi girdiğimiz zaman onu programın bilmesi gerekiyor.

Örneğin 
```py
    turtle.done()
```

Bu komut bizim pencereyi kapatmamız için çarpı işareti yani ```X```'e bastığımızı bekliyor bu sayede programdan çıkış yapıyor.

Biz yılanımızın yönünü değiştirmek için ok yön tuşlarını kullanmak istiyoruz. Bunun için programda bir kullanıcı girdi izleme döngüsü oluşturmalıyız. Yani kısaca bizim tuşa basmamızı bekleyen bir döngü. Tabiki bunu da Ekran kısmında yazmalıyız.

```py

ekran.listen()                                  # Ekrana Tuş basışlarını veya mouse kliklerini dinlemesini söylüyor.

```

Şimdi gelin tuşlara bastığımızı programa söyleyelim.

```py

ekran.onkey(yukariya, "Up")
ekran.onkey(asagiya, "Down")
ekran.onkey(sola, "Left")
ekran.onkey(saga, "Right")

```

Burada parantez içindeki yön belirten ifadeleri tanımlamadık, onları tanımlayalım. Fonksiyon olarak yapmak daha mantıklı duruyor sizin bir fikriniz var mı?

```py
def yukariya():
    global yilan_yon
    if yilan_yon != "aşağı":
        yilan_yon = "yukarı"

def asagiya():
    global yilan_yon
    if yilan_yon != "yukarı":
        yilan_yon = "aşağı"

def sola():
    global yilan_yon
    if yilan_yon != "sağ":
        yilan_yon = "sol"

def saga():
    global yilan_yon
    if yilan_yon != "sol":
        yilan_yon = "sağ"
```

Şimdi bir değişiklik yapmamız gerekiyor hatırlarsanız ```yonler``` isimli bir sözlüğümüz ve ilk oluşturduğumuz ```hareket_yilan``` isimli bir fonksiyonumuz vardı. Bu fonksiyonumuzun içinde ```yeni_bas[0] += 20``` bir kod parçamız vardı. Eğer biz yılanımızı hareket ettireceksek x ve y koordinatlarında hareketini sağlamalı. Başta yazdığımız bu kod parçası sadece X koordinatında hareket ettiriyor.


```py

yeni_bas[0] += yonler[yilan_yon][0]         
yeni_bas[1] += yonler[yilan_yon][1]         # [0] = X koordinatı [1] = Y koordinatı
```

Yazdığımız kodları deneyelim. <br>

![YönTesti](Görseller/3.gif)

- Burada göze çarpan bir şeyden bahsetmek istiyorum, Oyun açıldığı zaman ilk olarak yılan yukarı doğru hareket ediyor. Burada bence doğal olması adına; <br>
``` yilan_yon = 'yukarı'  ``` yerine ``` yilan_yon = 'sağ'  ``` yapalım. <br>

- İkinci olarak yılanımız pencere dışına çıktığında sonsuz bir dünya da kayboluyor. Geri getirmek biraz zor buraya bir sınır getirmeliyiz.

<hr>

Şimdi yapmak istediklerimize geri dönelim.

1) Duvarla, yılanın kendisiyle ve yiyeceklerle çarpışma olup olmadığını kontrol edip bunları uygun bir şekilde oyuna eklemeliyiz.
2) Yılanı ekrandan temizleyip yeni pozisyona çekmek.
3) Puan


Hadi başlayalım. Öncelikle ```hareket_yilan``` adlı bir fonksiyonumuz vardı. Bunun içerisine X koordinatlarını, Y koordinatlarını ve Yılanımızın olduğu konumu kontrol eden if-else kontrolcüsü koyalım. Aralarda ```or``` kullanıyoruz çünkü herhangi bir durumda olursa ekranımızın kapanmasını istiyoruz. ```yeni_bas[0]``` --> X koordinatlarını ```yeni_bas[1]``` Y koordinatlarını kontrol ettiriyor. 2'ye bölüyoruz çünkü yılanımızı (0,0)'dan başlatıyoruz. Koordinat sistemini düşünürseniz hem -X tarafı hemde X tarafı var. Şuan bizim genişliğimiz 900 yani (0,0) koordinatındayken hem sol tarafında 450 var hemde sağ tarafında 450 var.

```py

if yeni_bas in yilan or yeni_bas[0] < - genislik / 2 or yeni_bas[0] > genislik / 2 or yeni_bas[1] < - yukseklik / 2 or yeni_bas[1] > yukseklik / 2:
        turtle.bye()                            # Çarpma olunca kapatacak.
    else:
        yilan.append(yeni_bas)
        yilan.pop(0)                            # En sonuncu listeyi siliyor.
        for parca in yilan:                     # Yılanı çizdirdiğimiz kodların aynısı.
            bas.goto(parca[0], parca[1])            
            bas.stamp()
        
        # Ekranı yenileyelim.
        ekran.update()
        # Tekrar Etmeli
        turtle.ontimer(hareket_yilan, gecikme)


```

Eğer duvar yoksa oyunumuz normal olarak devam etmeli burada ise ```else``` kısmı devreye giriyor. Önceki yazdığımız kodlarımızı ```else``` kısmına ekliyoruz.
<br>Şimdi duvarlarımızı deneyelim.

![DuvarTest](Görseller/4.gif)

Yılan oyunun ana amacı yılanın beslenmesi. Şuan bizim yılanımızında ihtiyacı olan şey bu. Bizde yılanımızı beslemek için bir yem fonksiyonu eklemeliyiz.

Bu fonksiyon için iki nokta arasındaki uzaklığı bulmamız gerekiyor. Bunu bulabilmek için meşhur hepimizin bildiği _Pisagor Teoremini_ kullanacağız. Tanımlamamız gereken şey şu, Yılanın başı yeme yeterince yaklaştığı zaman bunu çarpışma olarak algılaması


![Pisagor](Görseller/Pisagor.JPG)

```py

def uzaklık_bul(pos1, pos2):
    x1, y1 =pos1
    x2, y2 =pos2
    uzaklık =((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5 # Pisagor
    return uzaklık
```

Şimdi sıra yeme geldi oyunda rastgele yerlerde ortaya çıkan bir yem fonksiyonu yazalım. Rastgele olması için random modulünü içeriye aktaralım öncelikle. Birde yemlerin boyutlarını tanımlamak gerekiyor.
```py
import random

yem_boyutu = 12                 # Pixel
```


Oyunda rastgele yem ortaya çıkarmak için

```py

def rastgele_yem():
    y = random.randint(- yukseklik / 2 + yem_boyutu, yukseklik / 2 - yem_boyutu)                          # Rastgele int verecek.
    x = random.randint(- genislik / 2 + yem_boyutu, genislik / 2 - yem_boyutu)                            # Neden 2'ye böldüğümüzü anlattım aynı mantık burada geçerli.                        
    return(x, y)
```


Yılanımızın yem ile etkileşime girdiğini belirlemek için bir fonksiyon yazalım 

```py
def yem_etkilesim():
    global yem_pozisyon
    if uzaklık_bul(yilan[-1], yem_pozisyon) < 20: # Yılanın başı ve yem birbirine 20 pixel yakınsa bu bir etkileşim olarak göstermiş olduk.
        
        yem_pozisyon = rastgele_yem()
        yem.goto(yem_pozisyon)
        return True
    return False
```

Sonrasın da ```Çarpışmayı kontrol et``` bölümünü şöyle düzenleyelim.

```py

# Çarpışmayı Kontrol Et
    if yeni_bas in yilan or yeni_bas[0] < - genislik / 2 or yeni_bas[0] > genislik / 2 or yeni_bas[1] < - yukseklik / 2 or yeni_bas[1] > yukseklik / 2:
        turtle.bye()                            # Çarpma olunca kapatacak.
    else:
        yilan.append(yeni_bas)                  # Çarpma yok ama yem yediğinde yılanımız büyüsün.
        
        if not yem_etkilesim():
            yilan.pop(0)                        # Beslenmediği sürece aynı boyutta kalsın.
            
        for parca in yilan:                     # Yılanı çizdirdiğimiz kodların aynısı.
            bas.goto(parca[0], parca[1])            
            bas.stamp()
        
        # Ekranı yenileyelim.
        ekran.update()
        # Tekrar Etmeli
        turtle.ontimer(hareket_yilan, gecikme)
```

Sonrasında alt kısımda yemimizi tanımlayalım.

```py

# Yem
yem = turtle.Turtle()
yem.shape("circle")
yem.shapesize(yem_boyutu / 20)
yem.penup()
yem_pozisyon = rastgele_yem()
yem.goto(yem_pozisyon)
yem.color("cyan")

```
<hr>
<br>
Yem rengini tek renk olarak ayarladık ama biraz daha eğlence katmak için yem rengini rastgele seçmesini ve yukarıdaki kodlarda yaptığımız şekilde yılanımızı kısaltan zehirli yem yapmaya ne dersiniz? 

Bunları yaptıktan sonra bir yemi yedikten sonra tüm yemler resetlenip farklı yerde ortaya çıkmasını sağlayalım.
<hr>
<br>

![RenkliYemler](Görseller/5.gif)



Bir tane de skor tablosu yapalım. Skor sayacı için bir tane değişken tanımlayalım.
```py

skor = 0

```

Sonra ```yem_etkilesim()``` fonksiyonumuzun ```if``` kısmına ```skor += 1``` ekleyelim. global olarak eklemeyi unutmayın.

```py

global skor
    if uzaklık_bul(yilan[-1], yem_pozisyon) < 20: # Yılanın başı ve yem birbirine 20 pixel yakınsa bu bir etkileşim olarak göstermiş olduk.
        
        skor += 1
```
ve ekranımızda görmek için ```ekran.title(f'Skor: {skor}') ``` kod parçasını ekleyelim.

```py

# Ekranı yenileyelim.
        ekran.title(f'Skor: {skor}')
        ekran.update()

```
Artık yem yenildiğinde skor sayacını arttığını görebilirsiniz.
<hr>
<br>
Oyunda yandığımız zaman oyun direk kendini kapatıyor. Bunu yukarıda ```turtle.bye()``` ile yapmasını sağladık fakat tekrar oynamak için programı tekrardan başlatmamız gerekiyor. Buda ideal olan bir şey değil. Bunu düzeltmek için bir reset fonksiyonu yaratabiliriz. Önceden yazdığım eski kodlarıda içine eklediğimiz bir ```reset()``` fonksiyonu yazalım.
<hr>
<br>

```py

def reset():
    global skor, yilan, yilan_yon, yem_pozisyon, zehir_pozisyon
    skor = 0
    # Yılanın koordinat listesi
    yilan = [[0, 0], [20, 0], [40, 0] ,[60, 0]]     # Global değişken!
    yilan_yon = 'sağ'                               # Yılanın ilk baştaki yön değerini sağ olarak ayarlayalım.
    yem_pozisyon = rastgele_yem()
    yem.goto(yem_pozisyon)
    zehir_pozisyon = rastgele_yem()
    zehir.goto(zehir_pozisyon)
    hareket_yilan()

```

Ve bu bölümü siliyoruz.

```py

# Yılanı ilk defa çizdirelim.

for parca in yilan:
    bas.goto(parca[0], parca[1])                # X = 0 ve Y = 0 koordinatlarına
    bas.stamp()                               


```

_Lambda_ fonksiyonu kullanarak yılanımızı daha efektif bir şekilde daha az kod kullanarak yönetebiliriz. Nasıl mı?
Öncelikle aşağıdaki kodlardan kurtulalım.

```py
ekran.onkey(yukariya, "Up")
ekran.onkey(asagiya, "Down")
ekran.onkey(sola, "Left")
ekran.onkey(saga, "Right")
```
Yerine bir tane fonksiyon yaratalım.

```py
def yon_tuslari():
    ekran.onkey(lambda: yilan_yon_belirle('yukarı'), "Up")
    ekran.onkey(lambda: yilan_yon_belirle('sağ'), "Right")
    ekran.onkey(lambda: yilan_yon_belirle('aşağı'), "Down")
    ekran.onkey(lambda: yilan_yon_belirle('sol'), "Left")
```

Sonrasında her yön için bir fonksiyon kullanmak yerine tek bir fonksiyon kullanalım.

```py

def yilan_yon_belirle(yon):
    global yilan_yon
    if yon == "yukarı":
        if yilan_yon != "aşağı":    # Yanlış tuşa basıldığında çarpışmayı önlemek için 2. bir kontrol ediyoruz.
            yilan_yon = "yukarı"
    elif yon == "aşağı":
        if yilan_yon != "yukarı":
            yilan_yon = "aşağı"
    elif yon == "sol":
        if yilan_yon != "sağ":
            yilan_yon = "sol"
    elif yon == "sağ":
        if yilan_yon != "sol":
            yilan_yon = "sağ"

```

ve eski kodlarımızı silelim.

```py

def yukariya():
    global yilan_yon
    if yilan_yon != "aşağı":
        yilan_yon = "yukarı"

def asagiya():
    global yilan_yon
    if yilan_yon != "yukarı":
        yilan_yon = "aşağı"

def sola():
    global yilan_yon
    if yilan_yon != "sağ":
        yilan_yon = "sol"

def saga():
    global yilan_yon
    if yilan_yon != "sol":
        yilan_yon = "sağ"
```

İlk sildiğim kodlar yerinde ```yon_tuslari()``` fonksiyonumuzu çağıralım.


![OyununKendisi](Görseller/6.gif)


<hr>
<br>
Yapılması ve düzeltilmesi gerekenler:

- Yılan sadece zehirli yemi yediği zaman yani skor = -4'e eşit olduğunda oyun resetlenmiyor.
- Yemlerden birini aldıktan sonra diğer yemin durması ve yeni 2 adet yemin ortaya çıkması.

<hr>
<br>







