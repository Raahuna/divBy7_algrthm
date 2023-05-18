import os
import time
def run_numberInput(message, inputPermission, inputValue): # "run_numberInput" isminde bir fonksiyon oluştur.
  if (inputPermission == "allowInput"): # Eğer girdiye izin verildiyse...
    Input = input(message) # Kullanıcının yazabilmesi için bir girdi oluştur.
  elif(inputPermission == "denyInput"):
    Input = inputValue
  try: # Dene
    if (float(Input) < 100): # Eğer sayı 100'den küçükse...
      run_numberInput("Lütfen daha büyük bir sayı giriniz. \n>> ", "allowInput", "") # Fonksiyonu tekrar çalıştır.

    if (float(Input) > 9999999999999999): # Eğer sayı çok büyükse...
      run_numberInput("Lütfen daha küçük bir sayı giriniz. \n>> ", "allowInput", "") # Fonksiyonu tekrar çalıştır.
  except: # Test başarısızsa (Büyük ihtimalle sayı girilmedi)...
    run_numberInput("Sadece rakamlar kullanılabilir! Sayıyı tekrar giriniz. \n>> ", "allowInput", "") # Fonksiyonu tekrar çalıştır.
  
  # -------- Algoritmayı oluştur. -------- #

  def Algorithm(Number): # Algoritma için ayrı bir fonksiyon oluştur ve "Number" adında bir değişken ver.
    lastDigit = Number[-1] # Sayının son basamağını al "lastDigit" adını ver.
    multipliedLastDigit = str(float(lastDigit) * 5)[0:-2] # lastDigit ile 5'i çarp ve sadeleştir (x.y => x) son olarak buna "multipliedLastDigit" adını ver.
    formatedNumber = Number[0:-1] # Sayının son basamağını sil ve buna "formatedNumber" adını ver. 
    Result = str(float(formatedNumber) + float(multipliedLastDigit))[0:-2] # formatedNumber'dan multipliedLastDigit'i çıkar ve sondan 2 haneyi silerek sadeleştir.
    
    return Number, lastDigit, multipliedLastDigit, formatedNumber, Result # İşlemlerin çıktısını oluştur.
  Algorithm(Input) # Algoritmayı, kullanıcının girdiği değeri "Number" değişkeni olacak şekilde çalıştır. 
  Number, lastDigit, multipliedLastDigit, formatedNumber, Result = Algorithm(Input) # Çıktıyı al

  # -------- İşlemleri adımlar halinde yazdır. -------- #

  print(f'\033[96m {Number} değerinin son hanesi alındı => {lastDigit} \033[0m')
  time.sleep(0.5) # 0.5 Saniye bekle.
  print(f'\033[96m "{lastDigit} . 5" çarpım sonucu => {multipliedLastDigit} \033[0m')
  time.sleep(0.5) # 0.5 Saniye bekle.
  print("\n") # Satır atla.
  print(f'\033[96m {Number} sayısının son basamağı silindi => {formatedNumber} \033[0m')
  time.sleep(0.5) # 0.5 Saniye bekle.
  print(f'\033[96m "{formatedNumber} + {multipliedLastDigit}" => {Result} \033[0m')
  time.sleep(0.5) # 0.5 Saniye bekle.

  # -------- 7'li tekrar. -------- #

  print(f"\033[95m Algoritma hesaplandı. Tekrarlanıyor... \033[0m") # İşlemin devam edeceğini belirt.
  time.sleep(1) # 1 Saniye bekle.
  Counter = 3 # Sayaç oluştur (3. adımdan başlat).
  while Counter != 8: # İşlemi tekrarlamak için bir while döngüsü oluştur.
    Algorithm(Result) # Algoritmayı, çıkan sonuç yeni "Number" değişkeni olacak şekilde çalıştır. 
    Number, lastDigit, multipliedLastDigit, formatedNumber, Result = Algorithm(Result) # Çıktıyı al.
    print(f'\033[94m {Counter}) {Result} ({formatedNumber} + ({lastDigit} . 5)) \033[0m') # Sonucu yazdır.
    Counter+= 1
    time.sleep(0.2) # 0.2 Saniye bekle.
  time.sleep(0.5) # 0.5 Saniye bekle.
  if (len(Result) <= 2): # Sayı 2 basamaklıdan küçükse...
    print("\n")
    time.sleep(0.5) # 0.5 Saniye bekle.
    print(f'\033[93m Son adımdaki sonucumuz {len(Result)} basamaklı, tekrar olmayacak. \033[0m') # Tekrar olmayacağını bildir.
    time.sleep(0.5) # 0.5 Saniye bekle.
    print(f'\033[95m "{Result} / 7" işleminden çıkan sonuç: {float(Result) / 7}, kalan: {float(Result) % 7} \033[0m') # Oluşan sonucu 7'ye böl ve sonuç ve kalanı yazdır.
    time.sleep(0.5) # 0.5 Saniye bekle.
    print("\n❤ Coded by Rahuna.") # Credit
    os.system("PAUSE") # Terminali durdur.
  else:
    print("\n")
    time.sleep(0.5) # 0.5 Saniye bekle.
    print(f'\033[91m 7. adımdaki sonucumuz {len(Result)} basamaklı, Tüm işlem tekrardan "{Result}" sayısına uygulanacak. \033[0m') # Sayının kaç basamaklı olduğunu söyle
    time.sleep(0.5) # 0.5 Saniye bekle.
    run_numberInput("", "denyInput", Result) # "run_numberInput" fonksiyonunu kullanıcıya yazma hakkı vermeden çalıştır.
    time.sleep(0.5) # 0.5 Saniye bekle.

run_numberInput("\033[95mLütfen bir sayı giriniz. \033[93m\n>> \033[0m", "allowInput", "") # "run_numberInput" fonksiyonunu kullanıcıya yazma hakkı vererek çalıştır.