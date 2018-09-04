n = [ int(x) for x in input("give a list of integers\n").split()]
m = input("give integer\n")
m = int(m)
l = len(n)
def binarysearch(n,v,p,q):
    if q <= p and v!=n[p]:
        return False
    else:
        j=int((q-p+1)/2)
        print(j)
        if n[j]==v:
            return True
        if n[j]>v:
            return binarysearch(n,v,p,j)
        else:
            return binarysearch(n,v,j,q)
    
def checkSums(n,m,l):
    nn=sorted(n)    
    for i in range(l):
        if nn[i]>=0 and binarysearch(nn,nn[i]-m,0,l):
            return True

    return False
print(checkSums(n,m,l))
#time complexity O(nlogn)
