t = int(input());

def DP (N) : 
    d_zero = [1,0];
    d_one = [0,1];
    for i in range(2,N+1):
        d_one.append(d_one[i-1]+d_one[i-2]); 
        d_zero.append(d_zero[i-1] + d_zero[i-2]);
    return [d_zero[N],d_one[N]];

for i in range(t):
    number = int(input())
    [a,b] = DP(number);
    print("%d %d"%(a,b));
    