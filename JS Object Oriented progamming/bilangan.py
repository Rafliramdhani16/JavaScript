# Meminta pengguna memasukkan dua bilangan
bilangan1 = float(input("Masukkan bilangan pertama: "))
bilangan2 = float(input("Masukkan bilangan kedua: "))

# Meminta pengguna memasukkan simbol operasi matematika
simbol_operasi = input("Masukkan simbol operasi matematika (+, -, *, /): ")

# Melakukan operasi matematika sesuai simbol yang dimasukkan
if simbol_operasi == '+':
    hasil = bilangan1 + bilangan2
    print("Hasil penambahan:", hasil)
elif simbol_operasi == '-':
    hasil = bilangan1 - bilangan2
    print("Hasil pengurangan:", hasil)
elif simbol_operasi == '*':
    hasil = bilangan1 * bilangan2
    print("Hasil perkalian:", hasil)
elif simbol_operasi == '/':
    if bilangan2 == 0:
        print("Tidak dapat melakukan pembagian dengan nol")
    else:
        hasil = bilangan1 / bilangan2
        print("Hasil pembagian:", hasil)
    else:
        print("Operator matematika tidak valid. Gunakan operator (+, -, *, /).")

