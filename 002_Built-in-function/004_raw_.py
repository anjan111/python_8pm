# raw_input ===> float()
print "******** raw_input **********"
var = raw_input("enter float : ")
print "daata in var : ",var
print(type(var))
print "memory loc : ",id(var)
print "******** float  **********"
var = float(var)
print "daata in var : ",var
print(type(var))
print "memory loc : ",id(var)
