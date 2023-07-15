random_string = "This  is a Dipak"
print(random_string.find("is"))
print(random_string.replace("Dipak","David"))
print(random_string.upper())
print(random_string.lower())

string1 = "{author} is teaching python to you".format(author="David")
print(string1)

l = ['a','b','c']
print(' '.join(l))

var = lambda a,b,c : a[0]+b[0]+c[0]
print(var("World ","Wide ","Web"))
