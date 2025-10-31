"""
thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))

thislist = ["apple", "banana", "cherry","orange","kiwi","melon","mango"]

thislist[1] = "blackcurrant"
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])
        """
"""
thislist = ["apple", "banana", "cherry"]
#thislist.insert(2, "watermelon")
thislist.append("orange")
print(thislist)
    """
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)