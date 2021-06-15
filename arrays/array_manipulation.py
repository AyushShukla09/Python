'''
Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in the array.

Example

n=  1
queries =
    a b k
    1 5 3
    4 8 7
    6 9 1
index->	 1 2 3  4  5 6 7 8 9 10
	    [0,0,0, 0, 0,0,0,0,0, 0]
	    [3,3,3, 3, 3,0,0,0,0, 0]
	    [3,3,3,10,10,7,7,7,0, 0]
	    [3,3,3,10,10,8,8,8,1, 0]

'''



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
