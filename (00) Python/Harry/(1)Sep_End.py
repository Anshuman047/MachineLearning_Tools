##Escape sequence, comments, separetor, end
print("Hello world!!")
print(23**2) #Would give product, if it was in double quotes then would print as it is as string

##Printing to next line = /n (Escape sequence character for new line)
print("My name is Anshuman,\n I am the trigintrillionaire!!")

##Printing double quotes as a part of line, put backslash before starting and before ending of qoutes (Escape sequence character for double quotes)
print("Hi, my name is \"Anshuman Sahoo\", and I am a trilionaire!!")

##Printing multiple things at one time,and using separetor 
print("Hey",6,3) #By default seperater b/w them is space
print("Hey", 6, 3, sep="_") #This will make sepertor as any symbol

##By default end value of any print statemnt is nextLine, but we could change it by passing the attribute value
print("end has by default \"Next Line\" as its value, ", end="2130043") #Here we changed the lineEnding by a number
print(", But we have changed it, giving a number")