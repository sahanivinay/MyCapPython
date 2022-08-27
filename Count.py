from collections import Counter
test_str =str(input("Please enter a string: "))
res = Counter(test_str) 
print ("Count of all characters in MISSISSIPPI:\n " +  str(res))