while True:
  try:
    birinci_sayı=float(input("1. sayıyı giriniz: "))
    break
  except:
      print("**lütfen geçerli bir sayı giriniz!")
while True:
  try:
    ikinci_sayı= float(input("2. sayıyı giriniz: "))
    break
  except:
    print("**lütfen geçerli bir sayı giriniz!")



işlem=input("hangi işlemi yapmak istiyorsunuz? (toplama,çıkarma,çarpma,bölme,exit) ")
if işlem=="toplama":
  print("toplama işl. sonucu: ",birinci_sayı+ikinci_sayı )
elif işlem== "çıkarma":
  print("çıkarma işl. sonucu: ", birinci_sayı-ikinci_sayı)
elif işlem=="çarpma":
  print("çarpma iş. sonucu: ", birinci_sayı*ikinci_sayı)
elif işlem== "bölme":
  print("bölme işl. sonucu: ", birinci_sayı/ikinci_sayı)
elif işlem=="exit":
  print("Görüşürüz cnm <3")
else :
  print("**geçerli bir ifade giriniz!")

