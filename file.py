#Code1
age = int(input("enter age : "))

if(age >= 18):
 if(age >= 80):
    print("cannot drive")
 else:
    print("can drive")

else:
 print("cannot drive")

#Code2
def check():
    if(n <= 1):
      return False

    for i in range(2, n):
        if(n % i == 0):
            return False 
        return True 

check(7)

#Code3
for i in count(1):
  if(i > 10):
    break
  if(i == 5):
    i += 1
    continue 
  print(i)
 


