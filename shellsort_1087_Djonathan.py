def shellSort(arr):
    
    gap = len(arr) // 2
    while gap > 0:
        for awalstart in range(gap):
            for i in range(awalstart + gap, len(arr), gap):
                nilai_sekarang = arr[i]
                posisi = i

                while posisi >= gap and arr[posisi - gap] > nilai_sekarang:
                    arr[posisi] = arr[posisi - gap]
                    posisi -= gap

                arr[posisi] = nilai_sekarang
        gap = gap // 2

data = [35, 14, 33, 19, 42, 27, 10, 44]
print('Data sebelum : ',data)
shellSort(data)
print('Data sesudah : ',data)