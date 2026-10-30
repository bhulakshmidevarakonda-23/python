d={}
while True:
   print("1:add a word")
   print("2:serch for word")
   print("3:display all words")
   print("4:remove word")
   print("5:update word")
   print("6:exit")
   choice=input("enter your choice:")
   if choice=="1":
     word=input("enter word:")
     d[word] = True
     print(d)
   elif choice=="2":
       search_word=input("enter search word:")
       if search_word in d:
          print("word found")
       else:
           print("not found")
   elif choice=="3":
       print("display all words: ",d)
   elif choice=="4":
       r=input(" enter remove word:")
       if r in d:
            d.remove(r)
       else:
           print("r is not in d")
       print(d)
   elif choice=="5":
      u=input("enter update word:")
      d.update(u)
      print(d)
   elif choice=="6":
      print("exit")
      break 
   else:
      print("invalid")

