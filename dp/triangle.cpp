#include <iostream>
#include <vector>

#define max(a,b) (a>b ? a : b)

using namespace std;

int main(){
	vector<vector<int>> dp;
	int n,val;
	cin>>n;
	cin>>val;

	dp.push_back({val});
	vector<int> temp;
	for(int i=1;i<n;i++){
		temp = {};
		for(int j=0;j<=i;j++){
			cin>>val;
			if(j==0)
				temp.push_back(val+dp[i-1][0]);
			else if(j==i)
				temp.push_back(val+dp[i-1][i-1]);
			else{
				temp.push_back(max(val+dp[i-1][j-1],val+dp[i-1][j]));
			}
		}
		dp.push_back(temp);
	}

	int answer=dp[n-1][0];
	for(int i=1;i<n;i++){
		answer = max(dp[n-1][i],answer);
	}

	cout<<answer;
	return 0;
}