# encoding:utf-8
class style():
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"
# sahip olunan çocuk başına alınan prim ücreti
prim = {
	'0':402, 
	'1':462,
	'2':522,
	'3':603,
	'4':642.5
}
prim2 = {
	'0':481.5, 
	'1':543,
	'2':603,
	'3':684,
}
# Digit yetersiz float için o yüzden bunu kulanıcaz
def is_float_digit(n: str) -> bool:
     try:
         float(n)
         return True
     except ValueError:
         return False

adı = input("Çalışanın ismi:\n")
while adı.isalpha() == False:
	print("Lütfen alfabetik karakterler giriniz:")
	adı = str(input("Çalışanın ismi:\n"))
evbe = input("Evlimisiniz? y/n\n")
while evbe != "y" or evbe != "n":
	if evbe == "y":
		medeni = "Evli"
		y = 0
		eş = input("Eşiniz çalışıyor mu? y/n\n")
		while eş != "y" or evbe != "n":
			if eş == "y":
				eşçalışma = "Eşiniz çalışıyor"
				çocuk = (input("Kaç çocuğunuz var?\n"))
				while çocuk.isalpha() == True:
					print(f"Senin çocuğun '{çocuk}'mı bu mu lütfen bir sayı gir:")
					çocuk = (input("Kaç çocuğunuz var?\n"))
				
				if int(str(çocuk)) >= 5:
					y = 684
				else:
					y = prim[çocuk]
				break
			elif eş == "n":
				eşçalışma = "Eşiniz çalışmıyor"
				y = 481.5
				çocuk = (input("Kaç çocuğunuz var?\n"))
				while çocuk.isalpha() == True:
					print(f"Senin çocuğun {çocuk} bu mu lütfen bir sayı gir:")
					çocuk = (input("Kaç çocuğunuz var?\n"))
				if int(str(çocuk)) >= 4:
					y = 684
				else:
					y = prim2[çocuk]
				break
			print("Lütfen sadece y/n diyiniz:")
			eş = input("Eşiniz çalışıyor mu? y/n\n")
		break
	if evbe == "n":
		çocuk = 0
		eşçalışma = "Senin eşin yok"
		medeni = "Bekar"
		y = 402
		print(f"{çocuk}{eşçalışma}{medeni}{y}")
		break
	print(f"Lütfen sadece y/n diyiniz:")
	evbe = input("Evlimisiniz? y/n\n")
deger = float(input("Saatlik ücreti:\n"))
saat = float(deger)
while is_float_digit(saat) == False and saat.isalpha == True:
	print("Lütfen sayı giriniz:\n")
	saat = float(input("Saatlik ücreti:\n"))
gün = int(input("Günde kaç saat çalışıyor:\n"))
while gün > 24 or gün.isdigit() == False:
	print("Günde en fazla 24 saat var lütfen bir daha giriniz!")
	gün = int(input("Günde kaç saat çalışıyor:\n"))
hafta = int(input("Haftada kaç gün çalışıyor:\n"))
while hafta > 7 or hafta.isdigit() == False:
	print("Haftada 7 gün var lütfen bir daha giriniz\n")
	hafta = int(input("Haftada kaç gün çalışıyor:\n"))
günlük_kazanç = saat * gün
haftalık_kazanç = günlük_kazanç * hafta
aylık_kazanç = haftalık_kazanç * 4
if aylık_kazanç <= 5004:
	sgk = (aylık_kazanç * 14) / 100
	sig = (aylık_kazanç * 1) / 100
	vergili = aylık_kazanç - (sgk + sig)
	net = vergili + y
	print(f"Çalışanın ismi:{adı}\nMedeni durumu:{medeni}\nEş çalışma durumu:{eşçalışma}\nÇalışanın kaç çocuğu var:{çocuk}\nÇalışanın saatlik ücreti:{saat}\nGünde kaç saat çalışıyor:{gün}\nHaftada kaç gün çalışıyor:{hafta}\nÇalışanın günlük kazancı:{günlük_kazanç}")
	print(f"Çalışanın haftalık kazancı:{haftalık_kazanç}\nÇalışanın bürüt aylık kazancı:{aylık_kazanç}\nÇalışanın SGK pirimi:{sgk}\nÇalışanın İşsizlik SİG. Primi:{sig}\nÇalışanın vergiler çıkınca aylık kazancı:{vergili}\nÇalışanın net aylık kazancı:{net}")
if aylık_kazanç > 5004 and aylık_kazanç <= 32000:
	sgk = aylık_kazanç * 14 / 100
	sig = aylık_kazanç * 1 / 100
	gelir_vergisi = aylık_kazanç * 15 / 100
	vergili = aylık_kazanç - (sgk + sig + gelir_vergisi)
	print(f"Çalışanın ismi:{adı}\nMedeni durumu:{medeni}\nEş çalışma durumu:{eşçalışma}\nÇalışanın kaç çocuğu var:{çocuk}\nÇalışanın saatlik ücreti:{saat}\nGünde kaç saat çalışıyor:{gün}\nHaftada kaç gün çalışıyor:{hafta}\nÇalışanın günlük kazancı:{günlük_kazanç}")
	print(f"Çalışanın haftalık kazancı:{haftalık_kazanç}\nÇalışanın bürüt aylık kazancı:{aylık_kazanç}\nÇalışanın SGK pirimi:{sgk}\nÇalışanın İşsizlik SİG. Primi:{sig}\nÇalışanın vergiler çıkınca aylık kazancı:{vergili}\nÇalışanın net aylık kazancı:{net}")
