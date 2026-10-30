#strings are used to store the text data in python
#used to print sequence of characters in python
#uphrast(') value use and text in in single quote then it becom error(ex:'8'o clock')
#space is also a character in python
#string is immutable datatype
#reallife example:gmail,it avoid case sensetive ,
#how you typed even upper or lower no matter that convert in lower in mail point of you only 
#in othercases it is case sensetive like password,username etc
n=" python life"

#print(len(n))#len() is used to find the length of the string
#print(n[-4:])#life
#print(n[-11:-5])#python
#print(n.upper())#PYTHON LIFE
#print(n.lower())#python life
#strip() is used to remove the white space from the string
#rstrip() is used to remove the white space from the right side of the string
#lstrip() is used to remove the white space from the left side of the string
#n=" python life "
#print(n.strip())#python life
#print(n.rstrip())# python life
#print(n.lstrip())#python life


#print(n.split(" "))#['i', 'am', 'very', 'good', 'girl']
n="i am very good girl"
n2="1234"
n3=" 123"
print(n.find("v"))#5
print(n.find("g"))#10
r=n2.isdigit()
print(r)#True,because all are digits
r2=n3.isdigit()
print(r2)#false,because of space is string
n4="python.life" 
print()
