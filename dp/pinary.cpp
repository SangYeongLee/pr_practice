//https://www.acmicpc.net/problem/2193
#include <iostream>

using namespace std;

int main()
{
	long long dp[91][2]={{0,0},{0,1}};
	int n;
	cin>>n;

	for(int i=2;i<=n;i++){
		dp[i][0] = dp[i-1][0]+dp[i-1][1];
		dp[i][1] = dp[i-1][0];
	}

	cout<<dp[n][0]+dp[n][1];

	return 0;
}