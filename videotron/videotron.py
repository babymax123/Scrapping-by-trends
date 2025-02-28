from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt
import time

# Inisialisasi Pytrends
pytrends = TrendReq(hl='id', tz=360)

# Kata kunci pencarian
kw_list = ["videotron"]

# Daftar provinsi di Pulau Jawa
province_codes = {
    "Jakarta": "ID-JK",
    "Jawa Barat": "ID-JB",
    "Jawa Tengah": "ID-JT",
    "Jawa Timur": "ID-JI",
    "Banten": "ID-BT",
    "Yogyakarta": "ID-YO"
}

# Dictionary untuk menyimpan data tren per provinsi
data_provinsi = {}

# Looping untuk mendapatkan data tiap provinsi
for province_name, province_code in province_codes.items():
    try:
        # Bangun payload untuk provinsi tertentu
        pytrends.build_payload(kw_list, timeframe='now 7-d', geo=province_code, gprop='')
        
        # Ambil data tren per jam
        df_hourly = pytrends.interest_over_time()
        
        # Cek apakah kolom "running text" tersedia
        if "videotron" in df_hourly.columns:
            # Filter hanya data dengan nilai > 0
            df_hourly = df_hourly[df_hourly["videotron"] > 0]
            
            if not df_hourly.empty:
                data_provinsi[province_name] = df_hourly
                
                # Simpan data ke CSV per provinsi
                csv_filename = f"tren_videotron_{province_name}.csv"
                df_hourly.to_csv(csv_filename, index=True)
                print(f"Data tren di {province_name} telah disimpan ke dalam file: {csv_filename}")
            else:
                print(f"Data tren di {province_name} kosong setelah filter.")
        else:
            print(f"Tidak ada data untuk keyword 'videotron' di {province_name}")
    
    except pytrends.exceptions.TooManyRequestsError as e:
        print(f"TooManyRequestsError pada {province_name}. Menunggu 60 detik sebelum mencoba lagi...")
        time.sleep(60)
        # Setelah delay, Anda bisa mencoba kembali atau melewati provinsi ini
        continue
    except Exception as e:
        print(f"Error saat mengambil data untuk {province_name}: {e}")
    
    # Tambahkan delay antar request untuk menghindari rate limiting
    time.sleep(10)

# Plot hasil tren pencarian per provinsi (hanya yang memiliki data)
if data_provinsi:
    plt.figure(figsize=(14, 8))
    for province_name, df_hourly in data_provinsi.items():
        plt.plot(df_hourly.index, df_hourly["videotron"], label=province_name)
    
    plt.xlabel("Waktu (Per Jam)")
    plt.ylabel("Tren Pencarian")
    plt.title("Tren Pencarian 'videotron' per Jam di Provinsi Pulau Jawa")
    plt.xticks(rotation=45, ha="right")
    plt.legend()
    plt.grid()
    plt.show()
else:
    print("Tidak ada data yang dapat diplot.")

# Menampilkan 5 data terbaru dari masing-masing provinsi yang memiliki data
for province_name, df_hourly in data_provinsi.items():
    print(f"\nData tren pencarian per jam di {province_name}:")
    print(df_hourly.tail(5))
