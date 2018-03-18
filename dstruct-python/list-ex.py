#Example for list in python
friends = ['Damo', 'Preethi', 'Ranjith', 'Kaustubh', 'Vidhu']
print(friends)

new_friends = ['Gautham', 'Sheetal']

friends.append(new_friends)
print(friends)

friends.append('Laxmi')
print(friends)

family = ['Padmini', 'Ajay', 'Baburaya']
friends.extend(family)
print(friends)

print('The length of friends list is ' + repr(len(friends)))
print(len(friends))

sorted_friends = sorted(friends)
print(sorted_friends)

sorted_friends.reverse()
print(sorted_friends)