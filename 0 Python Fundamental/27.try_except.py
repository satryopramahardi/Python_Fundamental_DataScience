
# try:
#     angka = int(input('Ketik angka: '))
#     print(angka)
# except:
#     print('Input bukan angka!')

# run & coba inputkan bukan angka

#####################################

try:
    nilai = 10/0
    angka = int(input('Ketik angka: '))
    print(angka)
except ZeroDivisionError:
    print('Tak bisa dibagi 0!')
except ValueError:
    print('Input bukan angka!')

#####################################


# try:
#     nilai1 = int(input('Ketik angka 1 : '))
#     nilai2 = int(input('Ketik angka 2 : '))
#     print(nilai1 / nilai2)
# except ValueError:
#     print('Maaf, hanya menerima input berupa angka')
# except ZeroDivisionError:
#     print('Jangan dibagi 0 dong!')
