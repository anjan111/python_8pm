# raw_input  vs input
'''
===>> rawinput is resultant datatype is str for any data

===>> input is resultant datatype is based data
'''

a = raw_input("enter float by raw : ")
print "data in a " ,a
print(type(a))
print "memory : ",id(a)
a = bool(a)
print "data in a " ,a
print(type(a))
print "memory : ",id(a)

a = input("enter float by input : ")
print "data in a " ,a
print(type(a))
print "memory : ",id(a)

# datatype conversion functions
