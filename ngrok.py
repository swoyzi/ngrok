#!/usr/bin/env python3

import os 

while True:

	os.system("clear")

	print("""



				github=https://github.com/
				Telegram=https://t.me/Swoyzi_arsiv




###############################
			#	01)ngrok tcp   
			# # #	02)ngrok http
			    #	03)ngrok tls
			    #	04)ngrok update
 			    #	
			    #	
			    #
################################ Q)quit
""")

	islemno = input("işlem no: ")

	if islemno =="01":

		os.system("ngrok tcp 1275")

	elif islemno =="1":

		input("hatalı secim devam etmek icin enter bas ")

	if  islemno =="02":

		os.system("ngrok http 80")
	elif islemno =="2":

		input("hatalı secim devam etmek icin enter bas ")

	if islemno =="03":

		os.system("ngrok tls 8080")

	elif islemno== "3":

		input("hatalı secim devam etmek icin enter bas ")

	if islemno =="04":
		os.system("ngrok update")

	elif islemno=="4":
		 input("hatalı secim devam etmek icin enter bas ")

	elif islemno=="q" or islemno=="Q":
			quit()
