# COMMEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEENT!!!!!!!!!!
# When writing code, simultaneously try on for a small object. 
#  
import keyword		keyword.kwlist
del degisken
#sonuc=gün * (gidiş_ücreti + dönüş_ücreti) değeri gün'ün değerini değiştirince değişmedi,
#tekrar atamak gerekiyo!!!
pow(3,2,4)=1
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
print(*"galatasaray",sep="") 		# karakter dizisini tek tek öğelerine ayırıp
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
#eval() ve exec() hakkındaki güvenlik açığı meselesine dikkat (security bug veya security flaw)
bunlar işe yarar fonksiyonlar
---
>>> kartvizit="""
... istihza aonim şikeri
... fırat özgül
... 9089
... """ dedikten sonra komut satırına kartvizit yazıp enterlamak ile print(kartvizit) demek farklı sonuç veriyor!!!
ayrıca şu """ alt satıra geçme konusunda çok iyi """
---
if'leri iç içe kullanmak yerine and filan kullan					
note>=90 and note<=100		ile 		note>=90<=100 aynı;		90<=note<=100 ile zaten aynı
a-=5 işlemi normaline göre daha hızlı çalışır
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
#bir Python programının nasıl çalıştığını anlamanın en iyi yolu, program içinde uygun yerlere 
#print() fonksiyonları yerleştirerek arka planda hangi kodların hangi çıktıları verdiğini izlemektir.
__import__("os").system("dir")
---
print(*range(10))
---
print(repr(karakter_dizisi))	#çıktıdaki \n'leri görebilmek için	# TEKRAR BAK
---
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
os.startfile("C:\\users\emre\desktop\pardus-hastane.png")		# veya (r"C:\users...)
Please note that on unix or mac, there should be a different code
So, you should be aware of that the code you wrote may not be working on other OS
---
chromePath	= r'C:\Program Files\Google\Chrome\Application\chrome.exe'
png			= r'C:\users\emre\desktop\vaay.png'
subprocess.Popen("%s %s" % (chromePath,png))
#bu çok hoşuma gitti: evet tasdik ediyorum. (png'yi chromePath ile açıyo) Emre
# edit: (29.6.20) neden %s ile yazıldığını düşünürken bunun aslında cmd'ye yazılan kodla atynı olduğunu farkettim:
sb.Popen(chromePath + ' ' +png)
---
#yazdığınız programda mutlaka ama mutlaka işletilmesi gereken bir kısım varsa, o kısmı finally... bloğu içine 
#yazabilirsiniz. Mesela eğer dosya üzerinde işlem yapılırken bir hata ile karşılaşılırsa 
#dosyamızı kapatma işlemini gerçekleştirdiğimiz bölüme hiç ulaşılamayabilir.
---
raise Exception("Bu programda 23 sayısını görmek istemiyorum!")		
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
# her harfi bir sayıya atayarak yaptı				yukarda listelerin sort() metodu ile yapılanı var
---
print("http://",i) ifadesinin print("http://"+i) ile aynı sonucu vermesi için sonuna ,sep="" koymak lazım
karakter dizileri değiştirilemeyen (immutable) bir veri tipidir.
dir(complex)
---
major=sys.version_info[0]
minor=sys.version_info[1]
micro=sys.version_info[2]
print(major+minor+micro)
# bu yöntem bütün python sürümlerinde çalışır
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
f'Sayıların toplamı { int(input("İlk sayıyı gir: ")) + int(input("İkinci sayıyı gir: ")) } eder.'						#iyiymiş
---
alfabe = "abcçdefgğhıijklmnoöprsştuüvyz" harf_listesi=list(alfabe); print(harf_listesi) her harften bölmek için
li=list()		#boş liste oluşturur
>>> list(range(2))	#aslında burada yaptığımız şey range ifadesini bir listeye çevirmekten ibarettir
[0, 1]				#bu arada range ifadesinin type'i "range"miş
---
def ex(val,list=[]):
    list.append(val)
    return list
list1 = ex(10)
list2 = ex(123,[])
list3 = ex('a')
# çok ilginç: ex fonksiyonu her çağrıldığında list değişkeni belirtilmemişse tekrar tekrar kullanılır. Bu durumun önüne geçmek için
# fonksiyonun içinde list=None dendikten sonra şunlar yazılmalı:
if list is None:
	list = []
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
EDIT:
4)
%timeit k=np.arange(1000)				14.4 µs ± 50.4 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
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
işletim_sistemleri.extend(platformlar)
liste.insert(1, "erik")
liste.remove("elma")
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
from sys import * # modül içindeki bütün isimleri mevcut ortama ‘boşaltmış’ oluyoruz (ismi "_" ile başlayanlar hariç)
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
- python2 -m SimpleHTTPServer
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
>>> def foo(x=[]):								# bu nasıl oluyo lan 																	
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
# fonksiyonu çağırırken bode_ciz(); diye çağır yoksa bir sürü data print ediliyor
def bode_ciz(k1=-0.49,k2=1):
	# (if hop = 1)
	sys=ct.tf([k2],[1,-k1])
	mag,phase,omega = ct.bode(sys,dB=False) #eşitlemeye gerek yok aslında
	plt.show(block=False)
	return mag,phase,omega 
