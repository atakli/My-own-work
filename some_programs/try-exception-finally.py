def main():
	ilk_sayı=input("ilk sayı: ")					
	ikinci_sayı=input("ikinci sayı: ")
	try:
			sayı1=int(ilk_sayı)
			sayı2=int(ikinci_sayı)
			print(sayı1,"/",sayı2,"=",sayı1/sayı2)
	except (ValueError):
		print("Lütfen sadece sayı girin! ")
	except ZeroDivisionError:
		print("0'a niye bölüyosun kardeş! ")
	finally:
		print("final")
while 1:
	main()
