//https://www.acmicpc.net/problem/9663
#include <iostream>

#define abs(a) (((a)>0) ? (a) : -(a))
#define MAX 15

using namespace std;

int map[MAX];
int n,ans;

bool chk(int cur){
	for(int i=0;i<cur;i++){
		if(map[i]==map[cur] || abs(map[cur]-map[i])==cur-i)
			return false;
	}
	return true;
}

void dfs(int cur){
	if(cur==n){
		ans++;
		return;
	}

	for(int i=0;i<n;i++){
		map[cur] = i;
		if(chk(cur)) dfs(cur+1);
	}
}

int main(){
	cin>>n;
	dfs(0);

	cout<<ans;
	return 0;
}