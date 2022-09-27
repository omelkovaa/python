A = [0, 2, 4, 6, 8, 10]
for i in range(len(A) - 1):
    B = A[1] - A[0]
    if A[i+1] - A[i] == B:
        continue
    else:
        C = 'Нет'
        print(C)
        break
if 'C' not in locals():
    print('Да')