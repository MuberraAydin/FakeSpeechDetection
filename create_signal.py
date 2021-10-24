import wave
import matplotlib.pyplot as plt
import numpy as np
import os

file_name = []
for i in range(1000001, 1014219):
    file_name.append('./eval/E_{0}.wav'.format(i))


for i in range(0, len(file_name)):

    #Dosya ismi yoksa diğer dosyaya atlar
    if not os.path.isfile(file_name[i]):
        i=i+1
    #dosyayı açar
    wavefile = wave.open(file_name[i], "r")
    #bir nesne olarak ses karesini okur e döndürür (byte)
    signal = wavefile.readframes(-1)
    #integer'a çevirir
    signal = np.frombuffer(signal, dtype = "Int16")
    #örnekleme frekansını alır
    fs = wavefile.getframerate()
    #ses dosyasının süresini verir
    Time=np.linspace(0, len(signal)/fs, num=len(signal))
 
    plt.figure(1)
    plt.title('Signal Wave')
    plt.plot(Time,signal)
    plt.show()