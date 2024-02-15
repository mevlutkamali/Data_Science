    
    # Libraries.
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    
    source = pd.read_csv('sales.csv')
    print(source)
    
    # Verileri gruplara ayırdık.
    months = source[['Aylar']]
    print(months)
    
    sale = source[['Satislar']]
    print(sale)
    
    # Veri ön işleme kodları. 
    from sklearn.model_selection import train_test_split
    
    x_train, x_test, y_train, y_test = train_test_split(months, sale, test_size=0.33, random_state=0)
    
    '''
    from sklearn.preprocessing import StandardScaler
     
    sc = StandardScaler()
    
    X_train = sc.fit_transform(x_train)
    X_test = sc.fit_transform(x_test)
    
    Y_train = sc.fit_transform(y_train)
    Y_test = sc.fit_transform(y_test)
    '''
    
    # Model inşası (Linear Regression).
    from sklearn.linear_model import LinearRegression
    
    lr = LinearRegression()
    
    # X_train ile Y_traini tahmin etmeye çalıştırıyoruz.
    lr.fit(x_train, y_train)
    
    # Tahmin işlemleri.
    guess = lr.predict(x_test)
    
# Burada veiyi ön işleyerek yakın tahminler elde ettik.
    
    # x_train ve y_train içerisinde bulunan karışık verilerin index ' e göre sırlanması için kod bloğu.
    x_train = x_train.sort_index()
    y_train = y_train.sort_index()

    # Burada veri ' yi görselleştirme aşamasını kodluyoruz.
    plt.plot(x_train, y_train) 
    plt.plot(x_test,lr.predict(x_test))
    
    plt.title('Aylara Göre Satış')
    plt.xlabel('Aylar')
    plt.ylabel('Satışlar')
    
'''
NOT: 
     Burada tüm veriler çizilmiyor 20. satırda verileri bölerken 0.67 kısımın çizimini bize sunuyor.
'''

    print('\n Finish. . .')
    