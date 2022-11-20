def hesap_makinası(sayı1,sayı2,islem):
          if islem == "+":
              sonuc = sayı1 + sayı2
              print(sonuc)
          elif islem == "*":
              sonuc = sayı1 * sayı2
              print(sonuc)
          elif islem == "-":
              sonuc = sayı1 - sayı2
              print(sonuc)
          else:
              print("İlgili işlem bu hesap makinasında yapılmamakta")

import random as rd

list = ["Ghezzal","Salih","Quaresma","Cenk Tosun","Rosier"]

def guess_favourite_player(liste,favourite_player):
    guess_1 = rd.choice(liste)
    guess_2 = rd.choice(liste)
    guess_3 = rd.choice(liste)
    if guess_1 == favourite_player:
        print("Guess 1")
        print("Doğru tahmin")
        print(guess_1)
    elif guess_2 == favourite_player:
        print("Guess 2")
        print("Doğru tahmin")
        print(guess_2)
    elif guess_3 == favourite_player:
        print("Guess 3")
        print("Doğru tahmin")
        print(guess_3)
    else:
        print("Ne yazıkki tahmin edemedim")
    

#guess_favourite_player(list,"Quaresma")


def faktoriyel(sayı):
    faktoriyel = 1
    if sayı == 0 or sayı == 1:
        print('Faktoriyel:',faktoriyel)
    elif sayı < 0:
        print('Tanımsız')
    else:
        while sayı >= 1:
            faktoriyel = faktoriyel * sayı
            sayı = sayı - 1
        print('Faktoriyel:', faktoriyel)

#faktoriyel(4)

list = ["Ghezzal","Salih","Quaresma","Cenk Tosun","Rosier","Delgado","Ricardinho"]
i=0
while i<=len(list):
    print(list[i])
    i = i +1 
    if i == len(list):
        break