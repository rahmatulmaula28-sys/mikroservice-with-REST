## Langkah Pengecekan Program

### 1. Masuk ke Folder Project

<p align="justify">Pertama, buka PowerShell melalui Visual Studio Code, kemudian masuk ke folder project yang sudah dibuat. Gunakan perintah berikut:</p>

```text
cd "D:\semester5\Pradigma sistem untukTI\monolith_microservices"
```

<p align="justify">Setelah masuk ke folder project, aktifkan virtual environment dengan perintah:</p>

```text
.\venv\Scripts\Activate.ps1
```

<p align="justify">Jika berhasil, pada bagian awal terminal akan muncul tulisan <b>(venv)</b>. Artinya virtual environment sudah aktif dan program siap dijalankan.</p>

### 2. Menjalankan Program Monolith

<p align="justify">Selanjutnya, buka Terminal 1 dan jalankan program Monolith dengan perintah:</p>

```text
python .\monolith_app.py
```

<p align="justify">Jika program berhasil dijalankan, akan muncul keterangan bahwa aplikasi berjalan pada port 5000, seperti <b>http://127.0.0.1:5000</b>. Pada tahap ini berarti program Monolith sudah aktif.</p>

### 3. Mengecek Data Buku

<p align="justify">Setelah Monolith berjalan, buka Terminal 2 untuk melakukan pengecekan. Masuk ke folder project dan aktifkan kembali virtual environment:</p>

```text
cd "D:\semester5\Pradigma sistem untukTI\monolith_microservices"
.\venv\Scripts\Activate.ps1
```

<p align="justify">Kemudian jalankan perintah berikut untuk melihat data buku yang tersedia:</p>

```text
curl.exe http://localhost:5000/books
```

<p align="justify">Jika berhasil, akan muncul data buku seperti berikut:</p>

```text
[
  {
    "id": 1,
    "stock": 5,
    "title": "Belajar Flask"
  }
]
```

<p align="justify">Dari hasil tersebut dapat dilihat bahwa data buku berhasil ditampilkan. Jadi, bagian untuk mengambil data buku pada program Monolith sudah berjalan dengan baik.</p>

### 4. Menyiapkan Data untuk Order

<p align="justify">Sebelum melakukan pemesanan, buat terlebih dahulu file <b>data.json</b> yang berisi ID buku yang ingin dipesan. Jalankan perintah berikut:</p>

```text
Set-Content -Path data.json -Value '{"book_id":1}' -Encoding utf8
```

<p align="justify">Untuk memastikan datanya sudah benar, cek isi file dengan perintah:</p>

```text
Get-Content data.json
```

<p align="justify">Jika tampil seperti berikut, berarti data sudah siap digunakan:</p>

```text
{"book_id":1}
```

### 5. Mengecek Proses Order pada Monolith

<p align="justify">Selanjutnya lakukan pemesanan buku dengan mengirimkan file <b>data.json</b> ke endpoint order:</p>

```text
curl.exe -X POST -H "Content-Type: application/json" --data-binary "@data.json" http://localhost:5000/orders
```

<p align="justify">Jika berhasil, akan muncul hasil seperti:</p>

```text
{
  "book_id": 1,
  "id": 1,
  "status": "berhasil"
}
```

<p align="justify">Hasil tersebut menunjukkan bahwa order berhasil dibuat. ID buku yang dipesan adalah 1 dan status order menunjukkan <b>berhasil</b>.</p>

### 6. Mengecek Perubahan Stok

<p align="justify">Setelah order berhasil, cek kembali data buku untuk melihat apakah stoknya berubah:</p>

```text
curl.exe http://localhost:5000/books
```

<p align="justify">Hasilnya akan menunjukkan stok buku yang sebelumnya 5 menjadi 4:</p>

```text
[
  {
    "id": 1,
    "stock": 4,
    "title": "Belajar Flask"
  }
]
```

<p align="justify">Dari hasil ini dapat dilihat bahwa setelah satu buku dipesan, stok berkurang dari 5 menjadi 4. Berarti proses order pada Monolith berhasil dan perubahan stok juga berjalan sesuai dengan program.</p>

## Pengecekan Microservices

### 7. Menjalankan Book Service

