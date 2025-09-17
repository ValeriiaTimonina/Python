def sortNumbers(data, condition):   
    if condition == 'ASC':
        for i in range(len(data)-1):
            for j in range(len(data)-i-1):
                if data[j] > data[j + 1]:
                    temp=data[j]
                    data[j]=data[j + 1]
                    data[j + 1]=temp
        return data     
    elif condition == 'DESC':
        for i in range(len(data)-1):
            for j in range(len(data)-i-1):
                if data[j] < data[j + 1]:
                    temp=data[j]
                    data[j]=data[j + 1]
                    data[j + 1]=temp
        return data     
 
 
def sortData(weights, data, condition):
    if (len(weights) != len(data)):
        raise ValueError('Invalid input data')
 
    pole = {}
    for i in weights:
        for j in data:
            pole[i] = j
           # data.remove(j)
            break 
 #   print(pole)
 
    if condition == 'ASC':
        for i in range(len(weights)-1):
            for j in range(len(weights)-i-1):
                if weights[j] > weights[j + 1]:
                    temp=weights[j]
                    temp2 = data[j]
                    weights[j]=weights[j + 1]
                    data[j]=data[j + 1]
                    weights[j + 1]=temp
                    data[j + 1]=temp2
    elif condition == 'DESC':
        for i in range(len(weights)-1):
            for j in range(len(weights)-i-1):
                if weights[j] < weights[j + 1]:
                    weights[j], weights[j+1] = weights[j+1], weights[j]
                    data[j], data[j+1] = data[j+1], data[j]
               
    return(data)
#print(sortData([5,2,6], ['Ford','BMW','Audi'], 'ASC'))
#print(sortData([3,2,4],['Ford','BMW','Audi'], 'DESC'))
#print(sortData([2, 3, 4, 4, 5, 19, 2, 1] , ['Praha', 'Brno', 'Pariz', 'Londyn', 'Bratislava', 'Pelhrimov', 'Jihlava', 'CB'], 'DESC'))