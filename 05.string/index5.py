name = "Astha"
city = 'Kalol'
language = "Python" 
message = 'Learning Python is fun'
print(name, city, language, message)

a = "programming"
print(a[0])
print(a[1])
print(a[3])
print(a[-1])

a = "Python Programming"
print(a[0:6])
print(a[7:])
print(a[:])
print(a[:5])
print(a[-5:])

a = "Python Programming"
last_index = len(a) - 1 
print(a[last_index])

first_name = "Astha"
last_name = "Bhosale" 
full = first_name + " " + last_name
print(full_name)

a = "python programming language"
print(a.upper()) 
print(a.lower())
print(a.capitalize())
print(a.title()) 
print(a.swapcase()) 

txt = "Python is a programming language"
print("Python" in txt)
print(txt.find("Java"))

txt = "I am learning Java"
new_txt = txt.replace("Java", "Python") 
print(new_txt)

a = " Python Programming "
print(a.strip()) 
print(a.lstrip())
print(a.rstrip())

b = "python is easy to learn"
print(b.split())
words = ["python","is","easy"]
print(" ".join(words))

name = "Astha" 
age = 20
city = "Kalol"
print(f"my name is {name},i am {age} years old, and i live in {city}")

#read again**
name = input("enter full name: ")
clean = name.strip()
print(name)
print(clean)
print(clean.upper())
print(clean.lower())
print(clean.title())
print(len(clean))
print(clean[0])
print(clean[-1])
print("a" in clean)

a = input("enter a sentence:")
print(a)
print(len(a))
print(len(a.split()))
print(a[0])
print(a[-1])
print(a.upper())
print(a.lower())
print(a.title())
print("python" in a)
print(a.count("a"))

#read again**
first = input("First name: ").strip() 
last = input("Last name: ").strip()
city = input("City: ").strip()
course = input("Course: ").strip()
age = int(input("Age: "))
full = first + " " + last
print(full.title())
print(full.upper())
print(full.lower())
print(len(full)) 
print(full[0])
print(full[-1]) 
print(city, course)
print(f"Age is {age}")
print("Python" in course)
print(course.replace("Java", "Python", 1))
print(len(course.split()))