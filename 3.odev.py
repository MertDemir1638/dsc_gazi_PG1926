nmbrs=[]
sfrlr = []
snc=[ ]
while True:
    sy=int(input("Lütfen bir sayı giriniz: "))
    nmbrs.append(sy)
    for syi in nmbrs:
        if syi==0:
            sfrlr.append(syi)
            nmbrs.remove(0)
            snc=sfrlr+nmbrs
    soru=input("Devam etmek istiyorsanız E yaziniz, Çıkmak istiyorsanız H yaziniz. ")
    if soru=="e" or soru=="E":
        continue
    else:
        print(snc)
        break







