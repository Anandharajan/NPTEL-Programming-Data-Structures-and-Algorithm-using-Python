#First Method
def gcd1(m,n):
    fm=[]
    for i in range(1,m+1):
        if (m%i==0):
            fm.append(i)
    fn=[]
    for j in range(1,n+1):
        if (n%j==0):
            fn.append(j)
    cf=[]
    for f in fm:
        if f in fn:
            cf.append(f)
    return(cf[-1])
#Second Method
def gcd2(m,n):
    cf=[]
    for i in range(1,min(m,n)+1):
        if (m%i)==0 and (n%i)==0:
            cf.append(i)
    return(cf[-1])
#Third Method
def gcd3(m,n):
    for i in range(1,min(m,n)+1):
        if (m%i)==0 and (n%i)==0:
            mrcf=i
    return(mrcf)
#Fourth Method
def gcd4(m,n):
    i = min(m,n)
    while i>0:
        if (m%i) == 0 and (n%i) == 0:
            return(i)
        else:
            i = i-1
#Euclid's Method
def gcd5(m,n):
    if m<n:
        (m,n)=(n,m)
    if m%n==0:
        return(n)
    else:
        diff=m-n
        return(gcd5(n,m%n))
m=int(input("Enter first number\n"))
n=int(input("Enter second number\n"))
ans=gcd5(m,n)
print("GCD of ",m," and ",n," =",ans)
