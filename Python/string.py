string1 = "Python"
string2 = "Data Science"
concatenated_string = string2 + " " + string1
print(concatenated_string)


original_string = "Python"
replicated_string = original_string * 3
print(replicated_string)


String = "Python is powerful!"
length = len(String)
print(length)

# Creating a String 
String1 = "GeeksForGeeks"

# Printing 3rd to 12th character 
print("Slicing characters from 5-12: ") 
print(String1[5:12]) 

# Printing between 3rd and 2nd last character 
print("Slicing characters between " +
	"3rd and 3rd last character: ") 
print(String1[3:-3]) 


string = "Hello, Python!"
uppercase_string = string.upper()
lowercase_string = string.lower()
print(uppercase_string)  
print(lowercase_string)

strng = "I am beginner in Python"
new_string = strng.replace("beginner", "experienced")
print(new_string)

string = "python program run on python IDLE, in pythonic way."
count = string.count("python")
print(count)

string = "Python is powerful and Pythonic."
index = string.find("Python")
print(index) 
index = string.find("Pythonic")
print(index)