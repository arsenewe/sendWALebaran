import pandas as pd
import pywhatkit as pw
import time

print("Kirim WA Lebaran")
time.sleep(1)

data = pd.read_csv('data_k.csv', delimiter=';', converters={'no_hp': str})

teks = "Assalamu'alaikum warahmatullahi wabarakatuh, mohon maaf lahir dan batin nggih {}."

for num, kontak in data.iterrows():
    print('Kirim pesan ke ', num+1)
    time.sleep(2)
    pw.sendwhatmsg_instantly(kontak.no_hp, teks.format(kontak.nama))
    print(kontak.no_hp, 'sukses')
    time.sleep(20)

print("Terkirim semua")
