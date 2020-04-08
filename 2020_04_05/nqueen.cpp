#include <iostream>
#include <vector>

#define abs(a) (((a)>0) ? (a) : -(a))

using namespace std;

int main(){
	int n=0;
	bool flag;
	cin>>n;

	vector<vector<int>> stack;
	vector<int> queen_state(n,-1);
	
	for(int i=n-1;i>=0;i--){
		stack.push_back({0,i});
	}

	int ans=0;
	while(stack.size()!=0){
		vector<int> cur = stack.back();
		stack.pop_back();
		
		if(cur[0]==n-1){
			ans++;
			continue;
		}
		queen_state[cur[0]] = cur[1];

		for(int i=n-1;i>=0;i--){
			flag = true;
			vector<int> node = {cur[0]+1,i};

			for(int j=0;j<node[0];j++){
				vector<int> prev = {j,queen_state[j]};
				if(prev[1]==node[1] || abs(prev[0]-node[0])==abs(prev[1]-node[1])){
					flag = false;
					break;
				}
			}

			if(flag)
				stack.push_back(node);
		}
	}

	cout<<ans;
	return 0;
}