---
scipy.signal.lsim veya control.matlab.lsim ben ikincisini kullandım aşağıda
yout, T, xout = lsim(T,e,d[0])
# d[0] dediğim herhangi bir time vektörü, e input, T de transfer function
----------------------------------
git clone ...git
---
git add something.py
git commit -m some_msg
git reset HEAD~
git push
Everything up-to-date
--- 
git pull origin master
# sadece git pull dedim oldu
---
git add yeni.py				
git rm file1.txt			
git rm --cached file1.txt	# if you want to remove the file only from the Git repository and not remove it from the filesystem
---
git rm -r *.png 			# yukarıdaki gibi -r olmadan ne farkı var bilmiyorum
git commit -m 'deneme'
git push origin master # git push da yetiyo aslında, belki farklı branchlar olduğu zaman 'origin master'a gerek oluyodur
https://rogerdudler.github.io/git-guide/
---
git log # şimdiye kadar yapılan commitler
git log --oneline # muhtasar hali, sadece isimler
git whatchanged
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
# .sort() dediğin şeyin output'u none olduğu için bu satır her zaman True verir:
print('aymi mi: ',np.array_equal(final_result.sort(),result1.sort()))
# See Also:
# allclose: Returns True if two arrays are element-wise equal within a tolerance.
# array_equiv: Returns True if input arrays are shape consistent and all elements equal.
--------------------------------------
In [17]: 8==8.0000000000000001
Out[17]: True
--------------------------------------
dir(__builtins__) # builtin fonksiyon ve exception'lar
vars(globals()['__builtins__']) # yukardakinin baya ayrıntılı hali sanki
dir() # o sırada namespace'te tanımlı değişken, fonksiyon vs isimleri

--------------------------------------
python setup.py install --user
#kalıcı olarak dev version'ı yüklemek için
--------------------------------------
# 8.7 saniye
# çok ibretlik: stackoverflow'a sordum, birinin (onun da dediği gibi çok etkilemeyeceğini
# düşünsem de) dediğini yaparak tan ile cos'u inner loop'tan outer loop'a alınca
# bu üç for'lu blok 4.5 saniyeden 0.6 saniyeye indi (100-10'da)
---
# saçmalığa gel. demek ki 91 işe yaramıyor. çünkü sayılar çok küsuratlı, round etmek lazım
---
result1.sort()  # iç içe olan listeyi sort etmek saçma bi sonuç verdi
---
bune = list(result1 for result1,_ in groupby(result1))	# you have to sort the data before using groupby 
---
son=sorted(son)	# nasıl sort ediyo anlamadım. edit: anladım. ilk önce her elemanın ilk elemanına bakıyo, sonra ihtiyaç olursa ikinciye bakıyo
---
# elhamdülillah ya for loop yerine np array kullanınca 0.8591713905334473'ten 0.03124380111694336'a düştü 100-5'te
---
Like image processing with Pillow, high-performance machine learning with scikit-learn, or micro-threading with greenlet. 
But how can these packages do things that aren’t possible in regular Python?

The answer is that they include extension modules, sometimes called native modules. Unlike Python modules, these are not .py files
containing Python source code – they are .pyd files that contain native, platform-specific code, typically written in C. 
In many cases the extension module is an internal detail; all the classes and functions you’re actually using have been written 
in Python, but the tricky parts or the high-performance parts are in the extension module.
...
As a Windows user, you’re probably used to downloading programs that are ready to run. This is largely due to the very impressive 
compatibility that Windows provides – you can take a program that was compiled twenty years ago and run it on versions of Windows 
that nobody had imagined at that time. However, Python comes from a very different world where every single machine can be different 
and incompatible. This makes it impossible to precompile programs and only distribute the build outputs, because many users will not 
be able to use it. So the culture is one where only source code is distributed, and every machine is set up with a compiler and the 
tools necessary to build extension modules on install. Because Windows has a different culture, most people do not have 
(or need) a compiler.

