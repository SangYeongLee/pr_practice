//https://www.acmicpc.net/problem/14889
#include <iostream>
#include <vector>
#include <algorithm>
#include <limits.h>

#define abs(n) (n>0 ? n : -n)

using namespace std;

int main(){
	int n,ans=INT_MAX;
	vector<vector<int>> score;
	
	cin>>n;
	for(int i=0;i<n;i++){
		vector<int> temp;
		for(int j=0;j<n;j++){
			int val;
			cin>>val;
			temp.push_back(val);
		}
		score.push_back(temp);
	}

	vector<int> idx;
	for(int i=0;i<n/2;i++){
		idx.push_back(1);
		idx.push_back(0);
	}

	sort(idx.begin(),idx.end());
	vector<vector<int>> team1,team2;

	do{
		vector<int> t1,t2;
		for(int i=0;i<idx.size();i++){
			if(idx[i]==0)
				t1.push_back(i);
			else
				t2.push_back(i);
		}
		team1.push_back(t1);
		team2.push_back(t2);
	}while( next_permutation(idx.begin(),idx.end()) );
	
	for(int cur=0;cur<team1.size()/2;cur++){
		int diff=0;
		for(int i=0;i<team1[cur].size()-1;i++){
			for(int j=i+1;j<team1[cur].size();j++){
				diff+=score[team1[cur][i]][team1[cur][j]]+score[team1[cur][j]][team1[cur][i]];
				diff-=score[team2[cur][i]][team2[cur][j]]+score[team2[cur][j]][team2[cur][i]];
			}
		}
		if(abs(diff)<ans) ans = abs(diff);
	}
	cout<<ans;

	return 0;
}