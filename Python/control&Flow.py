x=1
if x >= 18 :
    print("You can vote")
else:
    print("You are not eligible")

    x=43
    print(x) if x < 10 else print(False)

    x =56

if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")


    # loops

    # for loop
    
for i in range(12,121,12):
    print(i)



for i in range(12):
    for i in range(12):
        print(i)
    

# with list
l = ["Data", "Science", "Python"]
for i in l:
	print(i)


# wiht dict
print("Dictionary Iteration")
d = dict()

d['key1'] = "val1"
d['key2'] = 345
for i in d:
	print(i, d[i])
     

# with strings
word = "Python"

for letter in word:
    print(letter)



# list comprehension 
squares = [x**2 for x in range(5)]
print(squares)



# while loops
n=1
while n<6:
    print(n)
    n+=1


counter = 1
while counter <= 5:
    if counter == 3:
        counter += 1
        continue
    print(counter, end=' ')
    counter += 1
    # break and continue statements
    # print("\nFor loop vs While Loop")
    # for each loop
    # fruits = ['apple', 'banana', 'cherry', 'date']
    # for fruit in fruits:
    #      print(fruit)
    #      # while loop
    #      while True:
    #           user_input = input("Do you want to see another fruit? (yes/no): ")
    #           if user_input.lower() != 'yes':
    #                break
              
# game loop
game_over = False
while not game_over:
    # Game logic here
    user_input = input("Continue playing? (yes/no): ")
    if user_input.lower() == "no":
        game_over = True


