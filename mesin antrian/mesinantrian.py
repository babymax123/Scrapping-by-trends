from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt

# Inisialisasi Pytrends
pytrends = TrendReq(hl='id', tz=360)

# Kata kunci pencarian
kw_list = ["mesin antrian"]

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
    # Bangun payload untuk provinsi tertentu
    pytrends.build_payload(kw_list, timeframe='now 7-d', geo=province_code, gprop='')
    
    # Ambil data tren per jam
    df_hourly = pytrends.interest_over_time()
    
    # Cek apakah kolom "mesin antrian" ada dalam DataFrame
    if "mesin antrian" in df_hourly.columns:
        # Filter hanya data yang memiliki nilai non-zero
        df_hourly = df_hourly[df_hourly["mesin antrian"] > 0]
        
        if not df_hourly.empty:
            # Simpan data ke dictionary
            data_provinsi[province_name] = df_hourly

            # Simpan ke CSV per provinsi
            csv_filename = f"tren_mesin_antrian_{province_name}.csv"
            df_hourly.to_csv(csv_filename, index=True)
            print(f"Data tren di {province_name} telah disimpan ke dalam file: {csv_filename}")
        else:
            print(f"Data tren di {province_name} kosong setelah filter.")
    else:
        print(f"Tidak ada data untuk keyword 'mesin antrian' di {province_name}")

# Plot hasil tren pencarian per provinsi (hanya yang memiliki data)
if data_provinsi:
    plt.figure(figsize=(14, 8))
    for province_name, df_hourly in data_provinsi.items():
        plt.plot(df_hourly.index, df_hourly["mesin antrian"], label=province_name)
    
    plt.xlabel("Waktu (Per Jam)")
    plt.ylabel("Tren Pencarian")
    plt.title("Tren Pencarian 'mesin antrian' per Jam di Provinsi Pulau Jawa")
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
