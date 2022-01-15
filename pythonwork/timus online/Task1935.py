# i[j] = a[i]
n = int(input())
wingsAmount = list(map(int, input().split()))
print(sum(wingsAmount)+max(wingsAmount))

#   a n b
#   left of n = max(a,n)
#   right of n = max(b,n)
#   a+b < n+max(a,b)
#   n,a,b n+max(a,b) 
#   
#   n = min
#   a > n
#   b > n
#   