import numpy as np
import array

#Ahmet Semiz (GitHub: muhendis385)
#NumPy Özet Bilgiler

def GİRİS():
    print("NumPy Özet Bilgiler")

def C_ve_F_Duzeni():
    #Satır bazlı işlemler için C-order, Sütun bazlı işlemler için F-order kullanılmalıdır.
    arr = np.array([1,2,3,4,5,6])
    print("Order da C ve F düzeni farkı")
    C = np.reshape(arr, (2, 3), 'C') #Önce Satır doldurulur.
    print(C,"\n")
    F = np.reshape(arr,(2,3),'F')    #Önce Sütun doldurulur.
    print(F)
def numpy_pratics():
    try:
        arr1 = np.array([[1,2,3],[3,4,5]],dtype= np.float64)
        arr2 = np.array([[10,20,30],[30,40,50]], dtype= np.float64)
        print(arr1)
        print()
        print(arr1.T) #Transpose
        print()
        print(np.sum(arr1)) #Sum (Toplama)
        print()
        print(np.sqrt(arr1)) #Sqrt (Kök Alma)
        print()
        print(np.add(arr1, arr2))  # Add Matristeki öğeleri girdi girdi toplar.
    except ValueError:
        print("UYARI!!! Boyutları farklı olan matrisler toplanamaz!")
def shape():
    list1 = [1,2,3,4]
    list2 = [4,5,6,5]
    list3 = [7,8,9,4]
    matris3d = np.array([list1,
                         list2,
                         list3])
    print("3d matris \n ---------")
    print(matris3d)
    print("boyutu nedir (satır,sütun):",matris3d.shape) #3x4
def dtype():
    # Doğru bellek seçmek, bilgisayarın performasını artırır.
    sample_array_1 = np.array([[0, 4, 2]])
    sample_array_2 = np.array([0.2, 0.4, 2.4])

    print("Data type of the array 1 :",sample_array_1.dtype)
    print("Data type of array 2 :",sample_array_2.dtype)
def fromiter():
    iterable = (a*a for a in range(8))
    arr = np.fromiter(iterable,float)
    print("fromiter()array:",arr) #fromiter()array: [ 0.  1.  4.  9. 16. 25. 36. 49.]
    #float yazınca sayıların yanına nokta kondu. int olsaydı noktasız olurdu.

    var = "Python"
    arr = np.fromiter(var,dtype="U16")
    print("fromiter()array:",arr) #fromiter()array: ['P' 'y' 't' 'h' 'o' 'n']
    print(arr.dtype)              #
def arange():
    arr = np.arange(1,20,2,dtype=np.int64)
    print("int64",arr)
    arr = np.arange(1, 20, 2, dtype=np.int32)
    print("int32",arr)
    #int64 ve int32 arasında bellek kullanımı açısından fark vardır, görünür de değil.
def linspace():
    arr = np.linspace(3.5,10,3,dtype=np.float64)
    #3.5'den başlayıp 10'kadar 3 sayı döndürür.
    print(arr)
def empty():
    arr = np.empty([4,3],dtype=np.int64, order='f')
    print(arr)
    #4x3 boyutlarında boş bir dizi oluşturur ve order='f' nedeniyle sütun düzeninde saklanır.
    # Ancak dizinin başlangıç değerleri rastgele olacaktır.
def ones():
    arr = np.ones([3,3],dtype=np.int32, order='C')
    print(arr) #belirtilen boyuta 1'leri doldurur.
def zeros():
    arr = np.zeros([3,4],dtype=np.float32, order ='F')
    print(arr) #belirtilen boyuta 0'ları doldurur.
def dtype_ogrenme():
    arr = np.array([1.0,2.0,4.0])
    arr1 = np.array([1,2,4])
    print(arr,arr.dtype)
    print(arr1,arr1.dtype)
                     #int >>> int64
                     #float >>> float64
    #bilgisayara göre sonuçlar değişebilir.
def yapilandirilmis_diziyle_dtype():
    dt = np.dtype([('name', np.str_, 16), ('grades', np.float64, (2,))]) #np.unicode_ yerine np.str_ kullanıldı.
    x = np.array([('Sarah', (8.0, 7.0)), ('Ali', (6.0, 7.0))], dtype=dt)
    print(x[1])
    print("Grades of Ali:",x[1]['grades'])
    print("Names:",x['name'])
    print()
    print(dt['grades']) #<f8 float64 anlamına gelir. (2,) ise matrisin tek boyutlu olduğunu belirtir.
    print(dt['name'])   # <U16, Bellekte 16 karakterlik yer ayırıldığını söyler.
def ozel_islevlerle_dizi_olusturma():
    zeros_array = np.zeros((2, 3))
    ones_array = np.ones((3, 3))
    constant_array = np.full((2, 2), 7) #belirtilen boyuta, değer doldurulur.
    range_array = np.arange(0, 10, 2)
    linspace_array = np.linspace(0, 1, 5) #0 ile 1 arasına 5 sayı sıkıştırılır.
    print("Zeros Array:\n",zeros_array)
    print("Ones Array:\n",ones_array)
    print("Constant Array:\n",constant_array)
    print("Range Array\n",range_array)
    print("Linspace Array\n",linspace_array)
def reshape():
    arr = [1, 2, 3, 4, 5, 6]
    print(arr)
    print("Sonrası")
    reshaped_arr = np.reshape(arr, (2, 3))  # arr dizisini 2x3 boyutunu döndür.
    print(reshaped_arr)
    reshaped_arr1 = np.reshape(arr, (-1,2)) # -1 ile satır sayısını otomatik olarak ayarlamasını isteriz.
    print("Sütunu söyleyip Satırı ayarlasın dersek;")
    print(reshaped_arr1)
def array_and_random():
    a = np.random.rand(3,4) #0 ve 1 arasındaki sayıları belirtilen boyuta doldurur.
    print(a)
    b = np.random.randn(2,3) #belirtilen şekilde oluşan bir dizi oluşturur,
    # bunu, standart bir normal dağılımdan örneklenen rastgele değerlerle doldurur.
    print()
    print(b)
    print()
    c = np.random.randint(1,10,size=(2,3))  #low ve high sınırlar, size ise matris boyutu.
    print(c)


#calistirmak istenilen fonksiyonu yaz
GİRİS()



