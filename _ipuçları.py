# COMMEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEENT!!!!!!!!!!

# When writing code, simultaneously try on for a small object. 

#  
import keyword		keyword.kwlist
del degisken
#sonuc=gün * (gidiş_ücreti + dönüş_ücreti) değeri gün'ün değerini değiştirince değişmedi,
#tekrar atamak gerekiyo!!!
pow(3,2,4)=1
ocak = mart = mayıs = temmuz = ağustos = ekim = aralık = 31
y=7; u=6
---
osman, mehmet=mehmet, osman						#çok hoş
---
>>> print("""gel			#birden fazla satıra yayılmış karakter dizilerinin gösterilmesi için birebir
... dm""")
---
print("Tahir", "Zühre") denktir print("Tahir", "Zühre", sep=" ", end="\n", file=sys.stdout)
---
dosya=open("yeni","w")
print("bismillah",file=dosya)	denktir		print("bismillah",file=dosya,flush=False)
dosya.close()								#flush parametresi True olursa dosyanın kapatılmasını
#beklemeden print ediyo
---
print(*"galatasaray",sep=") 		# karakter dizisini tek tek öğelerine ayırıp
# bu öğeleri yine tek tek ve sanki her bir öğe ayrı bir parametreymiş gibi o fonksiyona gönderiyor
len(*"gala","tasaray") = 5 			#lüzumsuz gibi görünebilir ama nerede işe yarayacağı belli olmaz
---
sys.stdout #değişken örneği
sys.exit() #fonksiyon örneği		# python'dan çıkmayı sağlıyor, en azından cmd prompt'ta
sys.version
---	
sys.stdout=dosya
---					
sys.stdout.name
sys.stdout.encoding
sys.stdout.mode
---
#Etkileşimli kabuğu tekrar açtığınızda her şeyin eski haline döndüğünü göreceksiniz. 
#Aynı şekilde, eğer bu kodları bir program dosyasına yazmış olsaydınız, programınız 
#kapandığında her şey eski haline dönecekti.
f, sys.stdout = sys.stdout, f						
---
print("\"book\" kelimesi \"kitap\" demektir.")	
print("millet\ ne yapıoruz")							
print("\n","-"*len(başlık),"\n",başlık,"\n","-"*len(başlık),"\n",sep="")
open("C:\nisan\masraflar.txt")					#gives error, there should be two \ or at the beginning r
print("\a"*10)									#heryerde çalışmaz
print("Merhaba\rdünya")							#dünya merhaba yazmaya yarıyo ama ee? biraz garip geldi
print("düşey\vsekme")							#heryerde çalışmaz, ki benim bilgisayarda çalışmadı
print("yahoo.com\b.uk")	m'yi sildi		print("risale","\b","\b.com")		print("istihza\b\b\bsn")
#Aslına bakarsak, bu programlama dilinin bütün felsefesi, ‘bir kez yazılan kodların en verimli 
#şekilde tekrar tekrar kullanılabilmesi,’ fikrine dayanıyor.
#Gömülü fonksiyonlar, kendi tanımladığımız fonksiyonlar, hazır modüller, üçüncü şahıs modülleri 
#hep belli bir karmaşık süreci basitleştirme, bir kez tanımlanan bir prosedürün 
#tekrar tekrar kullanılabilmesini sağlama amacı güdüyor.
#Mesela, grafik bir arayüze sahip (yani düğmeli, menülü) programların ezici çoğunluğu 
#nesne tabanlı programlama yöntemiyle geliştiriliyor.
#Nesne tabanlı programlama, komut arayüzlü programlar geliştirmek için de kullanışlı bir programlama yöntemidir.
---										
sesli_harfler="aeıioöuü"
sayaç=0
kelime=input("Bir kelime girin: ")
for harf in kelime:
	if harf in sesli_harfler:
		sayaç+=1
mesaj="{} kelimesinde {} sesli harf var."
print(mesaj.format(kelime,sayaç))
---
print(r"Kurulum dizini: C:\aylar\nisan\toplam masraf")
(#!/usr/bin/env python3 ve # -*- coding: utf-8 -*- satırları hariç).
---
sayı = input("Herhangi bir veri girin: ")
tip = type(sayı)
print("Girdiğiniz verinin tipi: ", tip)
---
#eval() ve exec() hakkındaki güvenlik açığı meselesine dikkat (security bug veya security flaw)
bunlar işe yarar fonksiyonlar
---	
print("Hata! Google Chrome {} {} bulamadı".format(url,neyi)) veya print(cümle.format(...))
---
metin="Hata! Google Chrome {} {} bulamadı"
metin.format(url,neyi)							veya 		("xyz.com","adresini")
---
>>> kartvizit="""
... istihza aonim şikeri
... fırat özgül
... 9089
... """ dedikten sonra komut satırına kartvizit yazıp enterlamak ile print(kartvizit) demek farklı sonuç veriyor!!!
ayrıca şu """ alt satıra geçme konusunda çok iyi """
---
sayı = int(input("Bir sayı giriniz: "))
3+5		# 3 ve 5 operand(işlenen) ve + işareti işleç(operator)		
#65 % 10 = 5		herhangi bir sayının son basamağını elde etmek için
int(4/3)		=		1		4//3	=	1		ikisi de round etmiyo.
---
round(2.48)		=		2
round(2.75,1)	=		2.8
---
pow(25,2,5)		=		(25**2)%5
bool(0)=bool("")=False
---
isim = input("İsminiz: ")
print(isim == "Ferhat")
---
kullanıcı=input("kullanıcı adınızı giriniz: ")
if kullanıcı:
	print("Teşekkürler")
---
if'leri iç içe kullanmak yerine and filan kullan					
note>=90 and note<=100		ile 		note>=90<=100 aynı;		90<=note<=100 ile zaten aynı
a-=5 işlemi normaline göre daha hızlı çalışır
"i" in "inek"
id(a)			a is 100
#is işleci nesnelerin kimliklerine bakıp o nesnelerin aynı nesneler olup olmadığını kontrol ederken,
# == işleci nesnelerin içeriğine bakarak o nesnelerin aynı değere sahip olup olmadıklarını sorgular.
a is 1000 şu demek:	id(a)==id(1000)
#Python kendi iç mekanizmasının işleyişi gereğince ‘ufak’ nesneleri önbelleğe alırken
# ‘büyük’ nesneler için her defasında yeni bir depolama işlemi yapıyor.
sys.version_info.major
# -*- coding: utf-8 -*- (veya ASCII) ama python3'te zaten utf-8 olduğu için buna gerek yok
---
girdi=u"gelsene" # unicode olarak tanımlamak için. çünkü mesela 2x sürümlerinde # -*- falan yazıp, coding'i
#utf-8 yapıp hata mesajından kurtulsan bile türkçe karakterler düzgün görüntülenmeyebilir,o yüzden bu lazım
---
ctrl+c ve ctrl+z: keyboard interrupt
---
while True:		#Aksi belirtilmediği sürece çalışmaya devam et! demek
...
	break
---
tekrar=1
while tekrar<=3:
    tekrar+=1
    input("Nassın iyimin?")
---
#bir Python programının nasıl çalıştığını anlamanın en iyi yolu, program içinde uygun yerlere 
#print() fonksiyonları yerleştirerek arka planda hangi kodların hangi çıktıları verdiğini izlemektir.
__import__("os").system("dir")
---
for i in range(0,10):	#range(10) desek de olur #ilk sayı dahil, son sayı dahil değil
	print(i)
---
izinli_karakterler = "0123456789+-/*= "
for s in veri:
    if s not in izinli_karakterler:
        print("Neyin peşindesin?!")
        quit()
hesap = eval(veri)							# TEKRAR BAK. TAM OLARAK NE İŞE YARADIĞINI HATIRLAMIYORUM
---
print(*range(10))
pass: hiç bir şey yapmadan yoluna devam et	# TEKRAR BAK
# Programın gidişatına göre, bir noktada yapmanız gereken bir işlem var, ama henüz ne yapacağınıza karar vermediniz.
# Böyle bir durumda oraya bir pass koyarak durumu şimdilik geçiştiriyorsunuz.
break ifadesinin her zaman bir döngü içinde yer alması gerekiyor. Aksi halde """SyntaxError: 'break' outside loop"""
continue döngünün başına döndürür
---
>>> ilk_metin = "asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjh"
>>> ikinci_metin = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"
>>> for i in ilk_metin:
...     if i not in ikinci_metin:
...             if i not in dizi:
...                     print(i)
...                     dizi+=i
...
a
ş
---	veya
for s in ilk_metin:
    if not s in ikinci_metin and not s in dizi:
            dizi+=s
            print(s)
a
ş
---

---
print(repr(karakter_dizisi))	#çıktıdaki \n'leri görebilmek için								# TEKRAR BAK
#bug‘lar ise çok daha karmaşıktır. Kusurlu programlar çoğu zaman herhangi bir hata vermeden çalışır. 
#Ancak programın ürettiği çıktılar beklediğiniz gibi değildir. Örneğin yazdığınız programda 
#bir formül hatası yapmış olabilirsiniz. Böyle bir program çalışma sırasında hata vermeyeceği için 
#buradaki sorunu tespit etmek, özellikle büyük programlarda çok güçtür. ooooo
---
ilk_sayı:input("ilk sayı: ")					
ikinci_sayı:input("ikinci sayı: ")
try:
	sayı1=int(ilk_sayı)
	sayı2=int(ikinci_sayı)
	print(sayı1,"/",sayı2,"=",sayı1/sayı2)
except ValueError:
	print("Lütfen sadece sayı girin: ")
veya
except (ValueError, ZeroDivisionError):		# hata ismi girmeyebiliriz. Örnek bi kullanım gelecek:
    print("Bir hata oluştu!")
#Böylece kullanıcıya anlamsız ve karmaşık hata mesajları göstermek ve daha da kötüsü, 
#programımızın çökmesine sebep olmak yerine daha anlaşılır mesajlar üretiyoruz. (çok iyi)
try:
    birtakım kodlar
except ValueError:
    print("Yanlış değer")
except ZeroDivisionError:
    print("Sıfıra bölme hatası")
except:
    print("Beklenmeyen bir hata oluştu!")
---
try:
    bölünen = int(input("bölünecek sayı: "))
    bölen = int(input("bölen sayı: "))
except ValueError:
    print("Lütfen sadece sayı girin!")
else:
    try:
        print(bölünen/bölen)
    except ZeroDivisionError:
        print("Bir sayıyı 0'a bölemezsiniz!")
#Bu yapı, her akla geldiğinde kullanılacak bir yapı değildir.
#Bu üçlü yapıyı hiç kullanmadan bir ömrü rahatlıkla geçirebilirsiniz.
---
import os
os.startfile("C:\\users\emre\desktop\pardus-hastane.png")		#veya (r"C:\users...)
Please note that on unix or mac, there should be a different code
So, you should be aware of that the code you wrote may not be working on other OS
---
chromePath	=r'C:\Users\emre\AppData\Local\Google\Chrome\Application\chrome.exe'
png			=r'C:\users\emre\desktop\pardus-hastane.png'
subprocess.Popen("%s %s" % (chromePath,png))
#bu çok hoşuma gitti: evet tasdik ediyorum. (png'yi chromePath ile açıyo) Emre
---
#yazdığınız programda mutlaka ama mutlaka işletilmesi gereken bir kısım varsa, o kısmı finally... bloğu içine 
#yazabilirsiniz. Mesela eğer dosya üzerinde işlem yapılırken bir hata ile karşılaşılırsa 
#dosyamızı kapatma işlemini gerçekleştirdiğimiz bölüme hiç ulaşılamayabilir.
---
raise Exception("Bu programda 23 sayısını görmek istemiyorum!")			
---
#hoşuma gitti:
site1 = "www.google.com"
site2 = "www.istihza.com"
site3 = "www.yahoo.com"
site4 = "www.gnu.org"
for isim in site1,site2,site3,site4:
	print("site: ",isim[4:-4])
#Burda hem 4:-4'teki -4 meselesi çok güzel hem de site'lerin yan yana yazılınca ortaya çıkan netice çok güzel
---
kardiz="istihza"
>>> kardiz[0:7:2]
'itha'
#ya kardiz[::-1] meselesini anladım ama oraya sayı yazarak neden olmuyo?
yani kardiz[::1] ile kardiz[0:7:1] aynı; bunu diğer türlü de yapmak istiyorum
---
for i in reversed("gelmene gerek yok"):
	print(i,end="")
veya
print(*reversed("gelmene gerek yok"),sep="")	#velhasıl range gibi, yani for döngüsü içine almak gerekiyo
---
for i in sorted("kitap"):
    print(i,end="")

aikpt
---
#sorted fonksiyonu türkçe karakteri içeren kelimeleri doğru sıralayamaz, o yüzden şunu yapmak lazım:
import locale																							
locale.setlocale(locale.LC_ALL, "Turkish_Turkey.1254")
sorted("çiçek",key=locale.strxfrm)	#yine de i'yi ı'dan önce yazdı. ama iyi. o da ufak bi kodla düzelir. veya
# aşağıdaki gibi:
---
>>> harfler="abcçdefgğhıijklmnoöprsştuüvyz"
>>> çevrim={i:harfler.index(i) for i in harfler}
>>> sorted("gelinız",key=çevrim.get)				# elh ala külli hal sivelküfri veddalal
['e', 'g', 'ı', 'i', 'l', 'n', 'z']
#her harfi bir sayıya atayarak yaptı				yukarda listelerin sort() metodu ile yapılanı var
---
print("http://",i) ifadesinin print("http://"+i) ile aynı sonucu vermesi için sonuna ,sep="" koymak lazım
karakter dizileri değiştirilemeyen (immutable) bir veri tipidir.
dir(complex)
---
major=sys.version_info[0]
minor=sys.version_info[1]
micro=sys.version_info[2]
print(major+minor+micro)
#u yöntem bütün python sürümlerinde çalışır
if sys.version_info[1] < 3:
    print("Kullandığınız Python sürümü eski!")
---
>>> organ="bağırsak"
>>> organ.replace("a","A")	
'bAğırsAk'
---
kardiz = "Bolvadin, Kilis, Siverek, İskenderun, İstanbul"						
kardiz=kardiz.split()		#.split(",",1) şeklinde parametleri de var. 1 dediği maxsplit.
# elhamdülillah .split(", ") deyince tam güzel ayırdı
for i in kardiz:			#ikinci parametreyi yazacaksan ilkini de mutlaka yazman lazım
	print(i)				# bu metod liste haline getiriyo
#bi de rsplit() var. Onun da tek farkı sağdan sola doğru ayırması
---
sys.version.split()[0]	#hoşuma gitti															
met=metin.splitlines() veya (True) 	#ikinci durumda \n'ler de geliyor				
---
iller = "ISPARTA, ADIYAMAN, DİYARBAKIR, AYDIN, BALIKESİR, AĞRI"
iller=iller.replace("I","ı").replace("İ","i").lower()				#.upper da bunun tersi işte
#lower() metodu yardımıyla standart bir hale getirilmesi sayesinde, kullanıcının girdiği kelimelerin 
#büyük-küçük harfli olmasının önemli olmadığı programlar yazabiliyoruz.
---
>>> for i in d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11:
...     if i.endswith(".mp3"):										#.startswith de tersi işte
...             print(i)
---
.capitalize ve .title metotları # bi fark göremedim aralarında: kelime ne olursa olsun sonuç: sadece ilk harfi büyük
değişken_adı.swapcase küçükleri büyük, küçükleri büyük yapar
.casefold() da .lower() gibi ama mesela Almancadaki ‘ß’ harfi farklı sonuç veriyor
---
.strip('s') karakter dizisinin baş ve sonundakileri kırpar											
metin=metin.strip(">"); print(metin) 		#emre bunu beğendi		.rstrip ve .lstrip de benzer
ama tutorial'da şöyle yapmış halbuki benim üstteki satırda yaptığım da aynı sonucu veriyor
İkinci bir örnek:
met="gele gele tabg geldig"
for i in met.split():
    print(i.strip("g"),end=" ")
ele ele tab eldi
---
" ".join(keyword.kwlist)	# parametre ile başındaki veri tipinin yerleri değişik gibi görünüyor olmasına dikkat
keyword.kwlist adlı listenin elemanlarının arasına bir boşluk koyup tek bir string haline getirdi 
_.split(" ")				# bu da eski haline getirdi
---
kendim bi ihtiyaca binaen iki metodu uyguladım harika oldu, fesubhanallah. Gayem şu stringteki \\'leri teke düşürmek:
st = 'C:\\Users\\emre\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\site-packages\\numpy'
st_l = st.split("\\") 	# aradaki \\'leri kaldırıp stringi \\'lerden bölerek liste haline getirdi
"/".join(st_l)			# şimdi de aralara / koyup tekrar string haline getirdim elhamdülillah 
yalnız şu hata veriyo, nasıl yapacağımı bilmek istiyorum: "\".join(st_l)
---
hoşlandım:
for i in parola:
	if parola.count(i)>1:
		kontrol=False
---
bu da hoşuma gitti. ben yazdım elh:
kelime = input("Herhangi bir kelime: ")
dizi=""
for harf in kelime:
	if not harf in dizi:	#not harf'ten sonra da oluyormuş
		print("{} harfi {} kelimesinde {} kez geçiyor!".format(harf, kelime, kelime.count(harf)))
		dizi+=harf
#tutorial'da bence daha amelece yapmış:
kelime = input("Herhangi bir kelime: ")
sayaç = ""
for harf in kelime:
    if harf not in sayaç:
        sayaç += harf
for harf in sayaç:
    print("{} harfi {} kelimesinde {} kez geçiyor!".format(harf, kelime, kelime.count(harf)))
---
"awak".count("a",1,2)	#3. parametre şart değil. Ve 2. parametre dahil ama 3. değil. yani slice gibi [1:3] ise 1'den 2'ye kadar 
---
sayaç=""
for i in range(len("adana")):
	if not str(i) in sayaç:
		deg="adana".index("a",i)
		print(deg)
		sayaç+=str(deg)
#tutorial daha orjinal ve güzel bir üslup ile çözmüş:
for i in range(len(kardiz)):
    if i == kardiz.index(aranacak, i):					#rindex() metodu da sağdan sola okur
        print(i)
#.find() ve .rfind() metotları da harfin olmadığı durumda hata yerine -1 vermesi dışında aynı
---
"elma".center(9,"-")																					
'---elma--'
---
for i in dir(""):			#.rjust() da sağa yaslar
    print(i.ljust(20,".")	#word'da içindekiler yazarken yapabilirdim bunu :)			
---
for i in range(11):																								
...     print(str(i).zfill(2))		#çünkü .zfill() karakter dizilerinin bir metodudur, sayıların değil		
---																																	
"istihza".partition("h")	#rpartition() da sağdan sola
('isti', 'h', 'za')
---
"çilek".encode("cp1254")
---
>>> a="elma\tbir\tmeyvedir"
>>> a.expandtabs(10)
'elma      bir       meyvedir'
---
#input() fonksiyonu bize bir karakter dizisi verdiği gibi str.maketrans() metodu da bize bir sözlük veriyor.
#sözlüğü str.maketrans() metoduna oluşturtmak yerine, kendiniz de bir sözlük oluşturarak 
#str.maketrans() metoduna parametre olarak atayabilirsiniz. 
kaynak = "şçöğüıŞÇÖĞÜİ"; hedef  = "scoguiSCOGUI"; çeviri_tablosu = str.maketrans(kaynak,hedef)
metin = "Bildiğiniz gibi, internet üzerinde bazen Türkçe karakterleri kullanamıyoruz."
print(metin.translate(çeviri_tablosu))
print(çeviri_tablosu)
print(çeviri_tablosu[351])
---																													
metin = """Bu programlama dili Guido Van Rossum adlı Hollandalı bir													
diyebiliriz."""
silinecek = "aeıioöuüAEIİOÖUÜ"
çeviri_tablosu = str.maketrans('', '', silinecek)	# Çünkü: the first two maketrans arguments must have equal length
print(metin.translate(çeviri_tablosu))				# amaç herhangi birşeyi değiştirmek değil, o harfleri silmek
---
>>> chr(97)		
'a'			
#Bilgisayarınızda gördüğünüz her karakter aslında bir sayıya karşılık gelir. Zaten bilgisayarlar 
#‘a’, ‘b’, ‘c’, vb. kavramları anlayamaz. Bilgisayarların anlayabildiği tek şey sayılardır.
---
>>> "kezb3an".isalpha()			#.isdigit() , .isalnum() , .isdecimal()													
False
---
.isidintifier() 	değişken, fonksiyon veya modul adı tanımlanabilir mi
.isnumeric() 		sayı mı değil mi
.isspace 			bir tane bile boşluk dışı karakter var mı yok mu? Sadece boşluk ise true (ama "" false verir)	
"\n".isprintable() 	anlaşılıyo
---
>>> for sıra,karakter in enumerate(kardiz,1):
...     print("%s. karakter: '%s' "%(sıra,karakter))
...
1. karakter: 'i'
2. karakter: 's'
3. karakter: 't'
4. karakter: 'i'
5. karakter: 'h'
6. karakter: 'z'
7. karakter: 'a'
---BURDAYIM
>>> print("|%-15s|"%"istihza")		negatif, sola yaslamak için
|istihza        |
---
>>> metin="gel %(bura)s gel %(bura)s olmamı?"
>>> print(metin%{"bura":"Antalya"})
gel Antalya gel Antalya olmamı?
---
#Python programlama dilinde bir fonksiyonu kullanışlı hale getirme işlemine "çağırma", bir sınıfı
#kullanışlı hale getirme işlemine de "örnekleme" (instantiate) diyoruz.
---
isimli parametre(mesela sep, end...), isimsiz parametre, varsayılan değerli parametre(file,sep,end...)
print 256 tane parametre alabilirmiş
function definition/function call
#bir fonksiyonu tanımlarken belirlediğimiz adlara parametre, 
#aynı fonksiyonu çağırırken belirlediğimiz adlara ise argüman deniyor. 
#Python’da isimli bir parametrenin ardından sıralı bir parametre gelemez. Yani şu kullanım yanlıştır:
#kayıt_oluştur(soyisim="Öz", isim="Ahmet", "Debian", "Ankara")
---
def kur(kurulum_dizini="/usr/bin"):
	print("Program {} dizinine kuruldu!".format(kurulum_dizini))
---
def kur(kurulum_dizini=" "):
	if not kurulum_dizini:
		print("LÜtfen bir dizin girin: ")
	else:
		print("Dizininiz: {}".format(kurulum_dizini))
---
def fonksiyon(**kwargs):			#sınırsız sayıda isimli parametre = sözlük. EDIT: args ve kwargs çok hoşuma gitti
    print(kwargs)
fonksiyon(isim="Ahmet", soyisim="Öz", meslek="Mühendis", şehir="Ankara") 	output dict oluyo
---
def fonksiyon(*args):			#sınırsız sayıda isimsiz parametre			output tuple oluyo
    print(args)
fonksiyon(1, 2, 3, 4, 5)
---
def kayıt_oluştur(**bilgiler):
    print("-"*30)
    for anahtar, değer in bilgiler.items():
        print("{:<10}: {:>11}".format(anahtar, değer))
    print("-"*30)
kayıt_oluştur(ad="Fırat", soyad="Özgül", şehir="İstanbul", tel="05333213232")
---
def karşılık_bul(*args,**kwargs):		# karşılık_bul('..','..',**sozluk) şeklinde kullanılır
	for sözcük in args:
		if sözcük in kwargs:
			print("{} = {} ".format(sözcük,kwargs[sözcük]))
		else:
			print("{} kelimesi sözlükte yok!".format(sözcük))
---
def bas(*args, start='', **kwargs):
    for öğe in args:
        print(start+öğe, **kwargs)									# anlamadım!!!!
																					
f = open("te.txt", "w")																				

bas('öğe1', 'öğe2', 'öğe3', start="#.", end="", file=f)
---
random.sample(liste,2)		# liste'den rastgele iki tane eleman seçer
random.shuffle(liste)		# liste'deki elemanları karman çorman eder ve liste değişmiş olur				
---
# Burda çok güzel yapılar var:															
import random
def sayı_üret(başlangıç=0, bitiş=500, adet=6):
    sayılar = set()
    while len(sayılar) < adet:
        sayılar.add(random.randrange(başlangıç, bitiş))
    return sayılar
#print(*sayı_üret(100, 1500, 20), sep='-')					isteğe bağlı, küme parantezini istemezsen	
---
import modül_ismi
p = modül_ismi.__file__
os.startfile(p)
---
#rumeli kavağı balıyla meşhur yer																			
#Python’da bir nesnenin değerini değiştirmekle, o nesneyi yeniden tanımlamak farklı kavramlardır.			EDIT: NEDEN????
---
>>> isim = 'Fırat'																								
>>> isim += ' Özgül'
>>> print(isim)
Fırat Özgül
#Burada yaptığımız şey, karakter dizisinin değerini değiştirmekten ziyade bu karakter dizisini yeniden tanımlamaktır.
#Çünkü bildiğiniz gibi karakter dizileri değiştirilemeyen veri tipleridir.
---
#isterseniz listeleri değişikliğe uğratabilirsiniz:
isim_listesi = []
def fonk():
    isim_listesi.extend(['Fırat Özgül', 'Orçun Kunek']) 
    return isim_listesi
print(fonk())
#ama .extend() yerine += olursa hata verir.																		 EDIT: NEDEN????
f'Sayıların toplamı { int(input("İlk sayıyı gir: ")) + int(input("İkinci sayıyı gir: ")) } eder.'
---
alfabe = "abcçdefgğhıijklmnoöprsştuüvyz" harf_listesi=list(alfabe); print(harf_listesi) her harften bölmek için
li=list()		#boş liste oluşturur
>>> list(range(2))	#aslına burada yaptığımız şey range ifadesini bir listeye çevirmekten ibarettir
[0, 1]				#bu arada range ifadesinin type'i "range"miş
---
>>> meyveler
['elma', 'armut', 'çilek', 'kiraz']
>>> meyveler[::-2]
['kiraz', 'armut']
---
liste[:]=5,6,8			#yeniden tanımlamaya gerek olmadan içeriğini değiştirdik
---
Şunların hepsi aynı işi görür:
1) liste=list(range(1000))				173 ms ± 3.26 ms per loop
2) 
liste = []								851 ms ± 23.3 ms per loop
for i in range(1000):
	liste+=[i]
3)
liste = [i for i in range(1000)]		387 ms ± 9.99 ms per loop
---
liste2=liste[:]															# işe yarayabilir. 2D listede aynısını yaptım oldu
#kopyalama ama aynı id'ye sahip olmadığı için ilkini değiştirince ikincisinin de değişmemesi
Eğer liste2=liste1 yaparsak list mutable(değiştirilebilir) bir veri tipi oldupu için ikisi de aynı anda değişir
---
liste = [i for i in range(1000) if i % 2 == 0]
[i for i in dir(tuple) if "_" not in i]				#demetlerin işe yarar metotlarını görmek için
---
liste = [[1, 2, 3],[4, 5, 6],[7, 8, 9],[10, 11, 12]]
İkisi aynı:
1)
tümü=[]											# ya TypeError: 'int' object is not iterable diyo
for i in liste:									# hata tümü+=z yapmaktaymış. tümü.append yapınca düzeldi. veya tümü+=[z] yapmalı
	for z in i:									# ama hatası belli değil
		tümü+=z									
