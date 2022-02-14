# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 13:46:15 2022

@author: Beyza
"""

import cv2

#Resimi okuyalım.
test_img = cv2.imread("image/selcuk_bayraktar.jpg")

#Face detection için gerekli olan xml uzantılı dosyayı dahil edelim.
#Github haar cascade yazarak erişebilrisiniz. 
face_cascade = cv2.CascadeClassifier("dataset/frontalface.xml") 

#Matris küçültmek için resmimizi gri formata çevirelim
gray_test_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)


#Face detection işlemini yapalım.
#Metod ayrıntıları Gri olan resim, yeniden ölçeklendirme sayısı,belli yerde yüz şablonundan kaç tane yakalarsa yüz saysın.
faces_test_img = face_cascade.detectMultiScale(gray_test_img,1.4,3)
#Çıktısına bakacak olursak x,y,w,h şeklinde olur

#Koordinatları belirledik şimdi dikdörtgeni çizelim
for (x,y,w,h) in faces_test_img:
    #İlk değer hangi resim üzerinde görmek istediğimiz
    #İkinci parametre olarak x ve y değerleri girilir
    #Üçüncü olarak dikdörtgenin sağ alt koordinatı
    #Son olarak rengi ve kalınlığını belirle
    cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,100,45),2)


cv2.imshow("Selçuk Bayraktar",test_img)