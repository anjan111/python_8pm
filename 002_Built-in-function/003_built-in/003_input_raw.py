# raw_input  vs input
a = raw_input("enter int by raw : ")
print "data in a " ,a
print(type(a))
print "memory : ",id(a)

a = input("enter int by input : ")
print "data in a " ,a
print(type(a))
print "memory : ",id(a)
