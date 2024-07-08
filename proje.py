bilgilendirici_kelimeler = {
            'EZ ' : 'Rakibi aşağılamak',
            'LOL ' : 'Gülmek',
            'SS ' : 'Ekran görüntüsü',
            'CRİNGE' : 'Utandırıcı şeyler',
            }
world= input("Anlamadığınız kelimeler")

if world in bilgilendirici_kelimeler.keys():
    print(bilgilendirici_kelimeler[word])
else:
        print("kelime bulunamadı")
