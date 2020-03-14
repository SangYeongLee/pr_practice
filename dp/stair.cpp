#include <iostream>
#include <algorithm>

using namespace std;

int main(){
	int dp[301][2]={{0,0},};
	int score[301];
	int n;
	cin>>n;

	for(int i=1;i<=n;i++){
		cin>>score[i];
	}
	if(n==1){
		cout<<score[n];
		return 0;
	}
	dp[n-1][0]=score[n]+score[n-1];
	dp[n-2][1]=score[n]+score[n-2];

	for(int i=n-3;i>0;i--){
		dp[i][0] = score[i]+dp[i+1][1];
		dp[i][1] = score[i]+max(dp[i+2][0],dp[i+2][1]);
	}

	cout<<max(max(dp[1][0],dp[1][1]),max(dp[2][0],dp[2][1]));

	return 0;
}