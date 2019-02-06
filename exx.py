def largest(ar,n):
     max = ar[0]
     for i in range(1, n):
        if(ar[i] > max):
            max = ar[i]
            return max
ar = [12, 23, 34, 45, 56, 78 ];
n = len(ar)
Ans = largest(ar,n)
print ("Largest num is",Ans)
