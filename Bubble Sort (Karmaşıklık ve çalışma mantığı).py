def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Her iterasyonda en büyük eleman sona yerleşir, dolayısıyla -i kadar azaltıyoruz
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Komşu elemanlar yer değiştirir
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Örnek kullanım
liste = [64, 34, 25, 12, 22, 11, 90]
print("Sıralanmadan önce:", liste)
bubble_sort(liste)
print("Sıralandıktan sonra:", liste)
