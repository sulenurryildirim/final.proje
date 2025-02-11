path=ogrenciler.txt 
dosya=open(path,"a") # Verilen boş dosyayı açtım.

sinif=[] # Boş liste tanımladım.
n=int(input(" İşlem yapmak istediğiniz öğrenci sayısını giriniz: "))

try:
  def bilgiler(ad,soyad,vize,final): # "def" fonksiyonunu aynı ifadeleri tekrarlamamak için kullanır. Burada da verileri tek seferde istemek için kullandım.
    for dosya in range(n):
      ad=input(" Öğrenci adını giriniz: ")
      soyad=input(" Öğrenci soyadını giriniz: ")
      vize=int(input(" Öğrenci vize notunu giriniz: "))
      final=int(input(" Öğrenci final notunu giriniz: "))
  
  def sonuc(vize,final): # Geçme notunu hesaplamak için kullandım.
    gecme_notu=(vize*0.5)+(final*0.5)
    return gecme_notu

  bilgi=[ad,soyad,vize,final,gecme_notu]
  sinif.append(bilgi) # Girilen bilgileri "sinif" listesine ekledim.

  print("Ad:",ad,"Soyad:",soyad,"Vize:",vize,"Final",final,"Geçme notu:",gecme_notu)

dosya.write(sinif) # Listedeki bilgileri dosyaya yazdırdım.
dosya.close() # Dosyayı kapattım.

# Hata olup olmadığını kontrol etmek için "except" ifadesi kullandım.
except ValueError: 
  print("Girilen bir sayı değil!")

except:
  print("Beklenmeyen bir hata oluştu!")