n=int(input())

arr=[list(map(int,input().split()))for _ in range(n)]
dp=[[0]*n for _ in range(n)]

dp[0][0]=arr[0][0]

for i in range(n):
    for j in range(n):
        if i==0 and j==0:continue
        if i-1>=0:dp[i][j]=max(dp[i-1][j],dp[i][j])
        if j-1>=0:dp[i][j]=max(dp[i][j-1],dp[i][j])
        dp[i][j]+=arr[i][j]

print(dp[n-1][n-1])