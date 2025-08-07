def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # En küçük elemanı bulunup baştaki elemanla değiştirilir
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Örnek kullanım
liste = [29, 10, 14, 37, 13]
print("Sıralanmadan önce:", liste)
selection_sort(liste)
print("Sıralandıktan sonra:", liste)
