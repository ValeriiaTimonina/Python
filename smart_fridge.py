"""
Homer's fridge
Course: B0B36ZAL
"""
 
#nasledujici kod nijak nemodifikujte!
class Food:
    def __init__(self, name, expiration):
        self.name = name
        self.expiration = expiration
#predesly kod nijak nemodifikujte!
 
def openFridge(fridge):
    print("Following items are in Homer's fridge:")
    for food in fridge:
        print("{0} (expires in: {1} days)".format(
            str(food.name), str(food.expiration))
        )
    print("")
 
# test vypisu - pri odevzdani smazte, nebo zakomentujte
#fridge = [Food("beer", 4), Food("steak", 1), Food("hamburger", 1), Food("donut", 3)]
#fridge1 = []
#openFridge(fridge)
 
 
"""
Task #1
"""
def maxExpirationDay(fridge):
    my_array = []
    for food in fridge:
        my_array.append(food.expiration)
    if (len(my_array) == 0):
        return (-1)
    return (max(my_array))
 
#print(maxExpirationDay(fridge))
 
"""
Task #2
"""
def histogramOfExpirations(fridge):
    my_array = [0]*(maxExpirationDay(fridge) + 1)
    for k in range (0, maxExpirationDay(fridge) + 1):
        for food in fridge:
            if food.expiration == k:
                my_array[k] = my_array[k] + 1
    return (my_array)
 
#print(histogramOfExpirations(fridge))
 
"""
Task #3
"""
def cumulativeSum(histogram):
    histogram1 = []
    for i in range(0, len(histogram)):
        histogram1.append(histogram[i])
    for i in range (1, len(histogram)):
        histogram1[i] = histogram1[i-1] + histogram1[i] 
        continue
    return (histogram1)
 
#print(cumulativeSum([0, 2, 0, 1, 1]))
 
"""
Task #4
"""
def sortFoodInFridge(fridge):
    nove_pole = [0]*len(fridge)
    histogram1 = cumulativeSum(histogramOfExpirations(fridge))
 #   print(histogram1)
    for food in fridge:
        posInd = histogram1[food.expiration] - 1
   #     print(histogram1[food.expiration], food.name, food.expiration, posInd, nove_pole[posInd])
        if nove_pole[posInd] == 0:
            nove_pole[posInd] = (Food(food.name, food.expiration))
        else:
            for i in range(0, histogram1[food.expiration]):
                if (nove_pole[posInd-i] == 0):
                    nove_pole[posInd-i] = (Food(food.name, food.expiration))
                    break
  #  print(nove_pole)
    return nove_pole
#fridge = [Food("beer", 4), Food("beer", 4), Food("beer", 4), Food("beer", 4), Food("beer", 4)]
#openFridge(sortFoodInFridge(fridge))
# The command should print
# Following items are in Homer's fridge:
# hamburger (expires in: 1 days)
# steak (expires in: 1 days)
# donut (expires in: 3 days)
# beer (expires in: 4 days)
 
"""
Task #5
"""
def reverseFridge(fridge):
    new_fridge = fridge[::-1]
    return new_fridge
 
#print(reverseFridge(fridge))
 
# test vypisu - pri odevzdani smazte, nebo zakomentujte
#openFridge(reverseFridge(fridge))
# The command should print
# Following items are in Homer's fridge:
# donut (expires in: 3 days)
# hamburger (expires in: 1 days)
# steak (expires in: 1 days)
# beer (expires in: 4 days)
 
# test vypisu - pri odevzdani smazte, nebo zakomentujte
#openFridge(sortFoodInFridge(reverseFridge(fridge)))
# The command should print
# Following items are in Homer's fridge:
# steak (expires in: 1 days)
# hamburger (expires in: 1 days)
# donut (expires in: 3 days)
# beer (expires in: 4 days)
 
 
"""
Task #6
"""
def eatFood(name, fridge):
    new_fridge = []
    for food in fridge:
        new_fridge.append(food)
    my_array = []
    for food in new_fridge:
        if food.name == name:
            my_array.append(food.expiration)
    if len(my_array) != 0:
        my_min = min(my_array)
    else:
        return new_fridge
    counter = 0
    for i in range(len(new_fridge) - counter):
        if (new_fridge[i - counter].name == name) and (new_fridge[i - counter].expiration == my_min):
            new_fridge.remove(new_fridge[i - counter])
            counter += 1
    return new_fridge
 
 
# test vypisu - pri odevzdani smazte, nebo zakomentujte
#a = [Food("donut", 2)]
#print(id(a))
#print(a)
#a = eatFood("maso", a)
#print(a)
#print(id(a))
#openFridge(
#     eatFood("donut",
#         [Food("beer", 4), Food("steak", 1), Food("hamburger", 1),
#         Food("donut", 1), Food("donut", 1), Food("donut", 1)]))
# The command should print
# Following items are in Homer's fridge:
# beer (expires in: 4 days)
# steak (expires in: 1 days)
# hamburger (expires in: 1 days)
# donut (expires in: 3 days)
# donut (expires in: 6 days)
 
 
#if __name__ == "__main__":
#    print("ahoj")
#    fridge = [Food("beer", 4), Food("steak", 1), Food("hamburger", 1), Food("donut", 3)]
#    openFridge(fridge)