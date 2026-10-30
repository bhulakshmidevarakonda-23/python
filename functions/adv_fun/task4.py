s="hlo python life"


from functools import reduce
count = reduce(lambda x, y: x+(y in "aeiouAEIOU"), s,0)
print(count)