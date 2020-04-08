//https://www.acmicpc.net/problem/10844
#include <iostream>

using namespace std;

int main()
{
	int n;
	cin>>n;

	int dp[101][10];
	dp[1][0] = 0;
	for(int i=1;i<10;i++)
		dp[1][i] = 1;

	for(int i=2;i<=n;i++){
		dp[i][0] = dp[i-1][1];
		for(int j=1;j<9;j++){
			dp[i][j] = (dp[i-1][j-1]+dp[i-1][j+1])%1000000000;
		}
		dp[i][9] = dp[i-1][8];
	}

	int ans=0;
	for(int i=0;i<10;i++){
		ans=(ans+dp[n][i])%1000000000;
	}
	cout<<ans;
	return 0;
}
