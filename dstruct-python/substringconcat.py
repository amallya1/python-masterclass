s = 'foobarthebarfoomanfoobarfoo'
words = ["foo", "bar"]
reversedWords = reversed(words)


listindex=[]
listindex2=[]
i = 0
j = 0
offset = 0

s1 = "".join(words)
s2 = "".join(reversedWords)

print (s2)

i = s.find(s1, offset)
while (i>=0):
    listindex.append(i)
    i = s.find(s1, i+1)
   
j = s.find(s2,offset)
while (j>0):
    listindex2.append(j)
    j=s.find(s2,j+1)
    
print (listindex)
print (listindex2)