The good news is that the culture is changing. For Windows platforms, a package developer can upload wheels of their packages 
as well as the source code. Extension modules included in wheels have already been compiled, so you do not need a compiler on the 
machine you are installing onto.
-------------------------------------
In [71]: print("%.e" % .000009878)		# scientific notation print
1e-05
In [72]: print("%e" % .000009878)
9.878000e-06
In [73]: print("%.2e" % .000009878)
9.88e-06
-------------------------------------
yav şu işe bak ipython --pylab diye bişey varmış yeni öğreniyorum. plot deyince show'a gerek kalmıyo ve 
xlim gibi şeyleri hemen tesir ettiriyo plot üzerinde, kapatıp açmadan. matlab gibi
tutor diyo ki: 
"In all examples, this book will assume that you are using a Unix-based computer:
either Linux or Macintosh. If you are using a Windows machine and are for some reason :)
unable or unwilling to upgrade that machine to Linux, you can still use Python on a
command line by installing the Python(x,y) package and opening an 'iPython' window." 
---
frequency, mic1, mic2 = loadtxt('microphones.txt', unpack = True)
---

-------------------------------------
myarray = numpy.array([[1, 2, 3], [4, 5, 6]])
rownames = ['a', 'b']
colnames = ['one', 'two', 'three']
mydataframe = pandas.DataFrame(myarray, index=rownames, columns=colnames)
mydataframe.one
mydataframe['one'] 																#bu iki misali hazmetmedim
---
myarray = numpy.array([1, 2, 3])
rownames = ['a', 'b', 'c']
myseries = pandas.Series(myarray, index=rownames)
---
data = data = pandas.read_csv(url,names=names)
# understand your data using descriptive statistics: 
data.shape
data.dtype
data.describe()		# her name'e ait count mean std min 25% 50% 75% max'leri veriyo
data.head()			# to look at the first few rows.
data.corr()			# Calculate pairwise correlation between your variables. ama ne manaya geldiğini anlamadım
scatter_matrix(data)# anlamadım ne işe yaradığını
---
import csv
with open('library.csv','r') as f:
    r = csv.reader(f)
    for row in r:
        print(row)
---
myarray = numpy.array([[1, 2, 3], [4, 5, 6]])
rownames = ['a', 'b']
colnames = ['one', 'two', 'three']
mydataframe = pandas.DataFrame(myarray, index=rownames, columns=colnames)
---
"""dolaptaki ayvanın hoşuma gitmediğini, tadının pek sevilmeyeceğini söylememeliydim, gerçi belirttim ama 1 tane ayvaya bakarak
hüküm çıkartmış olmama rağmen bütün ayvalara ve dersanedeki herkese teşmil edildi halbuki günlersonra tekrar yedim busefer sevdim"""

-------------------------------------
%whos # you can see which variables are in memory
-------------------------------------
Fs,y = read('den.wav')
wav_dosyasi_as_byte = wave.open('den.wav')
nframes = wav_dosyasi_as_byte.getnframes()
frames = wav_dosyasi_as_byte.readframes(nframes)
wav_from_bytes = np.frombuffer(frames,'int')		# wav_from_bytes.shape = (93184,)  # plt.plot(wav_from_bytes) tamamı 0 gibi ?
# frombuffer metodunun dtype'ına dikkat etmezsen yanlış sonuç verir
# wav_from_bytes sadece bir channel'ı verdi gibi
wav_from_bytes_scaled = wav_from_bytes / 	 # niyeyse hayvan gibi büyük sayılar, halbuki şekli aynı. scale ettim
wh = np.isclose(wav_from_bytes_scaled,y0,rtol=100)
-------------------------------------
import matplotlib.pyplot as plt
fig = plt.figure()
plt.title('Digital filter frequency response')
ax1 = fig.add_subplot(111)

plt.plot(w, 20 * np.log10(abs(h)), 'b')
plt.ylabel('Amplitude [dB]', color='b')
plt.xlabel('Frequency [rad/sample]')

# ax2 = ax1.twinx()
# angles = np.unwrap(np.angle(h))
# plt.plot(w, angles, 'g')
# plt.ylabel('Angle (radians)', color='g')
plt.grid()
plt.axis('tight')
plt.show()
-------------------------------------
#bits_list = []
#for index in range():
#    bits = [index & (2 ** k) for k in range(8)]
#    bits_list.append(tuple((1 if b else 0) for b in bits))
#    to_byte = dict((bits, i) for i, bits in enumerate(bits_list))
-------------------------------------
# unutma: copy.deepcopy meselesi
-------------------------------------
k.shape = (5,2)		m.shape = (5,1)		k[:] = m	
# deyince array([[ 7,  7], [ 4,  4], [13, 13], [ 0,  0], [ 1,  1]]) oluyor
len()	ve .size da var
-------------------------------------
# ilginç bir broadcasting örneği:
x = np.arange(4)
xx = x.reshape(4,1)
xx
y([[0], [1], [2], [3]])
y = np.random.randint(1,10,5) 		# y = array([7, 6, 3, 6, 4])
xx+y
y([[ 7,  6,  3,  6,  4], [ 8,  7,  4,  7,  5], [ 9,  8,  5,  8,  6], [10,  9,  6,  9,  7]])
-------------------------------------
In [47]: %%timeit
    ...: newlist = [s.upper() for s in oldlist]
    ...:
    ...:
