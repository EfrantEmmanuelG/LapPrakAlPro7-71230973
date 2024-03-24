kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

urutanhuruf1 = sorted(kata1)
urutanhuruf2 = sorted(kata2)

if len(urutanhuruf1) != len(urutanhuruf2):
    print("Kedua kata tersebut bukan kata anagram")
else:
    if urutanhuruf1 == urutanhuruf2:
        print("Kedua kata tersebut merupakan kata anagram")
    else:
        print("Kedua kata tersebut bukan kata anagram")