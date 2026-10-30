#n=[10,20,30,40,50,60]
#print(n[2])
#print(n[0:3])
#print(n[0:5:2])
#print(n[-5:-2])
#print(n[6:3:-1])
#print(n[-2:-6:-1])
#n=[10,20,30,40,50,60]


#m=n.copy()
#n.append(70)
#print(n)//[10,20,30,40,50,60,70]
#print(m)//[10,20,30,40,50,60]
#n=[10,20,30,40,50,60]
#m=n.copy()
#n.append(70)
#print(n)#[10,20,30,40,50,60,70]
#n.remove(30)
#print(n)#[10,20,40,50,60,70]
#n.pop(2)
#print(n)#[10,20,50,60,70]
#n.insert(2,30)
#print(n)#[10,20,30,50,60,70]
#n.insert(3,80)
#print(n)#[10,20,30,80,50,60,70]
#n.sort()
#print(n)#[10,20,30,50,60,70,80]
#n.sort(reverse=True)
#print(n)#[80,70,60,50,30,20,10]
#list=[]
#for i in range(1,11):
  #  if i%2==0:
        #list.append(i)
#print(list)#[2,4,6,8,10]
#print([i for i in range(11) if i%2==0])#[0,2,4,6,8,10]#just used to display output
#print([i**2 for i in range(11)])#[0,1,4,9,16,25,36,49,64,81,100]

n1 = [1, 2, 3, 4, 5]
n2 = [4, 5, 6, 7, 8]

list1 = []

for i in n1:
    for j in n2:
        if i == j:
            list1.append(i)

print(list1)