2)
tümü = [z for i in liste for z in i]			
---
# eğer programın akışı esnasında üzerinde değişiklik yapmayacağınız veya değişiklik yapılmasını istemediğiniz 			
# birtakım veriler varsa ve eğer siz bu verileri liste benzeri bir taşıyıcı içine yerleştirmek istiyorsanız, 
# listeler yerine demetleri kullanabilirsiniz. Ayrıca demetler üzerinde işlem yapmak listelere kıyasla daha hızlıdır. 
# Dolayısıyla, performans avantajı nedeniyle de listeler yerine demetleri kullanmak isteyebilirsiniz. 	
# elbette bir araya topladığınız veriler üzerinde sık sık değişiklikler yapacaksanız 
# demetler yerine listeleri tercih etmelisiniz.
bu tanımlamak yerine değişiklik yapmanın ehemmiyeti harcanan zamandan geliyo heralde. evet baya farkediyo. yani
---
# sayılar üzerinde döngü kurulabilen bir veri tipi olmadığı için list() fonksiyonuna parametre olarak atanamaz.		
# TypeError: 'int' object is not iterable hatası verir
---
liste += [7] ile liste = liste + [7] farklı şeyler; ikincisi yeniden tanımlamak oluyor
from time import sleep
işletim_sistemleri.extend(platformlar)
liste.insert(1, "erik")
liste.remove("elma")
---
f=open("deneme.txt","r")
içerik = f.readlines()
içerik.insert(1,"Ferhat Yaz\n")
g=open("deneme.txt","w")
g.writelines(içerik)
g.close(); f.close()
---
print(*reversed(meyveler))				veya
list(reversed(meyveler))												
Şu da listeyi direk değiştirmesiyle pratik ve güzel: meyveler.reverse()	
---
liste.pop(1) parametresiz olarak kullanıldığında son öğesini ekrana basar ve siler						
üyeler.sort() veya üyeler.sort(reverse=True)# bu direk listeyi değiştiriyo
sorted()									# bu listeyi değiştirmiyo, sort edilmiş listeyi return ediyo. süreleri aynı gibi
---
#Henüz incelemedim ama amaç sort() metodunun Türkçe harfleri de düzgün bir şekilde 							
#sıralayabileceğini göstermekten ibaret.
harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
çevrim = {harf: harfler.index(harf) for harf in harfler}
isimler = ["ahmet", "ışık", "ismail", "çiğdem", "can", "şule"]
isimler.sort(key=lambda x: çevrim.get(x[0]))
print(isimler)														yukarda sorted ile yapılanı var
---
liste = ["elma", "armut", "elma", "çilek"]																	
liste.index("armut") = 1
liste.count("elma") = 2
liste.clear() 		#içeriğini boşaltır
---
liste1 = ["ahmet", "mehmet", "özlem"]
Üç kopyalama yöntemi: (pass by reference olmayan, farklı id'ye atama yapan kopyalama yöntemleri)
liste2 = liste1[:]		liste2 = list(liste1)		liste2 = liste1.copy()
---
os.getcwd()		os.makedirs('DATA') os.name		'nt' veya 'posix'										
subprocess.call('notepad.exe')
import webbrowser as web; web.open("istihza.com")															
os.listdir() veya ('.') o klasörü, ".." bir üst klasördeki dosyaları listeler.
---
i=1
for filename in os.listdir():
    os.rename(filename, str(i)+") "+filename)
    i+=1
print(os.listdir())								# çok iyi ya elh
---
from os import path as p
Yıldızlı içe aktarma işlemleri ancak modül seviyesinde, yani global isim alanında gerçekleştirilebilir.
Yani mesela def içinde "from sys import *" yazma	# EDIT: dert etme zaten yazılmıyo
---
from sys import * # modül içindeki bütün isimleri mevcut ortama ‘boşaltmış’ oluyoruz (ismi "_" ile başlayanlar hariç)
---
# Python’daki bütün modüller Python programlama dili ile yazılmamıştır. Bazı modüller C ile yazılmıştır.
# Dolayısıyla C ile yazılmış bir modülün .py uzantılı bir Python dosyası bulunmaz. Mesela sys böyle bir modüldür.
# Dolayısıyla bu modülün bir __file__ niteliği de bulunmaz
---
from distutils import sysconfig
sysconfig.get_python_lib()			#site-packages klasörünün adresini gösterir
---
sys.path.remove('C:\\Users\\emre\\Desktop')	veya  daha pratiği: sys.path.pop() veya sys.path.pop(9)
# Python, içe aktarmak istediğimiz bir modülü bulabilmek için dizinleri ararken sys.path listesindeki dizin adlarını 
# soldan sağa doğru okur. Modül dosyasını bulduğu anda da arama işlemini sona erdirir ve modülü içe aktarır...
# ... Eğer siz içe aktarma sırasında bir dizine öncelik vermek isterseniz o dizini append() metoduyla 
# sys.path listesinin sonuna eklemek yerine, insert() metoduyla listenin en başına ekleyebilirsiniz
---
sözlük = {"kitap"      : "book",
          "bilgisayar" : "computer",
          "programlama": "programming"}
def ara(sözcük):
    hata = "{} kelimesi sözlükte yok!"
    return sözlük.get(sözcük, hata.format(sözcük))
def ekle(sözcük, anlam):
    mesaj = "{} kelimesi sözlüğe eklendi!"
    sözlük[sözcük] = anlam
    print(mesaj.format(sözcük))
---
importlib.reload(sözlük)
---
# modülden silinen öğeler, reload() ile yeniden yüklendikten sonra dahi kullanılır durumda kalmaya devam eder.
# ayrı bi klasör ise: python setup.py install
---
# yazdığın modülün en başına şunu yazınca: __all__ = ['fonk1', 'fonk2', 'fonk3'] from modül import * komutu ile sadece o fonksiyonlar
# içe aktarılır. Yani import modül ve dir(modül) dersen onların dışında bişey göremezsin 
# Ancak from modül import fonk tarzındaki aktarmada bu __all__ komutu işe yaramaz.
# Ama tabi o durumda önceden fonk diye bi fonksiyon olduğunu bilmek gerekiyor.
İlginç bir özellik: dir(__import__("random")) deyince çalışıyor ama random normal olarak import edilmiş gibi olmuyor
open("den.txt","w").write("merhaba"); __import__("subprocess").call("notepad.exe den.txt") # çok güzel
[*kümeler] == kümeler 	#basit ama güzel. Diğer çeşidi: 	
küme1.intersection(küme2)
Bütün modüllerde ortak olan beş nitelik: __doc__ __name__ __loader__ __spec__ __package__
#Teknik dilde, üç tırnak içinde gösterilen karakter dizilerine belge dizisi (docstring) veya belgelendirme dizisi
# (documentation string) adı verilir.
İlginç: os.__doc__ \n'lerle birlikte düzgün olmayan; print(os.__doc__) ise düzgün string verdi
---
modüller = ["os", "sys", "random", "subprocess"]																		
def kesişim_bul():
    kümeler = [set(dir(__import__(modül))) for modül in modüller]
    return set.intersection(*kümeler)
---
# dosya işlemleri sırasında bu “w” kipini kullanırken dikkat ediyoruz ve 
# disk üzerinde var olan dosyalarımızı yanlışlıkla silmiyoruz.			EDIT: """ooo çok önemli"""
Dosyayı okuma modunda açmak için "r" yazmaya gerek yok
read() tamamını, readline() satır satır, readlines() ise satır satır tamamını liste olarak verir
# İlginç: bir dosya açıldıktan sonra programda beklenmeyen bir hata gerçekleşirse, 
# programınız asla close() satırına ulaşamayabilir. Bu durumda da açılan dosya kapanmadan öylece bekler.
EDIT: kapanmasa nolur ki?
---																														
try:
    dosya = open("dosyaadı", "r")
    ...burada dosyayla bazı işlemler yapıyoruz...
    ...ve ansızın bir hata oluşuyor...
except IOError:
    print("bir hata oluştu!")
finally:											# çok hoş elh
    dosya.close()
													# veya daha pratiği:
with open("dosyaadı.txt","r") as dosya:
	print(dosya.read())
---
f = open("python.txt","r")
f.read()
f.seek(0) 		# istediğin byte'a dönebilirsin
f.tell()		# o sırada kaçıncı byte'ta olduğunu söyler
---
with open("fihrist.txt","r+") as f:
	veri = f.read()
	f.seek()
	f.write("something"+veri)
---
with open("fihrist.txt","r+") as f:
	veri = f.readlines()
	veri.insert(2,"Sedat Köz\t: 0322 234 45 45\n")
	f.seek(0)
	f.writelines(veri)
Burada write() metodunu kullanmadık. Çünkü write() metodu sadece karakter dizilerini yazabilir. writelines() ise
bize liste yazma imkanı verir. Eğer mutlaka write() metodunu kullanacaksak for döngüsü kurmamız gerekir:
with open("fihrist.txt","r+") as f:
	veri = f.readlines()
	veri.insert(2, "Sedat Köz\t: 0322 234 45 45\n")
	f.seek(0)
	for öğe in veri:
		f.write(öğe)
Aslında bu yöntem biraz güvensiz çünkü eğer bu işlemlerin herhangi bir aşamasında bir hata oluşursa, 
bütün değişiklikleri dosyaya işleyemeden dosya içeriğini tümden kaybedebiliriz. Okuma ve yazma işlemini
ayrı ayrı yapmak daha güvenli:
with open("fihrist.txt","r") as f:
	veri = f.readlines()
with open("fihrist.txt","w") as f:
	veri.insert(2,"Sedat Köz\t: 0322 234 45 45\n")
	f.writelines(veri)
Ayrıca bundan önceki kodda (heralde) dosya r+ modunda açıldığı için f.seek(0) yapmaya ihtiyaç oluyor yoksa
veri listesini dosyanın sonuna ekliyor. Ama bu sonuncuda gerek yok çünkü dosya w modunda açıldığı için 
ilk önce dosyanın içeriğini tamamen siliyor.
---
cmd'de python'ın help komutu çalışmıyodu, system32'yi her iki path'e ekledim düzeldi
# bir değişkeni def içinde değiştirmek istersen def içinde global kullanman lazım.
# Veya fonksiyonu şöyle tanımla: def artır(n): Sonra da artır(sayaç) diye çağır
 sınıf adlarında, yukarıda olduğu gibi büyük harf kullanmak ve birden fazla kelimeden oluşan sınıf adlarının
 ilk harflerini büyük yazıp bunları birleştirmek adettendir. Yani mesela: class ÇalışanSınıfı:
# class'ta tanımlanan değişkenlere sınıf nitelikleri denir (class attribute)
fonksiyonlar çağrılmadan çalışmaz ama sınıflar çalışır
# nesne tabanlı programlama yaklaşımı, özellikle birtakım ortak niteliklere ve
# davranış şekillerine sahip gruplar tanımlamak gerektiğinde son derece kullanışlıdır.
# Sınıfların önemli bir özelliği çağrılmaya gerek olmadan çalışmasıdır. Mesela class ... print(...) dersek basar
# Örnek niteliklerinde ise durum farklı. Örnekleme yapılmadan class çalışmaz
---
# ahmet.kabiliyetleri yazınca ilk önce self.kabiliyetleri" örnek niteliğini, onu bulamazsa "kabiliyetleri" sınıf niteliğini arar.
Eğer yanlışlıkla veya bilerek sınıf ve örnek niteliklerine aynı class içinde aynı isim verdiysen 
sınıf niteliğine erişmek için sınıf ismini, örnek niteliğine erişmek için örnek ismini kulanıyoruz
Ancak elbette, aynı adı taşıyan bir sınıf niteliği ile bir örnek niteliğini aynı sınıf içinde tanımlamak
daha baştan iyi bir fikir değildir
# Sınıf niteliklerinin özelliği, o sınıfın bütün örnekleri tarafından paylaşılıyor olmasıdır. 
# Yani herhangi bir örneğin bu nitelik üzerinde yaptığı değişiklik, öteki örneklere de yansıyacaktır.
Bir sınıf içinde örnek metotlarına ve örnek niteliklerine hep self kelimesi aracılığıyla erişiyoruz
# Eğer düzenli ifadelerden tek beklentiniz 	bir karakter dizisinin en başındaki veriyle eşleştirme  işlemi
# yapmaksa, split() veya startswith() metotlarını kullanmak çok daha mantıklıdır çünkü bunlar match() 
# metodundan çok daha hızlı çalışacaktır. Zaten match() stringin sadece en başına bakar 
---
for f in dosyalar:																								
    okunan = open(f, 'rb').read(10)
    if okunan[6:11] in [b'JFIF', b'Exif']:
        print("Evet {} adlı dosya bir JPEG!".format(f))
	elif okunan[:8] == b"\211PNG\r\n\032\n":
        print("{} adlı dosya bir PNG!".format(f))
	elif okunan[:3] == b'GIF':
        print("{} adlı dosya bir GIF!".format(f))
	elif okunan[:2] in [b'II', b'MM']:
        print("{} adlı dosya bir TIFF!".format(f))
	elif okunan[:2] in [b'BM']:
        print("{} adlı dosya bir BMP!".format(f))
    else:
        print("{} JPEG değil!".format(f))		##buranın ne işe yaradığı anlaşılıyor##
---
"{0} {1} ({1} {0})".format("Fırat", "Özgül")	istediğin sırada yerleştir
print("|{:>15}|".format("istihza"))
print("{:o}".format(65))			# 10'lu düzendeki sayıyı 8'li düzendeki sayıya çevirir
print("{:x}".format(65))			# 10'lu düzendeki sayıyı 16'li düzendeki sayıya çevirir
print("{:X}".format(65))			# Aynı. tek farkı bunun büyük harfle temsil etmesi
"{:b}".format(2)					# binary'ye
print("{:.2f}".format(50))																					
"{:,}".format(1234567890)			# basamaklara ayırır
bin(2)	ve bin(2)[2:]				# string veriyor  dikkat et
hex(10)
int('7bc', 16) 						# cevap: 1980
sayı.bit_length()		veya 		(10).bit_length()
(4.5).as_integer_ratio()
(12.0).is_integer()	
divmod(10,2)																										
sum(a,10)							# a = [10, 20, 43, 45 , 77, 2, 0, 1]
---
sayı_sistemleri = ["onlu", "sekizli", "on altılı", "ikili"]
en_uzun = len(max(sayı_sistemleri, key=len))
print(("{:^{aralık}} "*len(sayı_sistemleri)).format(*sayı_sistemleri, aralık=en_uzun))
for i in range(17):
    print("{0:^{1}} {0:^{1}o} {0:^{1}x} {0:^{1}b}".format(i, en_uzun))
---
Ancak örnek metotlarına ve örnek niteliklerine atıfta bulunmak için örnek adlarını kullanmak, 
sınıf metotları ve sınıf niteliklerine atıfta bulunmak için ise sınıf adlarını tercih etmek daha akıllıca olabilir.
# Python’da herşey bir nesne olduğunu bilmek, muhatap olduğunuz programlama dilini ve onun kabiliyetlerini tanımak açısından
# önemlidir. Python’da her şeyin bir nesne olduğunu anladığınız anda, {'a': 0, 'b': 1} gibi bir kodla yalnızca
# basit bir sözlük tanımlamadığınızı, bunun arkaplanında, bu sözlükle etkileşim kurmanızı sağlayacak
# koca bir mekanizma bulunduğunu bilirsiniz.
Bu fonksiyon toplam iki parametre alıyor: ölçüt ve değer. Bu parametrelerin öntanımlı değerlerini 
None olarak belirledik. Böylece bu fonksiyonu herhangi bir argüman vermeden de çalıştırabileceğiz. (süper) EDIT: hakkaten
#shutil.move(src,dst,copytree="copy2")
for i in os.listdir():
    if i.startswith("Unders"):
            import shutil; shutil.move(i,"pid")		# çalıştı elh
---
elhamdülillah bi adedi zerratil kainat: 
def fonk(output_path = None) dedikten sonra:	# yav arkadaş tmm hoş ama öyle yapmaya ne gerek var, direk parantez
output_path = output_path or os.getcwd()		# içinde output_path = os.getcwd() diyebilirdim. Ama başka yerde lazım olabilir doğru
------------------
elhamdülillah ya mp3'ü open'la istediğim yerden kestim, ne kadar kolaymış:
f = open('dua.mp3','rb')
ses = f.read()
s = open('dua_yeni.mp3','wb')
oran = (9*60+52) / (26*60+23) # istediğim parçanın bütün ses dosyasının uzunluğuna oranı
ses_yeni = ses[:int(len(ses)*oran)]
s.write(ses_yeni)
s.close()
f.close()
------------------
b = byte("ş","utf-8")	veya 32																							
# locale.getpreferredencoding()	
Önceki derslerimizde errors parametresinin hangi değerleri alabileceğini tartışmıştık.
Orada anlattığımız şeyler burada da geçerlidir.			"""Bu önceki derslere çalışmadım"""
b'\xc3\xbc'.decode("utf-8")		# bytes tipinin stringten farklı olarak sahip olduğu iki metottan biri
bytes.fromhex("c4b0")			# bu da diğeri
pdf = bytearray(b'PDF-1.7')
---
tarih ve saati düzgün bir şekilde görüntüler:
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
---
@property bezeyicisinin bir görevi de salt okunur,
yani kodları kullananların değiştirmesini istemediğimiz nitelikler oluşturmaktır
---
- Python’da bir değişkenin adını değiştirmeden o değişkene erişimi kontrol altına almak istediğimizde 
tek alt çizgi kullanmak tercih edilen bir yöntemdir.
# Python her ne kadar nitelikleri gizlememiz için bize özel bir mekanizma sunmuş olsa da bu niteliğe erişmemizi 
# tamamen engellemiyor, ancak ilgili sınıfı yazan kişinin niyetine saygı göstereceğimizi varsayıyor. (elh bu cümle için)
- Taban sınıf denen şey, birkaç farklı sınıfta ortak olan nitelik ve metotları barındıran bir sınıf türüdür.			
- pdfkit.from_url(input("url: "),r"C:\users\emre\desktop\\"+input("dosya ismi: ")+".pdf") (elhamdülillah)	
- bir kere yapılması yeterli olan işlemleri bir kereden fazla yapacak şekilde loop içine falan sokma! veya 
ilgili fonksiyonun outputunu bir değişkene atamak yerine o fonksiyonu gereksiz yere tekrar çağırarak ...
- python2 -m pip install ctype 
0535 646 65 05
- Bununla birlikte, birkaç koldan çalışan işlemler arasında tesanüd nasıl sağlanır, onu da bilmek gerekiyor.
Threading bir yandan çay demlenirken, diğer yandan kahvaltı hazırlamak demektir, multiprocessing ise, siz kahvaltı hazırlarken,
 başka birinin de sofrayı hazırlaması gibidir.

Threading kullanırken, tek bir işlem farklı kollardan iki işi aynı anda yürütür. Multiprocessing'de ise, iki ayrı işlem vardır.

Threading hakkında daha basit bir örnek vermek gerekirse, iş başvurusu yapacağınızı düşünün. Başvurmak istediğiniz 5 farklı iş yeri
 var. 2. iş yerine başvurmak için, 1. iş yerinden size dönmelerini beklemek istemezsiniz, çünkü ne zaman size dönüleceğini, hatta
 dönülüp dönülmeyeceğini bilmiyorsunuz. Bu sebeple, daha bir yerden cevap gelmeden, diğer işyerlerine de başvuru göndermek istersiniz,
 böylece en kısa sürede iş bulabilirsiniz. 
---
>>> def foo(x=[]):																						
...     x.append(1)
...     print x
... 
>>> foo()
[1]
>>> foo()
[1, 1]
>>> foo()
[1, 1, 1]							
											yerine: (önceki nasıl öyle sonuç veriyo???)
>>> def foo(x=None):
...     if x is None:
...         x = []
...     x.append(1)
...     print x
>>> foo()
[1]
>>> foo()
[1]
--------------------
from collections import Counter																							
my_list = [1,3,4,1,4,6,12,3,4]
c = Counter(my_list)
c[1]				#1 kaç kere tekrar edilmiş olduğunu gösterir. Yani 1 denilen şey index değil, key
c.most_common(2)	#en çok kullanılan 2 key
list(c)				#sadece keys, yani list(c.keys()) ile aynı
set(c)				#sadece keys, yani set(c.keys()) ile aynı
dict(c)				#key-value değerlerinin sözlüğe çevrilmiş hali
--------------------
from collections import defaultdict
my_dict = defaultdict(lambda: 'Not known')	#Normalde aradığın key dictionary'de yoksa hata döndürür, ama bunda default değer atıyo
--------------------
from collections import namedtuple																									
Person = namedtuple('Person',['name','age','weight','height'])	
me = Person('Emre',25,56,1.72)										
bmi = me.weight / me.height ** 2
--------------------
a=[int(x) for x in input().split()]		# to take a list or an array input in a single line
---
from urllib.request import urlopen																					BURDAYIM
html = urlopen(input('url: ')).read().decode('utf-8')
with io.open('amazing.html','w',encoding="utf-8") as f:f.write(html)
---
a = [1, 2, 3]; x, y, z = a
a = ["Code", "mentor", "Python", "Developer"]; " ".join(a)
list(zip(List_1,List_2)) output = [('a', 'p'), ('b', 'q'), ('c', 'r'), ('d', 's')]
list(itertools.chain.from_iterable(a)) # Convert it to a single list without using any loops. (ama 3D'yi tek seferde yapmadı.)
code.interact(local=globals()) # bunu main loop'undan önce koy
merged_dict = {**dict_1, **dict_2}
---
d = [[]]  * 5
d[0].append(25)
print d
e  = [[] for _ in xrange(5)]
e[0].append(25)
assert e == d
---
a, _, b = (1, 2, 3)
a, *_, b, c = (1, 2, 3, 4, 5, 6)
---
timeit.timeit(stmt=function_to_be_tested, number=2000000)
assert kullanabilirsin: assert boy == 5, 'boy yanlış'
---
>>> def f(a, b, *, c='x', d='y', e='z'):
...     return 'Hello'
---

python deneme.py & # aynı terminalde birden fazla script çalıştırmak için
---
>>> import urllib
>>> site = urllib.urlopen('https://github.com/mit-cml/appinventor-sources/archive/master.zip')
>>> meta = site.info()
>>> meta.getheaders("Content-Length")
['326259490']
---
Şu işe bak ya onPreExecute'un o'sunu büyük yazdığım için hata verdi ona uğraştım. elh buldum ama
---
ilginç bi tespit:
çok acayip ya.demek ki bi veriyi alıp plot çizince böyle çiziyo nedense.
demek ki plottan x-y extract ederken dikkatli olmak lazım
>>> dizit[1000]
-2.1316282072803006e-13 (halbuki 0 çıkması lazım, bu bi plota ait, sinc'in t ekseninin tam ortasındaki değer)
t = np.arange(-10,10,0.01)
y = np.sinc(t)
ciz = plt.plot(t,y)	#list
>>> type(ciz[0])
<class 'matplotlib.lines.Line2D'>
veri = ciz[0].get_data() #tuple. len(veri) = 2. ilki t diğeri y
>>> dizit = veri[0]   #<class 'numpy.ndarray'>
>>> diziy = veri[1]	  #<class 'numpy.ndarray'>
>>> dizit[1300]
2.999999999999723
>>> veri[0][1300]
2.999999999999723
>>> ciz[0].get_data()[0][1300]
2.999999999999723
>>> plt.plot(t,y)[0].get_data()[0][1300]
2.999999999999723
----------------------------------
vaaaay:
>>> np.where(diziy.round(2)==0)	# y'yi 0 yapan index değerlerini bulmak için. yukarıdaki sıkıntıdan dolayı round kullandım
(array([  94,   95,   96,   97,   98,   99,  100,  101,  102,  103,  104,
        105,  295,  296,  297,  298,  299,  300,  301,  302,  303,  304,
        496,  497,  498,  499,  500,  501,  502,  503,  697,  698,  699,
        700,  701,  702,  898,  899,  900,  901, 1099, 1100, 1500, 1501,
       1699, 1700, 1701, 1702, 1898, 1899, 1900, 1901, 1902, 1903],
      dtype=int32),)
>>> dizit[_]
array([-9.06, -9.05, -9.04, -9.03, -9.02, -9.01, -9.  , -8.99, -8.98,
       -8.97, -8.96, -8.95, -7.05, -7.04, -7.03, -7.02, -7.01, -7.  ,
       -6.99, -6.98, -6.97, -6.96, -5.04, -5.03, -5.02, -5.01, -5.  ,
       -4.99, -4.98, -4.97, -3.03, -3.02, -3.01, -3.  , -2.99, -2.98,
       -1.02, -1.01, -1.  , -0.99,  0.99,  1.  ,  5.  ,  5.01,  6.99,
        7.  ,  7.01,  7.02,  8.98,  8.99,  9.  ,  9.01,  9.02,  9.03])
yav arkaadaş nedense doğru sonucu 3'te veriyo. sonra düşün!!!
>>> np.where(diziy.round(3)==0)
dizit ve diziy yanlış sonuçlar veriyodu, uzun incelemeler sonucu en sonunda dizit vs diziy'i plot edince anladım.
meğer expanded'mış sinc fonksiyonu
----------------------------------
import numpy as np, matplotlib.pyplot as plt, control as ct
def bode_ciz(k1=-0.49,k2=1):
	# (if hop = 1)
	sys=ct.tf([k2],[1,-k1])
	mag,phase,omega = ct.bode(sys,dB=False) #eşitlemeye gerek yok aslında
	plt.show(block=False)
	return mag,phase,omega 
# fonksiyonu çağırırken bode_ciz(); diye çağır yoksa bir sürü data print ediliyor
----------------------------------
git clone ...git
---
git git reset HEAD~
--- 
git pull origin master
---
git add yeni.py				
git rm file1.txt			
git rm --cached file1.txt	# if you want to remove the file only from the Git repository and not remove it from the filesystem
---
git commit -m 'deneme'
git push origin master # git push da yetiyo aslında, belki farklı branchlar olduğu zaman 'origin master'a gerek oluyodur
https://rogerdudler.github.io/git-guide/
-----------------------------------
# tf'nin pole veya zero'larını bulmak için kullanılabilir
GH -> control.tf or control.matlab.tf object
den = GH.den[0][0]
den = list(den)
np.roots(den) 
------------------------------------
import matplotlib.pyplot as plt
import scipy.io as sio
mat = sio.loadmat('SysIdDataExp2.mat')		# bunun source code'una bak python bunu nasıl açıyo merak ettim
mat = list(mat.values())
t = mat[-1]
out = mat[-2]
inp = mat[-3]
fig,(output,input) = plt.subplots(2,1)#sharex=True)
input.plot(t,inp)
plt.suptitle('Experimental data from a bump test ')
input.set(xlabel='Time (sec)', ylabel='Input\nVoltage (Volts)')
output.plot(t,out)
mplcursors.cursor(multiple=True)
output.set(ylabel='Output\nTemperature (Celcius)')
plt.show(block='False')
--------------------------------------
result_2 =  [list(i) for i in itertools.product(teta_degree,t,x_values)] #fayda vermedi, even a bit worse 
--------------------------------------



BURDAYIM kelimesini arat.
TEKRAR BAK kelimesini arat.









