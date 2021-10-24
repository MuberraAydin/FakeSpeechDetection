def knn_hesapla():
    # KNeighborsClassifier sınıfını import ettik
    from sklearn.neighbors import KNeighborsClassifier
    
    # KNeighborsClassifier sınıfından bir nesne ürettik
    # n_neighbors : K değeridir. Bakılacak eleman sayısıdır. Default değeri 5'tir.
    # metric : Değerler arasında uzaklık hesaplama formülüdür.
    # p : Alternatif olarak p parametreside verilir.
    classifier = KNeighborsClassifier(n_neighbors=8, metric='minkowski', p = 2)
    
    # Makineyi eğitiyoruz
    classifier.fit(x_train, y_train)
    
    # Test veri kümemizi verdik ve tahmin etmesini sağladık
    y_pred = classifier.predict(x_test)
    
    # Karmaşıklık matrisi
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_test,y_pred)
    print(cm)
    
    # Başarı Oranı
    from sklearn.metrics import accuracy_score
    accuracy = accuracy_score(y_test, y_pred)
    print("knn: ",accuracy)

def svm_hesapla():
    
    from sklearn.svm import SVC
    classifier = SVC(kernel='linear', random_state = 0)
    classifier.fit(x_train, y_train)
    
    y_pred = classifier.predict(x_test)
    
    # Karmaşıklık matrisi
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_test,y_pred)
    print(cm)
    
    # Başarı Oranı
    from sklearn.metrics import accuracy_score
    accuracy = accuracy_score(y_test, y_pred)
    print("svm: ",accuracy)


# csv dosyalarını okumak için
import pandas as pd

# csv dosyamızı okuduk.
dataset = pd.read_csv('train_new.csv')

x_train = dataset.iloc[:, [0,1,2,3,4,5,6,7,8,9,10,11,12]].values

# Bağımlı Değişkeni bir değişkene atadık
y_train = dataset.iloc[:, 14].values

# csv dosyamızı okuduk.
dataset = pd.read_csv('eval_new.csv')

x_test = dataset.iloc[:, [0,1,2,3,4,5,6,7,8,9,10,11,12]].values

# Bağımlı Değişkeni bir değişkene atadık
y_test = dataset.iloc[:, 14].values

# sc_X = StandardScaler()
# x_train = sc_X.fit_transform(x_train)
# x_test = sc_X.transform(x_test)

knn_hesapla()
svm_hesapla()

