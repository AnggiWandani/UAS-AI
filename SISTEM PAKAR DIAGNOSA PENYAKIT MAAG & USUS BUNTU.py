# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JVWhHwKCiqSaxMARZCtugitVV8xsUCM8
"""

import os

print("=================================================")
print("|\tSelamat Datang di Sistem Pakar\t\t|")
print("|\tDeteksi Gejala Magh dan Usus Buntu\t|")
print("=================================================")

nama = input("nama\t: ")
pilihan = input("Hallo "+nama+" ,\nApakah anda ingin melakukan diagnosa ? (y/n) : ")

os.system("clear")

while pilihan == "y" :
  print("Apakah anda merasakan gejala berikut ini ?")
  print("1. Perut kembung")
  print("2. Mual")
  print("3. Nafsu makan menurun")
  print("4. perut terasa sakit")
  ask1 = input("jawab (y/n) : ")

  if ask1 == "y" :
    print("\nApakah anda juga merasakan gejala berikut ini ? ")
    print("1. Naiknya asam lambung")
    print("2. Nyeri ulu hati")
    print("3. Sulit bernafas")
    print("4. Pusing")
    ask2 = input("jawab (y/n) : ")

    if ask2 == "y" :
      print("\nHI, "+nama+" Hasil diagnosa kamu adalah :")
      print("Gejala Magh segera ke dokter")
      break

    elif ask2 == "n" :
      print("\nApakah anda juga merasakan gejala berikut ini ? ")
      print("1. Nyeri perut")
      print("2. Merasa mual")
      print("3. Muntah")
      print("4. Kehilangan nafsu makan")
      ask3 = input("jawab (y/n) : ")

      if ask3 == "y" :
        print("\nHI, "+nama+" Hasil diagnosa kamu adalah :")
        print("Gejala Usus Buntu segera ke dokter")
        break

      elif ask3 == "n" :
        print("\nHI, "+nama+" Sepertinya anda sedang banyak pikiran")
        break

      else :
          print("\nHI, "+nama+" sepertinya anda tidak mau berobat")
          break

  elif ask1 == "n" :
    print("\nHI, "+nama+" sepertinya anda butuh healing")
    break

else :
  print("\nHI, "+nama+" seprtinya anda tidak mau berobat")
  print("===============TERIMA KASIH==============")