if aylık_kazanç > 32000 and aylık_kazanç <= 70000:
	sgk = aylık_kazanç * 14 / 100
	sig = aylık_kazanç * 1 / 100
	gelir_vergisi = (aylık_kazanç - 32000) * 20 / 100
	vergili = aylık_kazanç - (sgk + sig + gelir_vergisi + 4800)
	print(f"Çalışanın ismi:{adı}\nMedeni durumu:{medeni}\nEş çalışma durumu:{eşçalışma}\nÇalışanın kaç çocuğu var:{çocuk}\nÇalışanın saatlik ücreti:{saat}\nGünde kaç saat çalışıyor:{gün}\nHaftada kaç gün çalışıyor:{hafta}\nÇalışanın günlük kazancı:{günlük_kazanç}")
	print(f"Çalışanın haftalık kazancı:{haftalık_kazanç}\nÇalışanın bürüt aylık kazancı:{aylık_kazanç}\nÇalışanın SGK pirimi:{sgk}\nÇalışanın İşsizlik SİG. Primi:{sig}\nÇalışanın vergiler çıkınca aylık kazancı:{vergili}\nÇalışanın net aylık kazancı:{net}")
if aylık_kazanç > 70000 and aylık_kazanç <= 250000:
	sgk = aylık_kazanç * 14 / 100
	sig = aylık_kazanç * 1 / 100
	gelir_vergisi = (aylık_kazanç - 70000) * 27 / 100
	vergili = aylık_kazanç - (sgk + sig + gelir_vergisi + 12400)
	print(f"Çalışanın ismi:{adı}\nMedeni durumu:{medeni}\nEş çalışma durumu:{eşçalışma}\nÇalışanın kaç çocuğu var:{çocuk}\nÇalışanın saatlik ücreti:{saat}\nGünde kaç saat çalışıyor:{gün}\nHaftada kaç gün çalışıyor:{hafta}\nÇalışanın günlük kazancı:{günlük_kazanç}")
	print(f"Çalışanın haftalık kazancı:{haftalık_kazanç}\nÇalışanın bürüt aylık kazancı:{aylık_kazanç}\nÇalışanın SGK pirimi:{sgk}\nÇalışanın İşsizlik SİG. Primi:{sig}\nÇalışanın vergiler çıkınca aylık kazancı:{vergili}\nÇalışanın net aylık kazancı:{net}")
if aylık_kazanç > 250000 and aylık_kazanç <= 880000:
	sgk = aylık_kazanç * 14 / 100
	sig = aylık_kazanç * 1 / 100
	gelir_vergisi = (aylık_kazanç - 250000) * 35 / 100
	vergili = aylık_kazanç - (sgk + sig + gelir_vergisi + 61000)
	print(f"Çalışanın ismi:{adı}\nMedeni durumu:{medeni}\nEş çalışma durumu:{eşçalışma}\nÇalışanın kaç çocuğu var:{çocuk}\nÇalışanın saatlik ücreti:{saat}\nGünde kaç saat çalışıyor:{gün}\nHaftada kaç gün çalışıyor:{hafta}\nÇalışanın günlük kazancı:{günlük_kazanç}")
	print(f"Çalışanın haftalık kazancı:{haftalık_kazanç}\nÇalışanın bürüt aylık kazancı:{aylık_kazanç}\nÇalışanın SGK pirimi:{sgk}\nÇalışanın İşsizlik SİG. Primi:{sig}\nÇalışanın vergiler çıkınca aylık kazancı:{vergili}\nÇalışanın net aylık kazancı:{net}")
if aylık_kazanç > 880000:
	sgk = aylık_kazanç * 14 / 100
	sig = aylık_kazanç * 1 / 100
	gelir_vergisi = (aylık_kazanç - 880000) * 40 / 100
	vergili = aylık_kazanç - (sgk + sig + gelir_vergisi + 281000)
	print(f"Çalışanın ismi:{adı}\nMedeni durumu:{medeni}\nEş çalışma durumu:{eşçalışma}\nÇalışanın kaç çocuğu var:{çocuk}\nÇalışanın saatlik ücreti:{saat}\nGünde kaç saat çalışıyor:{gün}\nHaftada kaç gün çalışıyor:{hafta}\nÇalışanın günlük kazancı:{günlük_kazanç}")
	print(f"Çalışanın haftalık kazancı:{haftalık_kazanç}\nÇalışanın bürüt aylık kazancı:{aylık_kazanç}\nÇalışanın SGK pirimi:{sgk}\nÇalışanın İşsizlik SİG. Primi:{sig}\nÇalışanın vergiler çıkınca aylık kazancı:{vergili}\nÇalışanın net aylık kazancı:{net}")