46.7 ms ± 261 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

In [48]: %%timeit
    ...: newlist = [s.upper() for s in old]
    ...:
    ...:
10.1 ms ± 52.4 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
#####	list comprehension list ile array'a göre daha hızlı. ilginç
--- # ikinci bir örnek:
In [49]: %%timeit
    ...: for word in oldlist:
    ...:     newlist.append(word.upper())
    ...:
55 ms ± 1.15 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

In [50]: %%timeit
    ...: for word in old:
    ...:     newlist.append(word.upper())
18 ms ± 1.03 ms per loop (mean ± std. dev. of 7 runs, 100 loops each)
--- # Ama şu çok iyi ya. hem array hem list, map ile dehşet hızlanıyor; for'a ve comprehension'a göre:
In [51]: %%timeit
    ...: newlist = map(str.upper, oldlist)
2.23 µs ± 33.8 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

In [52]: %%timeit
    ...: newlist = map(str.upper, old)
2.24 µs ± 32.5 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
-------------------------------------
# ben bu aralar numpy array'e baya sardım ama for döngüsü gerekmediği durumlarda list daha hızlı olabilir bakmak lazım
---
def myfunc(a, b):
    if a > b:
        return a - b
    else:
        return a + b

vfunc = np.vectorize(myfunc)	# bu heralde sadece yazılan kodu azaltmak için.çünkü normal yoldan yapıunca süresi değişmedi.aşağıda:
vfunc([1, 2, 3, 4], 2)
array([3, 4, 1, 2])
264 µs ± 1.69 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
---
kl = []
def rt(a, b):^M
    global kl
    for im in a:
        if im > b:^M
            kl.append(a - b)
        else:^M
            kl.append(a + b)
%%timeit
vfunc([1, 2, 3, 4], 2)
272 µs ± 20.6 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
-------------------------------------
f = open('??? ???? ???? ???? ? ??? ????? ????? ????? ??? ??? ???? ???? ??????? ??????? ????? ?????? ?????.mp3')
# farsça karakterler var o yüzden öyle görünüyo
f = f.read() # ilk unicode error verdi, tekrar deneyince oldu nasılsa
-------------------------------------
np.pad(arr.reshape(-1, 1), ((0, 0), (2, 0)), 'constant').reshape(-1, )
---
np.any 	# arraydaki herhangi (any) bi eleman true ise true döndürür
		# boş veya hepsi false ise false döndürür. can be thought as OR operation
np.all	# hepsi true ise veya boş ise true döndürür. can be thought as AND operation
# both of them short circuit the execution as soon as the result is known 
---
arr1d2=np.array([1,2])
arr3d222=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# Correct Solution is below
for i1 in range(len(arr1d2)):
    print(arr1d2[i1]*arr3d222[i1])
# faster and more pythonic way:
arr1d2[:, np.newaxis, np.newaxis] * arr3d222	# or
arr1d2.reshape(len(arr3d222),1,1) * arr3d222
-------------------------------------
def greet(greeting,target):
    return '%s! %s' % (greeting,target)
