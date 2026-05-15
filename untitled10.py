def solve_arrays():
    # Test uchun namuna massivlar
    data26 = [2, 3, 4, 5, 8, 10] # 4-indeksda buzilgan (8 - juft, 10 ham juft)
    data27 = [1, -2, 3, -4, 5]    # Hammasi joyida (0 qaytaradi)
    data28 = [10, 5, 2, 8, 1, 9]  # Juft indekslar: 10, 2, 1 -> min: 1
    data29 = [1, 15, 3, 25, 5, 10] # Toq indekslar: 15, 25, 10 -> max: 25
    data30 = [5, 2, 8, 4, 3, 10, 1] 

    # --- Array26 ---
    def array26(arr):
        for i in range(1, len(arr)):
            if (arr[i-1] % 2 == arr[i] % 2):
                return i
        return 0

    # --- Array27 ---
    def array27(arr):
        for i in range(1, len(arr)):
            if (arr[i-1] * arr[i] > 0):
                return i
        return 0

    # --- Array28 ---
    def array28(arr):
        return min(arr[::2])

    # --- Array29 ---
    def array29(arr):
        return max(arr[1::2])

    # --- Array30 ---
    def array30(arr):
        indices = [i for i in range(len(arr)-1) if arr[i] > arr[i+1]]
        return indices, len(indices)

    # Natijalarni chiqarish
    print(f"Array26 natijasi: {array26(data26)}")
    print(f"Array27 natijasi: {array27(data27)}")
    print(f"Array28 natijasi: {array28(data28)}")
    print(f"Array29 natijasi: {array29(data29)}")
    
    idx, count = array30(data30)
    print(f"Array30: Indekslar = {idx}, Soni = {count}")

# Dasturni ishga tushirish
if __name__ == "__main__":
    solve_arrays()
