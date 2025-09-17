def permutations(array):
    n = len(array) 
    all_lists = []
    def get_factorial(factorial, n):
        for i in range(n):
            factorial = factorial * (i+1)
        return factorial
    factorial = get_factorial(1, n)
    all_lists = [[] for i in range(factorial) ]
    if (n == 0):
        return all_lists
     
    def rec_perm(array, temp, all_lists, counter, n, depth):
        if (depth == n):
            for j in range(n):
                all_lists[counter].append(temp[j])
            counter += 1
            return all_lists, counter
        for i in range(n):
            if (array[i] in temp):
                continue
            temp[depth] = array[i]
            all_lists, counter = rec_perm(array, temp, all_lists, counter, n, depth+1)
            temp[depth] = None
        return all_lists, counter
    temp = [0 for i in range(n)]
    counter = 0
    rec_perm(array, temp, all_lists, counter, n, 0)
    return all_lists