gre = functools.partial(greet,'hola')
gre('bob')
'hola! bob'
-------------------------------------
stop writing classes:
if you need later, you can convert :)
so in conclusion if you see a class with two methods and init :) it'a not a class. Don't make new exceptions, when you don't need to
and you don't need to :) ^^
-------------------------------------
def on_progress(stream, chunk, file_handle, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining 
    percentage_of_completion = bytes_downloaded / total_size * 100
	# Then you have to use percentage_of_completion variable to draw the progress bar
yt('https://www.youtube.com/watch?v=iOi5-XMBnzA').register_on_progress_callback(on_progress)
-------------------------------------
%load_ext fortranmagic							# ipython'da çalışmadı
%%fortran
subroutine func_fort(n,d)
    integer, intent(in) :: n
    double precision, intent(out) :: d
    integer :: i
    d = 0
    do i = 0, n = 1
        d = d + (mod(i,3) - 1) * i
    end do
end subroutine func_fort
---
In [33]: %who_ls 	# bu %who'nun \n'lı hali galiba
Out[33]: ['i', 'idx', 'inp', 'np', 'os', 'out', 'subprocess']
---
%reset
%reset -f
%reset_selective -f variable
---
%save Desktop/498_workspace 1-37
---
get_ipython().user_ns['variable']
---
ctrl+r -> I-search backward
ctrl+s -> I-search
ctrl+p -> üst tuşundan farkını anlamadım
ctrl+y -> bi tane girdi kopyalanmış, onu yapıştırıyosun gibi ama niye o anlamadım
ctrl+o -> yazmadığın halde ek satır koyuyo
ctrl+d -> escape (ama soruyo)
ctrl+l -> cls (clear space)
ctrl+v -> normal yapıştır 
ctrl+j -> enter'dan farkını anlamadım
ctrl+m -> enter'dan farkını anlamadım
ctrl+w -> öbek öbek siliyo. mesela url = 'wdf.ttx' burda ilk tırnaklı ifadeyi, sonra ='i sonra da url kelimesini siliyo
ctrl+t -> son iki harfin yerini değiştiriyo. çok mu önemli anlamadım. basmaya devam edersen bi harfi ileriye doğru götürmüş oluyo
ctrl+h -> normal sil tuşundan bi farkı yok gibi
ctrl+b -> sol tuşundan farkını anlamadım
ctrl+c -> girdinin tamamını siliyo
ctrl+n -> ctrl+c'den farkını anlamadım
ctrl+ ->
ctrl+ ->
ctrl+ ->
---
%history -l 2 # son iki line'ı yazdırır
%history 2 # line number'ı 2 olan satırı yazdırır
-o # also print outputs for each input.
# By default, input history is printed without line numbers so it can be directly pasted into an editor. Use -n to show them.
%save mak.py 1-56 -a # -a append eder diyo ama olmadı, overwrite etti, dikkat et
---
# jupyter notebook'ta imleç metodun parantezleri içinde iken shift + tab'a basarsan öntanımlı argümanları görebilirsin
# aslında metodun help'ini görüyosun heralde
---
%history -g -f "fee.py" # bütün ipython history'sini dosyaya yazar. g olmazsa sadece current session'ı yazar. veya tam tersi
---
jupyter nbconvert --to script --no-prompt "bir_notebook.ipynb"
# script yerine pdf,html filan yazılabiliyo. python ile script aynı gibi
# --no-prompt [In1]'lerin yazılmamasını sağlıyo
# --clear-output -> Clear output of current file and save in place, overwriting the existing notebook. gibi başkaları da var
-------------------------------------
np.min, min'den çok hızlıymış nasılsa
-------------------------------------
mask = L < 4 | L > 8
L[mask]
ind = [0,4,2]
L[ind]
-------------------------------------
M = np.arange(6).reshape(2,3)
M[[1,0],:2]
M[M.sum(axis=1) > 4, 1:]
-------------------------------------
i = np.arange(1000)
D[i,i] = np.inf
-------------------------------------
fa = 'simpsons homer marge bart lisa sally'
lastname, *members = fa.split()				# çok iyi
-------------------------------------
cast = {input('role? '): input('actor? ') for i in range(2)}	# maşallah
-------------------------------------
options = {i:j for i,j in zip(keys,c)}
options.get(filter,back_projection())
-------------------------------------
matplotlib.interactive()
---
fig,ax = plt.subplots()
ax.plot([1,2,3],[10,-10,30])
# save the figure object as a binary file:
import pickle
pickle.dump(fig, open('FigureObject.fig.pickle', 'wb')) # This is for Python 3 - py2 may need `file` instead of `open`
# you may want to consider to use 'with'
figx = pickle.load(open('FigureObject.fig.pickle', 'rb'))
figx.show() # Show the figure, edit it, etc.!
# You can even extract the data from the plots:
data = figx.axes[0].lines[0].get_data() 
data = figx.axes[0].lines[0].get_xydata() # or for an image:
data = figx.axes[0].images[0].get_data()
---
ax2.set_axis_off()
# şununla farkını bilmiyorum: 
ax.get_yaxis().set_visible(False)
---
barprops = dict(aspect='auto', cmap='binary', interpolation='nearest')
ax1.imshow(x.reshape((-1, 1)), **barprops)
---
ax.set_aspect(1)	# x ve y axis oranlarını 1 yap
---
from matplotlib.widgets import Cursor
cursor = Cursor(ax, useblit=True, color='red', linewidth=2)
---
fig, ax = plt.subplots()
im = ax.imshow(image)
patch = patches.Circle((260, 200), radius=200, transform=ax.transData)
im.set_clip_path(patch)
---
plt.axes #to create inset axes within the main plot axes.
---
ax2.margins(2, 2)           # Values >0.0 zoom out
---
fig = plt.figure(FigureClass=MyFigure, figtitle='my title') # MyFigure denen şey function olcak heralde
ax = fig.subplots()
ax.plot([1, 2, 3])
---
fig, axs = plt.subplots(nrows=2, ncols=2, constrained_layout=True)
for ax in axs.flat:
    example_plot(ax)
---
# Remove horizontal space between axes
fig.subplots_adjust(hspace=0)
---
t = np.arange(0.01, 5.0, 0.01)
s = np.exp(-t)
plt.plot(t, s)
plt.xlim(5, 0)
---
# switch back to figure 1 and make some changes
# <ipython-input-27-75b0dd9c5548>:1: MatplotlibDeprecationWarning: Adding an axes using the same arguments as a previous axes c
# urrently reuses the earlier instance.  In a future version, a new instance will always be created and returned.  Meanwhile, t
# his warning can be suppressed, and the future behavior ensured, by passing a unique label to each axes instance.
# plt.subplot(211)
---
ax = plt.gca()
ax.set_xticklabels([])
---
secaxx = ax.secondary_xaxis('top', functions=(date2yday, yday2date))
secaxx.set_xlabel('yday [2018]')
---
fig, ax1 = plt.subplots()
color = 'tab:red'
ax1.set_ylabel('exp', color=color)
ax1.plot(t, data1, color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
fig.tight_layout()
---
plt.title('Center Title')
plt.title('Left Title', loc='left')
plt.title('Right Title', loc='right')	# aynı plotta
---
ax2.clear()	# bi keresinde plot yanıt vermiyor diyordu kapanmıyordu, bu kapattı hemen
# .clear() içindeki line'ı isliyo, .remove plotun tamamını kaldırıyo, bi pencereyi kapatmadığı kalıyo
# haşiye - ilginç: bi keresinde yanıt vermiyodu, remove() dedim, yanıt vermeye başladı 
# KALDIĞIM YER: Align y-labels
-------------------------------------
make_frame = lambda t : 2*[ np.sin(404 * 2 * np.pi * t) ]
-------------------------------------
from moviepy.editor import *	# how to concatenate
import os
os.chdir('Desktop/hastalar0')
k = 1
for i in os.listdir():
    globals()['clip'+str(k)] = AudioFileClip(i)
    k += 1
liste = []
for i in range(58):
    liste.append(globals()['clip'+str(i+1)])
final = concatenate_audioclips(liste)
final.write_audiofile('final.mp3')		# ya orjinal dosyaların toplamı 17 MB, ama bu 62 MB :( niye öyle ?
# bir üst satırdaki üzüntülü sualimin cevabını buldum elh. bitrate'i ayarlamam gerekiyomuş
# sonradan cmd'yi açıp şunu yazdım: 
ffmpeg -i final.mp3 -ab 37000 final.mp3 # (ab veya ba) (37000 de biraz farklı olabilir)
# galiba 36000 falan yapınca bitrate 34kbps oldu, onda ses kalitesi biraz düşüktü. 
# sonra 37000 yapınca 41kbps oldu. yani discrete değişiyo
---
from moviepy.editor import *	# simple video cut operation
vid = VideoFileClip('PN_JUNCTIONS_PART_2.mp4')
v1 = vid.subclip((13,24),(13,39)) # ikinci parantezi yazmazsan otomatikman duration of the video olur
v1.write_videofile('212.mp4')
v1.write_videofile('gulpembe.mp4')
BURDAYIM kelimesini arat.
TEKRAR BAK kelimesini arat. ... meselesi
---
ffmpeg -ss 00:01:00 -i "İlmin İzzeti ve Namusu İçin Münazara - Muhammed.mp4" -to 00:01:05 -c copy output.mp4
# moviepy acayip yavaş. bu hem hızlı hem daha pratik. ama baş tarafında ufak bi sorun oldu
-------------------------------------
# TEXT-TO-SPEECH. 
# python 3.6.6'da çalıştı. 3.8.1'de çalışmadı
import pyttsx3
engine = pyttsx3.init()
engine.say('I will speak this text')
engine.runAndWait()
---
engine.save_to_file('nasılsın emre', 'test.mp3')
engine.runAndWait()
---
rate = engine.getProperty('rate')
engine.setProperty('rate',125)
---
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)	# zaten bi tane var. index 1 yok.
-------------------------------------
android studio'da adb'yi usb'siz wifi üserinden kullamak için:
C:\Users\Emre\AppData\Local\Android\Sdk\platform-tools>adb tcpip 5555
restarting in TCP mode port: 5555

C:\Users\Emre\AppData\Local\Android\Sdk\platform-tools>adb connect 10.119.132.239
connected to 10.119.132.239:5555

-------------------------------------
--download-quizzes
from pytube import Playlist
playlist = Playlist('https://www.youtube.com/watch?v=58PpYacL-VQ&list=UUd6MoB9NC6uYN2grvUNT-Zg')
playlist.populate_video_urls()
print('Number of videos in playlist: %s' % len(playlist.video_urls))
playlist.download_all()
---
# playlist öğesi çalışmamıştı, html json cart curt yüzünden source kodu şöyle olmalıymış: (pytube version: '9.6.4', python 3.8.1)
from pytube import Playlist
import re

playlist = Playlist("https://www.youtube.com/playlist?list=PLynhp4cZEpTbRs_PYISQ8v_uwO0_mDg_X")
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

print(len(playlist.video_urls))
for url in playlist.video_urls:
    print(url)
------------------------------------- MACHINE LEARNING
# Labeling the Data
import numpy as np	
from sklearn import preprocessing
input_labels = ['red','black','red','green','black','yellow','white']
encoder = preprocessing.LabelEncoder()		# encoding
encoder.fit(input_labels)
test_labels = ['green','red','black']
encoded_values = encoder.transform(test_labels)
encoded_values = [3,0,4,1]					# decoding
decoded_values = encoder.inverse_transform(encoded_values)
---
# Building a Classifier in Python
# Naïve Bayes Classifier: The assumption is that the predictors are independent. In simple words:
# it assumes that the presence of a particular feature in a class is unrelated to the presence of any other feature.
# types of Naïve Bayes models are Gaussian, Multinomial and Bernoulli
from sklearn.datasets import load_breast_cancer	
label_names = data['target_names']^M
labels = data['target']^M
feature_names = data['feature_names']
features = data['data']
from sklearn.model_selection import train_test_split	# Organizing data into sets
train, test, train_labels, test_labels = train_test_split(features,labels,test_size = 0.40, random_state = 42)
from sklearn.naive_bayes import GaussianNB	# Building the model	# Naïve Bayes algorithm
gnb = GaussianNB() # Gaussian Naïve Bayes Classifier
model = gnb.fit(train, train_labels)	# train the model by fitting it to the data
preds = gnb.predict(test)	# 0s and 1s are the predicted values for the tumor classes – malignant and benign.
from sklearn.metrics import accuracy_score	# to determine the accuracy of our model
print(accuracy_score(test_labels,preds))	
# Support Vector Machines (SVM)
import pandas as pd
import numpy as np
from sklearn import svm, datasets
import matplotlib.pyplot as plt
iris = datasets.load_iris()
X = iris.data[:, :2]
y = iris.target
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
h = (x_max / x_min)/100
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
np.arange(y_min, y_max, h))
X_plot = np.c_[xx.ravel(), yy.ravel()]
C = 1.0
svc_classifier = svm.SVC(kernel='linear', C=C, decision_function_shape='ovr').fit(X, y)
Z = svc_classifier.predict(X_plot)
Z = Z.reshape(xx.shape)
plt.figure(figsize=(15, 5))
plt.contourf(xx, yy, Z, cmap=plt.cm.tab10, alpha=0.3)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.xlim(xx.min(), xx.max())
plt.title('SVC with linear kernel')
plt.show()
# Logistic Regression
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
X = np.array([[2, 4.8], [2.9, 4.7], [2.5, 5], [3.2, 5.5], [6, 5], [7.6, 4], \
[3.2, 0.9], [2.9, 1.9], [2.4, 3.5], [0.5, 3.4], [1, 4], [0.9, 5.9]])
y = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3])
Classifier_LR = linear_model.LogisticRegression(solver='liblinear', C=75) # create logistic regression classifier
Classifier_LR.fit(X, y) # train this classifier
def Logistic_visualize(Classifier_LR, X, y):	# in order to visulize the output
	min_x, max_x = X[:, 0].min() - 1.0, X[:, 0].max() + 1.0
	min_y, max_y = X[:, 1].min() - 1.0, X[:, 1].max() + 1.0
	return min_x, max_x, min_y, max_y
