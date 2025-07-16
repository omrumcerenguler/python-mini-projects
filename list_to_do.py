list_to_do=[]
while True:
  seçim=input("ne yapmak istersiniz? (ekle,sil,göster,çık) ")
  if seçim=="ekle":
    ekle_ürün=input("eklemek istediğiniz ürün: ")
    list_to_do.append(ekle_ürün)
  elif seçim=="sil":
    sil_ürün=input("silinecek ürün: ")
    list_to_do.remove(sil_ürün)
  elif seçim=="göster":
    if not list_to_do:
      print("liste boş")
    else:
      print("sepetindeki ürünler: ")
      for item in list_to_do:
        print("-", item)
  elif seçim=="çık":
    break
