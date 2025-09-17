def polyEval(poly, x):
    m = 0
    count=0
    for i in poly:
      count=count+1
    for i in range(count):
        m = m + poly[i]*(x**i)
    return m
 
def polySum(poly1, poly2):
    count1=0
    for i in poly1:
      count1=count1+1
    #print (count1)
    count2=0
    for i in poly2:
      count2=count2+1
    #print (count2)
 
    t = 1
    if count1 > count2:
        for i in range(count2):
            poly1[i] = poly1[i] + poly2[i]  
        while (len(poly1) - t >= 0) and (poly1[len(poly1)-t] == 0):
          del poly1[len(poly1)-t] 
          #t = t+2
        return poly1
 
    elif count1 < count2:
        for i in range(count1):
            poly2[i] = poly2[i] + poly1[i]
        while (len(poly2) - t >= 0) and (poly2[len(poly2)-t] == 0):
          del poly2[len(poly2)-t] 
          #t = t+1
        return poly2
 
    elif count1 == count2:
        for i in range(count2):
          poly1[i] = poly1[i] + poly2[i]  
        while (len(poly1) - t >= 0) and (poly1[len(poly1)-t] == 0):
          del poly1[len(poly1)-t] 
          #t = t+1
        return poly1
 
def polyMultiply(poly1, poly2):
    t = 1
    size = len(poly1)+len(poly2)
    poly3 = [0]*size
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            poly3[i + j] = poly1[i] * poly2[j] + poly3[i + j] #-20 -16 -12 -8 -4 0 0 0 0    -15 -12 -9 -6 -3 0    -20 -16 -12 -23 -16 -9 -6 -3 0
    while (len(poly3) - t >= 0) and (poly3[len(poly3)-t] == 0):
      del poly3[len(poly3)-t] 
    return poly3
 
#poly10 = [0, 1, 2, 3, 4, 5]
#poly9 =  [-3,0, 0,-4]
#poly8 =  [1, 1, 1, 1, 1, 1, 1]
#poly7 =  [10]
#poly6 =  [2, 0, 2, 0, 2, 0, 2, 0, 2]
#poly5 =  [0, -1, -2, -3, -4, -5]
#poly4 =  [0, 1, 2, 3, 4]
#poly3 =  [0,-1, 2,-3, 4]
#poly2 =  [20]
#poly1 =  [0, 0, 0, 0, 0, 5]
#print(polySum(poly10, poly5))
#print(polyMultiply(poly4, poly3))
#poly1 = [1, 2, 5,0,0,0,0,0]
#poly2 = [2, 0, 1, -7, 0, 0, 0,0,0,0,0]
#print(polyMultiply(poly1, poly2))