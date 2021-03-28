sorular = ["Bir yılda kaç ay var?(cevap 12)","Güneş sisteminde kaç gezegen vardır?(cevap 8)","10/2 kaç eder? (cevap 5)"]
cevaplar = [12,8,5]
soru_no = 0
puan = 0
while soru_no < len(sorular):
    print(str(soru_no + 1)+". soru\n"+sorular[soru_no])
    cevap = int(input("Cevap:\n"))
    if cevap == cevaplar[soru_no]:
        puan += 10
        print("Doğru cevap! Puanın: {}".format(puan))
    else:
        puan -= 10
        print("Yanlış cevap :( Puanın: {}".format(puan))
    soru_no += 1
