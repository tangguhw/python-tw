
from glob import glob
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression



# nama file hanya yang berbentuk angka  "200515" => 2020/05/15
# ".." itu karena direktori di atas ini
f = glob("../[0-9][0-9][0-9][0-9][0-9][0-9]")
dir = sorted(f, reverse=True)[0]


#print(dir)
# karena format dir adalah "../200515" - sesuaikan dengan lokasi direktori
# maka ambil tanggal dari nama direktori tersebut

#tanggal = dir[7:9] + "/" + dir[5:7] + "/20" + dir[3:5]
#print(dir[7:9])
#print(dir[5:7])
#print(dir[3:5])
#print(tanggal)

# ambil nama file
data_tabel_aktif = glob(dir + "/" + "csv_tabel_aktif_*")[0]
data_tabel_konfirmasi_kasus = glob(dir + "/" + "csv_tabel_confirmed_cases_*")[0]
data_tabel_meninggal = glob(dir + "/" + "csv_tabel_meninggal_*")[0]
data_tabel_sembuh = glob(dir + "/" + "csv_tabel_sembuh_*")[0]
data_tabel_prediksi = glob(dir + "/" + "csv_for_prediction_cases_*")[0]


print("Pilih kasus covid yang ingin di visualisasikan")
print("1. Confirmed")
print("2. Meninggal")
print("3. Sembuh")
print("4. Semua Kasus")
print("5. Prediksi Kenaikan Kasus")

pilihan = int(input("Masukkan pilihan anda : "))

if pilihan == 1:
    try:
       df = pd.read_csv(data_tabel_konfirmasi_kasus)
       print(df.head())
    except:
       print("Cannot open " + data_tabel_konfirmasi_kasus)

    # convert the column to datetime
    df['Datetime'] = pd.to_datetime(df['Tanggal'])
    print("Hasil convert date time")
    print(df.Datetime)
    
    
    #df.info()
    
    ax = df.plot(x='Datetime', y='CentralJava')
    plt.grid(True)
    judul = "Confirmed Cases di Daerah Jawa Tengah sd.29 Oct 2020 " #+ #tanggal
    plt.title(judul)
    plt.xlabel('Tanggal')
    plt.ylabel("Jumlah")

   
    
   
    
elif pilihan == 2:
    print("Data meninggal")
    try:
       df = pd.read_csv(data_tabel_meninggal)
       print(df.head())
    except:
       print("Cannot open " + data_tabel_meninggal)

    # convert the column to datetime
    df['Datetime'] = pd.to_datetime(df['Tanggal'])
    print("output hasil convert date time")
    print(df.Datetime)

    

    ax = df.plot(x='Datetime', y='CentralJava')

    plt.grid(True)

    judul = "Jumlah Meninggal COVID-19 di Daerah Jawa Tengah sd. 29 Oct 2020" #+ #tanggal
    plt.title(judul)
    plt.xlabel('Tanggal')
    plt.ylabel("Jumlah")

elif pilihan == 3:
    print("Data Sembuh")
    try:
       df = pd.read_csv(data_tabel_sembuh)
       # print(df.head())
    except:
       print("Cannot open " + data_tabel_sembuh)

    # convert the column to datetime
    df['Datetime'] = pd.to_datetime(df['Tanggal'])
    print(df.Datetime)

    

    ax = df.plot(x='Datetime', y='CentralJava')

    plt.grid(True)

    judul = "Jumlah Sembuh COVID-19 di Daerah Jawa Tengah sd. 29 Oct 2020" #+ #tanggal
    plt.title(judul)
    plt.xlabel('Tanggal')
    plt.ylabel("Jumlah")

elif pilihan == 4:
    print("Data Semua Kasus")
    try:
       df = pd.read_csv(data_tabel_aktif)
       dg = pd.read_csv(data_tabel_konfirmasi_kasus)
       dh = pd.read_csv(data_tabel_meninggal)
       di = pd.read_csv(data_tabel_sembuh)
       # print(df.head())
    except:
       print("Cannot open " + data_tabel_aktif)

    # convert the column to datetime
    df['Datetime'] = pd.to_datetime(df['Tanggal'])
    dg['Datetime'] = pd.to_datetime(dg['Tanggal'])
    dh['Datetime'] = pd.to_datetime(dh['Tanggal'])
    di['Datetime'] = pd.to_datetime(di['Tanggal'])
    print(df.Datetime)
    # add dg,dh,di to df
    df['Confirmed'] = dg['CentralJava']
    df['Meninggal'] = dh['CentralJava']
    df['Sembuh'] = di['CentralJava']
    #print(df[['Datetime', 'Jakarta', 'Confirmed', 'Meninggal', 'Sembuh']])

    df = df.rename(columns={'CentralJava':'Active'})

   

    ax = df.plot(x='Datetime', y=['Confirmed','Active', 'Sembuh', 'Meninggal'])

    plt.grid(True)

    judul = "COVID-19 di Jawa Tengah sd. 29 Oct 2020" #+ tanggal
    plt.title(judul)
    plt.xlabel('Tanggal')
    plt.ylabel("Jumlah")

elif pilihan == 5:
    print("Prediksi Kenaikan Kasus Covid-19")
    try:
        df = pd.read_csv(data_tabel_prediksi)
        df.head(226)
        #print(df.head())
    except:
        print("Cannot open " + data_tabel_prediksi)
    
    #create the lists or x and y data set
    dates = list()
    cases = list()
    
    df.shape
    
    df.tail(1)
    
    df.head(len(df)-1)
    df
    
    
    
    df.shape
    
    df_dates = df.loc[:, 'Tanggal']
    df_closes = df.loc[:, 'CentralJava']
    
    #Create the independent data set
    for date in df_dates:
        dates.append( [int(date.split('/')[1])] )
    #Create the dependent data set
    for close_cases in df_closes:
        cases.append( float(close_cases) )
        
    print(dates)
    
    