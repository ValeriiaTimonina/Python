from re import T
 
 
class Node:
    def __init__(self, nextNode=None, prevNode=None, data=None):
        self.data = data
        self.nextNode = nextNode
        self.prevNode = prevNode
  
class LinkedList:
    def __init__(self):  
        self.head = None
  
class Car:
    def __init__(self, identification, name, brand, price, active):
        self.identification = identification
        self.name = name
        self.brand = brand
        self.price = price
        self.active = active
  
db = LinkedList()
  
def init(cars):
    root = None
    for i in range(len(cars)-1):
        for j in range(len(cars)-i-1):
            if cars[j].price > cars[j + 1].price:
                temp2 = cars[j]
                cars[j]=cars[j + 1]
                cars[j + 1]=temp2
    for i in range(0, len(cars)):
        new_node = Node(None,None,None)
        new_node.data = cars[i]
        temp = db.head    
        if (db.head == None):
            db.head = new_node
        elif (db.head != None):
            while (temp.nextNode != None):
                temp = temp.nextNode
            temp.nextNode,new_node.prevNode=new_node,temp
    return root
 
 
#arr1 = Car(0,"Z47","Lada",100,True)
#arr2 = Car(1, "X5","Audi",150, False)
#arr3 = Car(2, "J56","DEO",300, False)
#arr4 = Car(3, "Super","Toyota",150, False)
#arr5 = Car(4, "Octavia","Skoda",250, False)
 
#era = [arr1, arr2, arr3, arr4]
  
#root4 = init(era)
 
 
def sizeof(db):
  temp,count = db.head,0
  while (temp != None):
    count,temp = (count+1),temp.nextNode
  return count
 
def getDatabase():
    return db
  
def getDatabaseHead():
    return db.head
  
def clean():
    while (db.head != None):
        temp = db.head
        db.head = temp.nextNode
        temp = None
        #temp = None
  
def add(car):
  new_node = Node(None, None, None)
  new_node.data = car
  temp = db.head
 
  #pokud seznam je prazdny:
  if db.head == None:
        db.head = new_node
        return
 
  #pokud seznam neni prazdny:
  while (temp != None): #pokud seznam se neskoncil
    while ( temp != None):
        if (temp.data.price <= car.price):
            if (temp.nextNode != None):
                temp = temp.nextNode   #prochazime seznamem
            elif (temp.nextNode == None):
                temp = new_node #pokud kazdy prvek je mensi, vlozime na konec seznamu
        else:
            if (temp == db.head):
                db.head = new_node
                db.head.nextNode = temp
                temp.prevNode = db.head
            else:
                temp_2 = temp
                temp = new_node
                temp.nextNode = temp_2
                temp.prevNode = temp_2.prevNode
                temp_2.prevNode.nextNode = temp
                temp_2.prevNode = new_node
            break
    temp_3 = db.head
    while temp_3 != None:
        temp_3 = temp_3.nextNode
    return #adding is finished
  return
  
def updateName(identification, name):
    temp = db.head
    while (temp != None):
        if (temp.data.identification == identification):
            temp.data.name = name
            return
        else:
            temp = temp.nextNode  
    return
  
def updateBrand(identification, brand):
    temp = db.head
    while (temp != None):
        if (temp.data.identification == identification):
            temp.data.brand = brand
            return
        else:
            temp = temp.nextNode  
    return
  
def activateCar(identification):
    temp = db.head
    while (temp != None):
        if (temp.data.identification == identification):
            temp.data.active = True
            return
        else:
            temp = temp.nextNode  
    return
  
def deactivateCar(identification):
    temp = db.head
    while (temp != None):
        if (temp.data.identification == identification):
            temp.data.active = False
            return
        else:
            temp = temp.nextNode  
    return
  
def calculateCarPrice():
    temp = db.head
    cena = 0
    while (temp != None):
        if (temp.data.active == True):
            cena = cena + temp.data.price
            temp = temp.nextNode  
        else:
            temp = temp.nextNode  
    return cena
  
#print(db.head.data.brand, "...stary prvni prvek")
#print(db.head.nextNode.data.brand, "...stary druhy prvek")
#print(db.head.nextNode.nextNode.data.brand, "...stary treti prvek")
#print(db.head.nextNode.nextNode.nextNode.data.brand, "...stary ctvrty prvek")
# updateName(1, "Lera")
#calculateCarPrice()
#activateCar(2)
#calculateCarPrice()
#updateBrand(3, "Gavno")
#print("\n")
#add(arr5)
#print("\n nova velikost = ", sizeof(db),"\n")
#print(db.head.data.brand, "...novy prvni prvek")
#print(db.head.nextNode.data.brand, "...novy druhy prvek")
#print(db.head.nextNode.nextNode.data.brand, "...novy treti prvek")
#print(db.head.nextNode.nextNode.nextNode.data.brand, "...novy ctvrty prvek")
 
#car1 = Car(13,"GT","Alfa Romeo",250000,True)
#car2 = Car(23, "Felicia","Skoda",5000, True)
#car3 = Car(1, "Octavia","Skoda",123000, True)
#car4 = Car(11, "Superb","Skoda",54000, True)
#clean()
#add(car1)
#add(car2)
#add(car3)
#add(car4)
#print("xxxxxxxxxxxxxx")
#print(db.head.data.price, "novy prvni prvek")
#print(db.head.nextNode.data.price, "novy druhy prvek")
#print(db.head.nextNode.nextNode.data.price, "novy treti prvek")
#print(db.head.nextNode.nextNode.nextNode.data.price, "novy ctvrty prvek")