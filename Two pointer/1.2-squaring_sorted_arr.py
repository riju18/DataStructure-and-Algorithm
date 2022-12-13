arr = [-3, -1, 0, 1, 2]
n = len(arr)
squares = [0 for i in range(n)]
left, right = 0, n - 1
highest_square_ind = n - 1
while left <= right:
    leftVal = arr[left] * arr[left]
    rightVal = arr[right] * arr[right]
    if leftVal > rightVal:  # when sqr of most left > most right
        print(f"leftVal > rightVal, leftSqrVal: {leftVal}, rightSqrVal:{rightVal}")
        squares[highest_square_ind] = leftVal  # replace the most left sqr val to most right ind
        left += 1  # slide window
    else:  # for < or = to leftVal & rightVal
        squares[highest_square_ind] = rightVal
        right -= 1
    highest_square_ind -= 1  # every time moves backward by default
print(squares)
