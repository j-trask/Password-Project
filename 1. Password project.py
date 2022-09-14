filename = "password.txt"
delimeter = '='

file = open(filename, 'r')

def findValue(fullString):

    #strips, and creates newlines
    fullString = fullString.rstrip('\n')

    #goes to the delimeter being '=' and
    #starts at the index ahead of delimeter    
    value = fullString[fullString.index(delimeter) + 1:]
    value = value.replace(" ", "") #gets rid of spaces
    return value 

for line in file:

    #when a line is found with these beginning it will pull the
    #entire line and make it equal variables password and username respectively
    if line.startswith('username'):
        username = findValue(line)
    if line.startswith('password'):
        password = findValue(line)
        
print (password)


def main():
    setPass = input("input your password: ")
    if setPass == password:
        print ("logged in!")
        conditionOne = 1
        
    while setPass != password:
        print ("Incorrect Password input correct Password!")
        setPass = input("Input your password: ")
        if setPass == password:
            print ("logged in!")
            
main()
