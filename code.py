import random
print("-----pattern recoginition game-----")
score=0
for i in range(3):
    num = randon.randint(0,1)
    diff = random.randint(2,5)
    p1 = num
    p2 = num + diff
    p3 = num + diff*2
    p4 = num + diff*3
    ans = num + diff*4
    print (f"\nQ{i+1} , what is next? {p1}, {p2}, {p3}, P4} ,?")
    user =int(input("your answer"))
    if user == ans:
          print("correct")
          score += 1
     else:
           print(f"wrong! correct answer is (ans)")
     print(f"\n Game over!score = {score}/3")
