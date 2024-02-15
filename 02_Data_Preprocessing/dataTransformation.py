    
    # Libraries.
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    
    source = pd.read_csv('source.csv')
    print(source)
    
    country = source.iloc[:, 0:1].values
    print(country)
    
    from sklearn import preprocessing  
    
    le = preprocessing.LabelEncoder()
    country[:, 0] = le.fit_transform(source.iloc[:, 0])
    print(country)
    
    # Buradaki kod parçası ile varlıklarına dair bir dizi oluşturduk.
    countryLists = preprocessing.OneHotEncoder()
    country = countryLists.fit_transform(country).toarray()
    print(country)
    
    # İstenilen yerlerden veri çekmek için kullanabileçegimiz kod yapısı.
    print(list(range(22)))
    
    conclusion = pd.DataFrame(data=country, index=range(22), columns=['fr', 'tr', 'us'])
    print(conclusion)
    
    conclusion_2 = pd.DataFrame(data=source, index=range(22), columns=['boy', 'kilo', 'yas'])
    print(conclusion_2)
    
    conclusion_3 = pd.DataFrame(data=source, index=range(22), columns=['cinsiyet'])
    
    # pd.concat([]) fonk. ile verileri birleştirme işlemleri gerçleştirilir. axis=1 işlemi dataFrame ' leri birleştirme işlemleri yapıyor.
    u = pd.concat([conclusion, conclusion_2], axis=1)
    print(u)
    
    u2 = pd.concat([u, conclusion_3], axis=1)
    
    # Burada kodumuzu eğitim ve test olmak üzere ikiye bölcez.
    # x bağımlı değişken y bağımsız değişken.
    from sklearn.model_selection import train_test_split
    
    x_train, x_test, y_train, y_test = train_test_split(u, conclusion_3, test_size=0.33, random_state=0)
    
    # Veri ön işleme kodları. 
    from sklearn.preprocessing import StandardScaler
     
    sc = StandardScaler()
    
    X_train = sc.fit_transform(x_train)
    X_test = sc.fit_transform(x_test)
    
    print('\n Finish. . .')
    
