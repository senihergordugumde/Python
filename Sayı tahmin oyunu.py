import random

a = random.randint(1,100)
hak = 5
kere = 0

while (hak > 0):
    hak -= 1
    kere += 1
    tahmin = int(input('Sayı tahmin et:'))

    if (tahmin == a) :
        print('Helal {} defada bildin. {} puan aldın.'.format(kere, (100 - (20 * kere))))
        break
    elif (a > tahmin):
        print('Çık')
    else:
        print('İn')
    if (hak == 0) :
        print('Kaybettin. Sayı: {}'.format(a))
    