<p align="justify">Setelah pengecekan Monolith selesai, selanjutnya masuk ke bagian Microservices. Pada bagian ini terdapat dua service yang dijalankan secara terpisah, yaitu Book Service dan Order Service.</p>

<p align="justify">Buka Terminal 3, kemudian masuk ke folder project dan jalankan Book Service:</p>

```text
cd "D:\semester5\Pradigma sistem untukTI\monolith_microservices"
.\venv\Scripts\Activate.ps1
python .\book_service.py
```

<p align="justify">Jika berhasil, akan muncul keterangan bahwa Book Service berjalan pada port 5001. Berarti service buku sudah aktif dan bisa menerima permintaan.</p>

### 8. Mengecek Book Service

<p align="justify">Buka Terminal 4 untuk mengecek apakah Book Service benar-benar bisa diakses. Aktifkan virtual environment terlebih dahulu:</p>

```text
cd "D:\semester5\Pradigma sistem untukTI\monolith_microservices"
.\venv\Scripts\Activate.ps1
```

<p align="justify">Kemudian jalankan:</p>

```text
curl.exe http://localhost:5001/books
```

<p align="justify">Jika berhasil, data buku akan muncul seperti:</p>

```text
[
  {
    "id": 1,
    "stock": 5,
    "title": "Belajar Flask"
  }
]
```

<p align="justify">Artinya Book Service sudah berjalan dengan baik dan data buku dapat diakses secara terpisah melalui port 5001.</p>

### 9. Menjalankan Order Service

<p align="justify">Selanjutnya buka Terminal 5 untuk menjalankan Order Service. Gunakan perintah:</p>

```text
cd "D:\semester5\Pradigma sistem untukTI\monolith_microservices"
.\venv\Scripts\Activate.ps1
python .\order_service.py
```

<p align="justify">Jika berhasil, Order Service akan berjalan pada port 5002. Jadi, sekarang Book Service berjalan di port 5001 dan Order Service berjalan di port 5002.</p>

### 10. Mengecek Order pada Microservices

<p align="justify">Sebelum melakukan pengujian, pastikan file <b>data.json</b> masih tersedia. Cek menggunakan:</p>

```text
Get-Content data.json
```

<p align="justify">Jika datanya masih <b>{"book_id":1}</b>, lanjutkan dengan melakukan order melalui Order Service:</p>

```text
curl.exe -X POST -H "Content-Type: application/json" --data-binary "@data.json" http://localhost:5002/orders
```

<p align="justify">Jika berhasil, hasilnya akan seperti berikut:</p>

```text
{
  "book_id": 1,
  "id": 1,
  "status": "berhasil"
}
```

<p align="justify">Dari hasil tersebut dapat dilihat bahwa Order Service berhasil menerima permintaan order. Dalam prosesnya, Order Service meminta informasi buku kepada Book Service melalui HTTP. Jika buku tersedia, order akan dibuat.</p>

## Pengecekan Ketika Book Service Dimatikan

### 11. Menghentikan Book Service

<p align="justify">Untuk melihat bagaimana Microservices menangani ketika salah satu service mengalami gangguan, kembali ke Terminal 3 yang sedang menjalankan Book Service. Kemudian tekan <b>Ctrl + C</b> untuk menghentikannya.</p>

<p align="justify">Setelah dihentikan, Book Service sudah tidak berjalan. Namun, Order Service pada Terminal 5 tetap dibiarkan berjalan.</p>

### 12. Mengecek Order Setelah Book Service Dimatikan

<p align="justify">Sekarang coba lakukan order lagi melalui Order Service dengan perintah:</p>

```text
curl.exe -X POST -H "Content-Type: application/json" --data-binary "@data.json" http://localhost:5002/orders
```

<p align="justify">Karena Book Service sudah dihentikan, hasil yang muncul adalah:</p>

```text
{
  "error": "Book Service sedang down!"
}
```

<p align="justify">Dari hasil pengujian tersebut dapat dilihat bahwa Order Service masih berjalan meskipun Book Service sudah dihentikan. Order Service tidak ikut mati, tetapi memberikan pesan bahwa Book Service sedang tidak tersedia. Pengujian ini memperlihatkan konsep <i>fault isolation</i> pada arsitektur Microservices, yaitu setiap service dapat berjalan secara terpisah sehingga gangguan pada satu service tidak langsung menghentikan service lainnya. 