min_x, max_x, min_y, max_y = Logistic_visualize(Classifier_LR, X, y)
mesh_step_size = 0.02	# define the mesh grid of X and Y values:
x_vals, y_vals = np.meshgrid(np.arange(min_x, max_x, mesh_step_size), np.arange(min_y, max_y, mesh_step_size))
# run the classifier on the mesh grid:
output = Classifier_LR.predict(np.c_[x_vals.ravel(), y_vals.ravel()])
output = output.reshape(x_vals.shape)
plt.figure()
plt.pcolormesh(x_vals, y_vals, output, cmap=plt.cm.gray)
plt.scatter(X[:, 0], X[:, 1], c=y, s=75, edgecolors='black', linewidth=1, cmap=plt.cm.Paired) # specify the boundaries of the plot:
plt.xlim(x_vals.min(), x_vals.max())
plt.ylim(y_vals.min(), y_vals.max())
plt.xticks((np.arange(int(X[:, 0].min() - 1), int(X[:, 0].max() + 1), 1.0)))
plt.yticks((np.arange(int(X[:, 1].min() - 1), int(X[:, 1].max() + 1), 1.0)))
plt.show()
# Decision Tree Classifier
------------------------------------- Symbolic Python 
import sympy 
x, y, z = sympy.symbols('x y z')
a = 2 * sympy.atan(x * sympy.sin(y) / (1 - x * sympy.cos(y))).diff(y) + 1 # tek variable varsa diff() yeterli
sympy.simplify(a)
sympy.pretty_print(_)
---
IB, b = sympy.symbols('IB b')
sympy.solve(-VBB + IB * RBB + 0.7 + IB * (b+1) * 10e3,b) # diğerleri constant. ,b demezsen sözlük olarak verir. yoksa list
---
expr = 2*x - 7*y # is equivalent to writing:
expr = Eq(2*x - 7*y, 0) which would tell SymPy that 2*x - 7*y = 0
---
sympy.rewrite() # çok keşfetmedim
---
-------------------------------------
from sklearn import datasets
iris = datasets.load_iris()
digits = datasets.load_digits()
digits.data
digits.target # gives the ground truth for the digit dataset, that is . # also known as label
# the number corresponding to each digit image that we are trying to learn
# The data is always a 2D array, shape (n_samples, n_features), although the original data may have had a different shape. 
# In the case of the digits, each original sample is an image of shape (8, 8) and can be accessed using: 
digits.images[0]
# An example of an estimator is the class sklearn.svm.SVC 
from sklearn import svm
clf = svm.SVC(gamma=0.001, C=100.) # In this example, we set the value of gamma manually. To find 
# good values for these parameters, we can use tools such as grid search and cross validation.
clf.fit(digits.data[:-1],digits.target[:-1]) # except for the last image, which we’ll reserve for our predicting
# pickle'ı kullanabilirsin: 
s = pickle.dumps(clf) ... # dump deyince "missing required argument 'file'" dedi
# pickle has some security and maintainability issues:
# https://scikit-learn.org/stable/modules/model_persistence.html#model-persistence
clf.predict(digits.data[-1:]) # refer to one of the upper comments: "The data is always a 2D array"
# bir digit'i görebilmek için:
plt.imshow(digits.images[-1])
from joblib import dump,load
dump(clf,'filename.joblib') #  more efficient on big data
---
plt.imshow(digits.images[-1],cmap=plt.cm.gray_r)
digits.images.shape
(1797, 8, 8)
# To use this dataset with scikit-learn, we transform each 8x8 image into a feature vector of length 64:
data = digits.images.reshape(digits.images.shape[0],-1)	# it becomes (1797, 64)
# An estimator is any object that learns from data; 
# it may be a classification, regression or clustering algorithm 
# or a transformer that extracts/filters useful features from raw data.
# All estimator objects expose a fit method that takes a dataset (usually a 2-d array):
estimator.fit(data)

