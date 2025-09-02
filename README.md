# Date Converter

## Deskripsi
Aplikasi ini dibuat menggunakan **Streamlit** untuk melakukan konversi tanggal antara kalender **Gregorian** dan **Julian Day (JD)**.  
Tersedia dua mode konversi:  
1. Gregorian ke Julian Day  
2. Julian Day ke Gregorian  

Aplikasi ini juga sudah dilengkapi validasi tahun kabisat dan pemeriksaan tanggal agar tidak terjadi input yang salah.

---

## Cara Menjalankan
1. Pastikan Python sudah terinstall (disarankan Python 3.9 ke atas).  
2. Install library yang dibutuhkan:
   ```bash
   pip install streamlit
   ```
3. Jalankan aplikasi dengan perintah:
   ```bash
   streamlit run main.py
   ```

---

## Fitur Utama
- **Gregorian ke Julian Day**  
  Masukkan tanggal (hari, bulan, tahun) lalu aplikasi akan menghitung nilai Julian Day.  

- **Julian Day ke Gregorian**  
  Masukkan nilai Julian Day (misalnya 2460676.5) lalu aplikasi akan mengonversinya ke tanggal Gregorian.  

- **Validasi tanggal**  
  Aplikasi memeriksa apakah tanggal valid, terutama untuk bulan Februari pada tahun kabisat.

---

## Struktur Kode
- **Class `converter_date`**  
  Menangani logika perhitungan konversi tanggal.  
  - `ke_JD()` → Konversi tanggal Gregorian ke Julian Day  
  - `ke_Gregorian()` → Konversi Julian Day ke tanggal Gregorian  
  - `tahun_kabisat()` → Mengecek apakah tahun adalah tahun kabisat  

- **Streamlit UI**  
  Bagian utama aplikasi menggunakan `st.radio`, `st.form`, dan `st.success` untuk interaksi pengguna.

---

## Contoh Input & Output

### 1. Gregorian ke Julian Day
Input:  
```
Tanggal: 1 Januari 2025
```  
Output:  
```
Julian Day: 2460676.5
```  

### 2. Julian Day ke Gregorian
Input:  
```
Julian Day: 2460676.5
```  
Output:  
```
Tanggal: 1 Januari 2025
```
