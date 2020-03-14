#include <iostream>

using namespace std;

int main(){
	int dp[11]={0,1,2,4};
	int num;
	cin>>num;

	for(int i=4;i<=10;i++){
		dp[i] = dp[i-1]+dp[i-2]+dp[i-3];
	}

	for(int i=0;i<num;i++){
		int temp;
		cin>>temp;
		cout<<dp[temp]<<endl;
	}

	return 0;
}