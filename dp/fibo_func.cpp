#include <iostream>

using namespace std;

int main(){
	int dp0[41]={1,0,1,1};
	int dp1[41]={0,1,1,2};
	int n;

	for(int i=4;i<41;i++){
		dp0[i] = dp0[i-1]+dp0[i-2];
		dp1[i] = dp1[i-1]+dp1[i-2];
	}
	cin>>n;

	for(int i=0;i<n;i++){
		int temp;
		cin>>temp;
		cout<<dp0[temp]<<" "<<dp1[temp]<<endl;
	}


	return 0;
}