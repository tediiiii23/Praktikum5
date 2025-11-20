print("\n================================")
print("Membuat Dictionary daftar kontak")
print("================================")

kontak = {
    "Tedi": "0812678888",
    "Adell": "087677776"
}

# Tampilkan kontaknya Tedi
print("Kontak Tedi:", kontak["Tedi"])

# Tambah kontak baru dengan nama Mhe
kontak["Mhe"] = "087654544"
print("\nSetelah menambah kontak Mhe:", kontak)

# Ubah kontak Adell dengan nomor baru
kontak["Adell"] = "088999776"
print("\nSetelah mengubah nomor Dina:", kontak)

# Tampilkan semua Nama
print("\nDaftar Nama:")
for nama in kontak.keys():
    print("-", nama)

# Tampilkan semua Nomor
print("\nDaftar Nomor:")
for nomor in kontak.values():
    print("-", nomor)

# Tampilkan daftar Nama dan nomornya
print("\nDaftar Nama dan Nomor:")
for nama, nomor in kontak.items():
    print(f"- {nama}: {nomor}")

# Hapus kontak Adell
del kontak["Adell"]
print("\nSetelah menghapus Adell:", kontak)