# to classify the observations in a set of finite labels, in other words to “name” the objects observed: classification
# to predict a continuous target variable: regression
import numpy as np
from sklearn import datasets
iris_X, iris_y = datasets.load_iris(return_X_y=True)
np.unique(iris_y)	# iris_y içindeki eleman çeşitleri galiba
---
np.random.seed(0) # A random permutation, to split the data randomly (galiba)
indices = np.random.permutation(len(iris_X))
iris_X_train = iris_X[indices[:-10]]
iris_y_train = iris_y[indices[:-10]]
iris_X_test = iris_X[indices[-10:]]
iris_y_test = iris_y[indices[-10:]]
from sklearn.neighbors import KNeighborsClassifier # # Create and fit a nearest-neighbor classifier
knn = KNeighborsClassifier()
knn.fit(iris_X_train, iris_y_train)
knn.predict(iris_X_test)
iris_y_test
---
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test  = diabetes_X[-20:]
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test  = diabetes_y[-20:]
from sklearn import linear_model
regr = linear_model.LinearRegression()
regr.fit(diabetes_X_train, diabetes_y_train)
regr.coef_
np.mean((regr.predict(diabetes_X_test) - diabetes_y_test)**2) # mean square error
# Explained variance score: 1 is perfect prediction and 0 means that there is no linear relationship between X and y:
regr.score(diabetes_X_test, diabetes_y_test)
# yetkili olmak. çaresiz beceriksiz kaldıkları o durumları düşün geliştiriliyor
# her an şüphe et gözün açık olsun ve muhtemel her aksaklığı göz önğnde bulundur. hastanede doktor kılıklı biri fake olabilir
--- 
SYSTEM CONFIGURATION CHANGES
windows + x -> performans -> ayarlar -> gelişmiş -> değiştir -> en baştaki tiki kaldırdım -> özel boyut (önceden "sistem yönetimli
boyut"taydı) -> sırasıyla 3072 ve 9216 MB -> ayarla -> tamam
(windows + x işe yaramadı. başlat'a performans yazdım. sonra şunu seçtim: windowsun görünmünü ve performansını ayarla)
bu ayarın sadece temporarily olarak yapılması önerilmiş:
Increasing page file size may help prevent instabilities and crashing in Windows. However, a hard drive read/write times are much 
slower than what they would be if the data were in your computer memory. Having a larger page file is going to add extra work for 
your hard drive, causing everything else to run slower. Page file size should only be increased when encountering out-of-memory 
errors, and only as a temporary fix. A better solution is to adding more memory to the computer.
---







-------------------------------------

kp00868070313 #edit: bu acaba kyk kredi numarası mı 





