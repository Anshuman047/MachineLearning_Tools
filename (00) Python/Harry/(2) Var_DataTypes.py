##Variables
a = 1 #int type
print(a,type(a))

b = "Anshuman" #string type
print(b, type(b))

c = True #Boolean
print(c, type(c))

d = None #Null
print(d, type(d))

e = complex(8,9) #Complex type, by using complexFunction
print(e, type(e))

f = 11.1
print(f, type(f)) #Float type

##Concatening 2-same-type of variables
c = " is Handsome!!"
print(b+c)

## List is the collection of different items but is mutable
list1 = [8, 2.3, 4,[-4,90], ["apple", 78], "Banana"]
print(list1, type (list1))

## Tupple is the collection of different items but is immutable
tupple1 = (8, 2.3, 4,[-4,90], ["apple", 78], "Banana")
print(list1, type (tupple1))

## Dictionary used for mapping values with key
dict1 = {
    "name":"Anshuman",
    "age":20,
    "canVote":True
}
print(dict1, type(dict1))

### Note: Bydefault in Python everything is object including all variables

