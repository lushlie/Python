#loop - repeat a process
#while loop
number = 20 # 1 no. to be displayed

while number <= 25: #last no. (condition)
    print(number)
    number += 1 # increase or decrease to the while (condition)
print()
#break
number = 20

while number <= 25:
    print(number)
    if number == 23 :
        break
    number += 1
print()
#continue
number = 20

while number <= 25:
    number += 1
    if number == 23 :
        continue
    print(number)
print()

#for loop
for x in range(30, 36): # 36 to get 35 a no. ahead (3 no. to pick how to increase e.g (1, 21, 2 ))
    print(x)
print()

#break
for x in range(30, 36):
    print(x)
    if x == 33 :
        break
print()
#continue
for x in range(30, 36):
   if x == 33 :
    continue
   print(x)

#break - stops the entire loop
#continue - skips 1 round and carries on 
