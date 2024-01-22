# capitalize()
# title()
# upper()
# lower()
# split()
# join()

data = "hello world"
result = data.capitalize()
print(result)  # "Hello world"


result = data.title()
print(result)  # "Hello World"

result = data.upper()
print(result)  # HELLO WORLD

result = data.lower()
print(result)  # hello world


data = "hello world"
result = data.split()
print(result)  # ["hello", "world"]

data = "hello+world"
result = data.split("+")
print(result)  # ["hello", "world"]

result = data.split("o")
print(result)  # ["hell", "+w", "rld"]

result = data.split("l")
print(result)  # ["he", "", "o+wor", "d"]


# join()
data = ["hello", "world"]
result = " ".join(data)  # data.join(" ")
print(result)  # hello world

result = "+".join(data)
print(result)  # hello+world




1.gitis a version of control system
2.it mainatains the code history so that we can to any version of the code at required moment.
3.git has major two significances 
=> to maintain code versions 
=>to collaborate in the team work 


repository => it is nothing but a git project folder 

=. 2 respotories 
=> one is local repo and another is remote repo

#git commands 
set username and email
1. git config --global user.name ,<username>
2.git config --global user.email