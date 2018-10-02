#which of the following statement generates error
x = [1,"abcd",2,"efgh",[3,4]]  # Statement 1
y = x[0:50]                    # Statement 2
z = y                          # Statement 3
w = x                          # Statement 4
x[1] = x[1] + 'd'              # Statement 5
#x[1][1] = 'y'                  # Statement 6
y[2] = 4                       # Statement 7
z[0] = 0                       # Statement 8
w[4][0] = 1000                 # Statement 9
a = (x[4][1] == 4)             # Statement 10
#ans line no 6

x = [13,4,17,1000]
w = x[1:]
u = x[1:]
y = x
u[0] = 50
y[1] = 40
print(x[1],y[1],w[0],u[0])

#what is the value of endmsg
startmsg = "hello"
endmsg = ""
for i in range(0,len(startmsg)):
    endmsg = startmsg[i] + endmsg
print(endmsg)

#What is the value of mylist after the following lines are executed?
def mystery(l):
    l = l+l
    return()
mylist = [31,24,75]
mystery(mylist)
print(mylist)
