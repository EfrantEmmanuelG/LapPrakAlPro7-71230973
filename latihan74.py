kalimat = input("Masukkan satu kalimat: ")

kata = kalimat.split()

kata_terpendek = kata[0]
kata_terpanjang = kata[0]

for i in kata:
    if len(i) < len(kata_terpendek):
        kata_terpendek = i
    elif len(i) > len(kata_terpanjang):
        kata_terpanjang = i

print("Terpendek:", kata_terpendek)
print("Terpanjang:", kata_terpanjang)
