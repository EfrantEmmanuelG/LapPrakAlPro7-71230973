kalimat = input("Masukkan suatu kalimat: ")
kata = input("Masukkan kata yang ada pada kalimat yang akan dihitung: ")

jumlah_kata = kalimat.lower().count(kata.lower())

print(f"{kata} ada {jumlah_kata} buah")