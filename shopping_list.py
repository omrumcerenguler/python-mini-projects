import json #Bu, listeyi dosyaya kaydetmek/yüklemek için lazım.
FILE_NAME = "shopping_list.json" #Bu dosya alışveriş listesini kaydedeceğimiz yer olacak.
def load_list(): #Program başlarken daha önce kaydedilmiş bir liste var mı diye kontrol etmek için şu fonksiyonu ekle:
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)  # Daha önce kaydedilmiş listeyi oku
    except FileNotFoundError:
        return []  # Dosya yoksa boş liste döndür
def save_list(shopping_list): #Liste değiştiğinde JSON dosyasına kaydedecek fonksiyon:
    with open(FILE_NAME, "w") as file:
        json.dump(shopping_list, file)  # Listeyi JSON formatında kaydet
shopping_list = load_list()  # Program açıldığında listeyi yükle


while True:
  secim= input("Ne yapmak istiyorsun? (ekle,sil,göster,çık) ").strip().lower()
  if secim == "ekle":
    eklenilecek_ürün= input("Eklemek istediğiniz ürünün ismini giriniz: ").strip().lower()
    shopping_list.append(eklenilecek_ürün)
    save_list(shopping_list)
    print("Güncel alışveriş listesi: ", shopping_list)
  elif secim == "sil":
    if not shopping_list:
      print("Liste zaten boş! ")
    else:
      silinecek_ürün= input("Silmek istediğiniz ürünün ismini girin: ").strip().lower()
      if silinecek_ürün in shopping_list:
        shopping_list.remove(silinecek_ürün)
        save_list(shopping_list)
        print("Güncel alışveriş listesi: ", shopping_list)
      else:
        print(f"{silinecek_ürün} zaten listede yok!")

  elif secim == "göster":
    if not shopping_list:
        print("Sepet boş :(")
    else:
        print("Sepetindeki ürünler:")
        for item in shopping_list:
            print("-", item)
  elif secim == "çık":
    print("Güle güle tatlım 💖")
    break
  else:
    print("geçerli bir komut giriniz! (ekle,sil,göster,çık) ")


