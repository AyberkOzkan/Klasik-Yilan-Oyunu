import turtle
import random

# Sabit değerleri tanımlıyoruz.

genislik = 900
yukseklik = 500
gecikme = 100                                   # Milisaniye
yem_boyutu = 12                                 # Pixel
renkler = ['red', 'yellow', 'cyan','green', 'purple', 'pink', 'blue']
sekiller = ['circle', 'square', 'triangle']

yonler = {                                      # Yönleri belirlemek için sözlük oluşturuyorum.
    'yukarı': (0, 20),
    'aşağı': (0, -20),
    'sağ': (20, 0),
    'sol': (-20, 0),
}

def yon_tuslari():
    ekran.onkey(lambda: yilan_yon_belirle('yukarı'), "Up")
    ekran.onkey(lambda: yilan_yon_belirle('sağ'), "Right")
    ekran.onkey(lambda: yilan_yon_belirle('aşağı'), "Down")
    ekran.onkey(lambda: yilan_yon_belirle('sol'), "Left")
    ekran.onkey(lambda: yilan_yon_belirle('yukarı'), "w")
    ekran.onkey(lambda: yilan_yon_belirle('sağ'), "d")
    ekran.onkey(lambda: yilan_yon_belirle('aşağı'), "s")
    ekran.onkey(lambda: yilan_yon_belirle('sol'), "a")


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




def hareket_yilan():
    bas.clearstamps()

    yeni_bas = yilan[-1].copy()                 # Kopyalamazsak eğer orijinal halini değiştirir.
    yeni_bas[0] += yonler[yilan_yon][0]         # Yılanın Hareketini sağlamak için X ve Y koordinatlarına ekleme yapıyoruz.
    yeni_bas[1] += yonler[yilan_yon][1]         # [0] = X koordinatı [1] = Y koordinatı
    
    # Çarpışmayı Kontrol Et
    if yeni_bas in yilan or yeni_bas[0] < - genislik / 2 or yeni_bas[0] > genislik / 2 or yeni_bas[1] < - yukseklik / 2 or yeni_bas[1] > yukseklik / 2:
        reset()                            # Çarpma olunca kapatacak.
    else:
        yilan.append(yeni_bas)
         
        if not yem_etkilesim():
            yilan.pop(0)                        # Beslenmediği sürece aynı boyutta kalsın.
            
        for parca in yilan:                     # Yılanı çizdirdiğimiz kodların aynısı.
            bas.goto(parca[0], parca[1])            
            bas.stamp()
        
        # Ekranı yenileyelim.
        ekran.title(f' - Klasik Yılan Oyunu - Skor: {skor}')
        ekran.update()
        # Tekrar Etmeli
        
        turtle.ontimer(hareket_yilan, gecikme)
        

# 2 ye bölüyoruz çünkü (0,0)dan başlıyoruz. Yani yılanın bir kısmı negatif kısımda diğer kısmı pozitifte.
# Her şeyi tanımladık fakat yılanı çizdirmemiz gerekiyor.
def yem_etkilesim():
    global yem_pozisyon, zehir_pozisyon, skor
      
    if uzaklık_bul(yilan[-1], yem_pozisyon) < 20: # Yılanın başı ve yem birbirine 20 pixel yakınsa bu bir etkileşim olarak göstermiş olduk.
        
        skor += 1
        yem_pozisyon = rastgele_yem()
        yem.goto(yem_pozisyon)
        zehir_pozisyon = rastgele_yem()
        zehir.goto(zehir_pozisyon)
        
        return True
    elif uzaklık_bul(yilan[-1], zehir_pozisyon) < 20:
        skor += -1
        zehir_pozisyon = rastgele_yem()
        zehir.goto(zehir_pozisyon)
        yilan.pop(0) 
    return False


def rastgele_yem():
    y = random.randint(- yukseklik / 2 + yem_boyutu, yukseklik / 2 - yem_boyutu)                          # Rastgele int verecek.
    x = random.randint(- genislik / 2 + yem_boyutu, genislik / 2 - yem_boyutu)                          
    yem.color(random.choice(renkler))
    
    return(x, y)

def uzaklık_bul(pos1, pos2):
    x1, y1 =pos1
    x2, y2 =pos2
    uzaklık =((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5 # Pisagor
    return uzaklık
    
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


# Yılanın hareket edeceği ekranı yaratalım.
ekran = turtle.Screen()
ekran.setup(genislik, yukseklik)                # Boyut değerlerini girelim.
ekran.title('Klasik Yılan Oyunu')               # Başlık
ekran.bgcolor('Black')                          # Arkaplan rengini ayarlayalım. (HEX kodda kullanılabilir.)
ekran.tracer(0)                                 # Otomatik animasyonları devredışı bırakıyor.


# Tuşa basma olayı
ekran.listen()                                  # Ekrana Tuş basışlarını veya mouse kliklerini dinlemesini söylüyor.
yon_tuslari()

bas = turtle.Turtle()
bas.shape("circle")                             # Yılanın şekli
bas.color("Cyan")                               # Yılan rengi
bas.penup()                                     # Hareket halinde çizim yapılmaması için.


# Yem
yem = turtle.Turtle()
yem.shapesize(yem_boyutu / 20)
yem.penup()

yem.shape('circle')

# Zehirli Yem

zehir = turtle.Turtle()
zehir.shapesize(yem_boyutu / 20)
zehir.penup()
zehir.shape('circle')
zehir.color("orange")

reset()                     

turtle.done()