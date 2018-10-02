def intreverse(n):
    n1=n
    s=0
    while n1>0:
        r=n1%10
        s=s*10+r
        n1=n1/10
    return(s)
