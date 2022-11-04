print ('WELCOME TO GIS 1 ATM')
print ('PILIH OPTION')
print ('1. Check uang nasabah')
print ('2. Ambil uang')
print ('3. Tabung uang')
option=int(input('silahkan pilih option : '))
uang_kamu=200000
if option==1:
     print('uang anda berjumlah Rp.200.000')
elif option==2:
  print('uang anda berjumlah Rp.200.000, mau ambil berapa?')
  print('1. Rp.100.000')
  print('2. Rp.200.000')
  option2=int(input('option:'))
  if option2==1:
    hasil=uang_kamu-100000
    print('uang kamu sekarang berjumlah ',hasil)
elif option2==2:
    hasil2=uang_kamu-200000
    print('uang kamu sekarang berjumlah ',hasil2)
else:
    print('keyboard anda salah, mohon ulangi lagi!')
elif option==3:
    print(uang anda berjumlah Rp.200.000, mau tabung berapa?)
    option3=int(input('masukan jumlah uang:'))
    hasil3=uang_kamu+option3
    print('jumlah uang kamu sekarang adalah',hasil3)
else:
    print("pilihan anda salah, silahkan ulangi lagi!!!")
    