def descending(l):
    j=0
    for m in range(0,len(l)-1):
        if (l[m]>l[m+1]) or (l[m]==l[m+1]):
            continue
        else:
            return (False)
    return (True)
print(descending([]))
print(descending([4,4,3]))
print(descending([19,17,18,7]))

def valley(l):
    a=len(l)
    if(a>=2):
        for i in range(0,int(a-1)):
            if (l[i] > l[i+1]):
                continue
            else:
                break
        for k in range(i,a-1):
            if(l[k]<l[k+1]):
                continue
            else:
                return(False)
        return(True)
    return(False)
print(valley([2]))
print(valley([13,12,14,14]))
print(valley([5,4,3,2,1,2]))
print(valley([17,1,2,3,4,5]))

def transpose(m):
    if not m:
        return[]
    return[[row[i] for row in m] for i in range(len(m[0]))]
print(transpose([[19,14]]))
print(transpose([[21,33,11],[42,64,16]]))
print(transpose([[16,31,42],[26,82,73],[84,53,38]]))
    
