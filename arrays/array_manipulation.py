def arrayManipulation(n, queries):
    # Write your code here
    arr = [0] * (n + 2)
    count = 0
    for a, b, k in queries:
        count += 1
        arr[a] += k
        arr[b + 1] -= k

    sum = max = 0
    for i in range(len(arr)):
        sum += arr[i]
        if sum > max:
            max = sum
    return max


if '__name__' == '__main__':
    query = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
    array_length = 10
    value = arrayManipulation(array_length, query)
    print(value)
