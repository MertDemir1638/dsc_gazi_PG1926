sylr=[]
tek_sylr=[]
while True:
    sayi = int(input('Sayı : '))
    sylr.append(sayi)
    if(int(sayi)%2!=0):
        tek_sylr.append(sayi)
    soru=input("Devam etmek istiyorsanız E yaziniz, Çıkmak istiyorsanız H yaziniz. ")
    if soru=="e" or soru=="E":
        continue
    else:
        print("Girdiğiniz değerler= "+str(sylr))
        tek_sylr.sort()
        print("En büyük tek_sylr değer= "+str(tek_sylr[-1]))
        break






