//https://www.acmicpc.net/problem/1149
#include <iostream>
#include <algorithm>

using namespace std;

int main(){
	int num;
	int dp[1000][3];
	int arr[1000][3];
	cin>>num;

	for(int i=0;i<num;i++){
		cin>>arr[i][0]>>arr[i][1]>>arr[i][2];
	}

	copy(arr[0],arr[0]+3,dp[0]);
	for(int i=1;i<num;i++){
		for(int j=0;j<3;j++){
			dp[i][j] = min(dp[i-1][(j+1)%3]+arr[i][j],dp[i-1][(j+2)%3]+arr[i][j]);
		}
	}

	cout<<min(dp[num-1][0],min(dp[num-1][1],dp[num-1][2]));

	return 0;
}