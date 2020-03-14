#include <iostream>

using namespace std;

int dp[1000000];

int make1(int num){
	if(num==1) return 0;
	if(dp[num]!=0) return dp[num];

	int temp;
	int ret=1000000;

	if(num%3==0){
		temp = 1+make1(num/3);
		if(temp < ret) ret = temp;
	}

	if(num%2==0){
		temp = 1+make1(num/2);
		if(temp < ret) ret = temp;
	}
	
	temp = 1+make1(num-1);
	if(temp < ret) ret = temp;
	
	dp[num] = ret;
	return ret;
}

int main(){
	int in;
	cin>>in;
	cout<<make1(in);
	return 0;
}