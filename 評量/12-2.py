#請寫出下列程式的輸出結果，並說明為什麼。
A = [0 for x in range(3)]
arr = [A for y in range(3)]
arr[0][0] = 9
print(arr)

#若要讓 arr[0][0] = 9 時只改動第一列，程式應該怎麼寫？
#應該這樣寫：
A = [0 for x in range(3)]
arr = [[A[i] for i in range(3)] for y in range(3)]
arr[0][0] = 9
print(arr)