import wave
import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.io import wavfile
from scipy.fftpack import fft
from python_speech_features import mfcc
import csv
import pandas as pd

#cepstrum sayısı sabitini ve wav dosya ismini alır
def wav_to_mfcc(wav_filename, num_cepstrum):
    
    #yeniden okuma yapıyor
    (rate, sig) = wavfile.read(wav_filename)
    #mfcc özelliklerini çıkartır
    mfcc_features = mfcc(sig, rate, numcep=num_cepstrum)
    return mfcc_features
    

file_name = []
mfcc_array = []
csv_array = []

def fft_show(signal):
    
    #fft 
    plt.figure(figsize=(30,20))
    plt.plot(signal, np.abs(fft(signal)))
    plt.show() 

def show_graph(wavfile, signal):
    #örnekleme frekansını alır
    fs = wavefile.getframerate()
    #ses dosyasının süresini verir
    Time=np.linspace(0, len(signal)/fs, num=len(signal))
    
    #sinyal grafiğini çizer
    plt.figure(figsize=(30,20))
    plt.title('Signal Wave')
    #zamana bağlı çizer (Time kaldırılırsa frekansa bağlı çizer)
    plt.plot(Time, signal)
    plt.show()

##dev: 1000001, 1001710, eval: 1000001, 1014219, train:1000001, 1003016
for i in range(1000001, 1014219):
    
    #dosyaları isimlendirir
    file_name.append('./eval/E_{0}.wav'.format(i))

j=0
for i in range(0, len(file_name)):
    
    
    #Dosya ismi yoksa diğer dosyaya atlar
    if not os.path.isfile(file_name[i]):
        continue
    #dosyayı açar
    wavefile = wave.open(file_name[i], "r")
    #bir nesne olarak ses karesini okur e döndürür (byte)
    signal = wavefile.readframes(-1)
    #integer'a çevirir
    signal = np.frombuffer(signal, dtype = "Int16")
    #show_graph(wavfile, signal)
    
    #mfcc özelliklerini diziye atar
    mfcc_array.insert(j, wav_to_mfcc(file_name[i], 13))
    #print(mfcc_array[j])
    j+=1

new_array = []
temp = []
csv_array = []
columns = []
tut = 0.0
basla = 0
sutun=['V1','V2','V3','V4','V5','V6','V7','V8','V9','V10','V11','V12', 'V13', 'dosya', 'gercekmi']
dev = pd.read_csv('dev.csv')
train = pd.read_csv('train.csv')
eval1 = pd.read_csv('eval.csv')
with open('eval_new.csv', mode='w') as yeni_dosya:
    yeni_yazici = csv.writer(yeni_dosya, delimiter=',',quoting=csv.QUOTE_ALL)
    yeni_yazici.writerow(sutun)
    
    #print("mfcc_arr[0][0]: ", len(mfcc_array[0][0]))
    for j in range(0, len(mfcc_array)):
        for k in range(0, len(mfcc_array[j][0])):      
            #print("k: ", k)
            for n in range(0,(len(mfcc_array[j]))):
                #print("mfcc: ", mfcc_array[0][n][k])
                tut=mfcc_array[j][n][k]
                csv_array.insert(k, tut)
            columns.append(sum(csv_array)/len(mfcc_array[j]))
            csv_array.clear()
        columns.append(eval1['dosya'][basla])
        columns.append(eval1['gercekmi'][basla])
        basla+=1
        new_array.append(columns)
        yeni_yazici.writerow(new_array[j])
        columns.clear()
    
df=pd.read_csv('eval_new.csv')
print(df)
