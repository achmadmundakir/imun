nama = input("ahmad wangsul: ")
umur = int(input("18: "))
nilai_ipk = float(input("3.8: "))

# Kondisi syarat pendaftaran
if umur >= 18 and nilai_ipk >= 3.0:
    print("Selamat, Anda diterima sebagai mahasiswa baru!")
else:
    print("Maaf, Anda tidak memenuhi syarat pendaftaran.")