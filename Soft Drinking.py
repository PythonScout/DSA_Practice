n,k,l,c,d,p,nl,np =map(int, input().split())
sol = int (min( (k*l/nl), (c*d), (p/np)) / n)
print( sol)

k*l/nl, c*d, p/np