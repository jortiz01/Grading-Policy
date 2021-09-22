#Python List
#List is dynamic array, means it can grow



from gradecalculator import calculate_mid


thislist = ["apple", "banana", "cherry"]
thislist.append("watermelon")
print(type(thislist))
print(thislist)


for currentRow in thislist:
    if currentRow == "cherry":
        print(currentRow)
        break