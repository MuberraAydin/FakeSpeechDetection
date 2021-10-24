import wave
import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.fft import fft

file_name = []

def fft_show(signal):
    
    #fft 
    plt.figure(figsize=(30,20))
    plt.plot(signal, np.abs(fft(signal)))
    plt.show() 
    
for i in range(1000001, 1000219):
    #dosyaları isimlendirir
    file_name.append('./dev/D_{0}.wav'.format(i))

for i in range(0, len(file_name)):
    
    #Dosya ismi yoksa diğer dosyaya atlar
    if not os.path.isfile(file_name[i]):
        continue
    #dosyayı açar
    wavefile = wave.open(file_name[i], "r")
    #bir nesne olarak ses karesini okur e döndürür (byte)
    signal = wavefile.readframes(-1)
    #integer'a çevirir
    signal = np.frombuffer(signal, dtype = "int")
    #örnekleme frekansını alır
    fs = wavefile.getframerate()
    #ses dosyasının süresini verir
    Time=np.linspace(0, len(signal)/fs, num=len(signal))
    
    #sinyal grafiğini çizer
    plt.figure(figsize=(30,20))
    plt.title('Signal Wave')
    #zamana bağlı çizer (Time kaldırılırsa frekansa bağlı çizer)
    plt.plot(signal)
    plt.show()
    
    fft_show(signal)
