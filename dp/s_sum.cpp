//https://www.acmicpc.net/problem/1912
#include <iostream>

using namespace std;

int main()
{
	int n,ans;
	cin>>n;
	int* num = new int[n];
	int* dp = new int[n];

	for(int i=0;i<n;i++){
		cin>>num[i];
	}
	dp[0] = num[0];
	ans = dp[0];

	for(int i=1;i<n;i++){
		if(dp[i-1]>0)
			dp[i] = dp[i-1]+num[i];
		else
			dp[i] = num[i];

		if(dp[i]>ans) ans = dp[i];
	}

	cout<<ans;

	return 0;
}