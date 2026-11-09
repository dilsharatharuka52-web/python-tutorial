#List is use store multiple value

friends = ["Pakaya", "Kariya", "Hukana"]
print(friends[0]) # acess element use index
print(friends[0:2]) # print specify range
friends[0] = "Doiya"
print(friends[0])

# List function
lucky_number = [4, 5, 6, 7, 8, 9]
lucky_name = ["a", "b", "c", "d"]

lucky_number.extend(lucky_name) # use combine tow arrays
print(lucky_number)
lucky_number.append("y") # add new value to end
lucky_number.insert(1,"p") # add new value in special index
lucky_number.pop() # remove last elemant
print(lucky_number)
fren2 = friends.copy() # copny old list value in new list
print(fren2)
print(lucky_number.index(4)) # print index of value in list
lucky_number.clear() # clear all value and emty list

print(lucky_number)


