List1 = [25,-67,45,-9,-1,25,37]
List2 = [19,-81,90,65,-89,-15]
print("Numbers in List1 are  : ",List1)
P1 = list(filter(lambda x: x>0, List1))
print("Positive Numbers in List1 are  : ",P1)
print("Numbers in List2 are  : ",List2)
P2 = list(filter(lambda x: x>0, List2))
print("Positive Numbers in List1 are  : ",P2)