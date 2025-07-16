#şifreyi belirleme
while True:
  try:
    şifre=int(input("şifrenizi belirleyiniz: "))
    if len(str(şifre))==4: #len() fonksiyonu sadece stringte çalışır o yüzden şifreyi stringe çevirdik
      print("şifre başarıyla oluşturuldu! ")
      break
    else:
      print("lütfen 4 rakamlı bir şifre oluşturun! ")
  except:
    print("sadece rakam giriniz. ")

#3 kere yanlış girilirse kilitleme
hak=3
bakiye=1000
while hak>0:
  try:
    girilen= int(input("şifrenizi giriniz: "))
    if girilen!=şifre:
      hak-=1
      if hak>0:
        print(f"girdiğiniz şifre yanlıştır. Lütfen tekrar deneyiniz. Kalan hakkınız: {hak} ")
      else:
        print("giriş yapma hakkınız kalmamıştır. hesabınız kilitlendi. ")
        break
    else:
      print("Giriş başarılı, Hoşgeldiniz!")
      seçim=input("Yapmak istediğiniz işlemi seçiniz:\n1) Bakiye Görüntüle\n2) Para Yatır\n3) Para çek\n4) Çıkış ")
      if seçim=="1":
        print(f"Güncel Bakiyeniz: {bakiye} TL")
      elif seçim=="2":
        yatırılacak_miktar=float(input("Hesaba yatırılacak para miktarını giriniz: "))
        bakiye+=yatırılacak_miktar
        print(f"Güncel Bakiye= {bakiye} TL")
      elif seçim=="3":
        çekilecek_miktar=float(input("Çekilecek miktarı giriniz: "))
        bakiye-=çekilecek_miktar
        print(f"Güncel Bakiye= {bakiye}")
      elif seçim=="4":
        print("Bankamızı kullandığınız için teşekkürler! İyi günler dileriz.")
        break
  except:
    hak-=1
    if hak>0:
      print(f"sadece rakam giriniz. Kalan hakkınız: {hak}")
    else:
      print("giriş yapma hakkınız kalmamıştır. hesabınız kilitlendi. ")



