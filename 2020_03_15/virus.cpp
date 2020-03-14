//https://www.acmicpc.net/problem/14502
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
	int N,M;
	int answer=0;
	vector<vector<int>> board;
	vector<vector<int>> blank;
	vector<vector<int>> virus;
	cin>>N>>M;

	for(int i=0;i<N+2;i++){
		vector<int> temp;
		for(int j=0;j<M+2;j++){
			if(i==0 || i==N+1 || j==0 || j==M+1){
				temp.push_back(1);
			}else{
				int num;
				cin>>num;
				temp.push_back(num);
				if(num==0) blank.push_back({i,j});
				else if(num==2) virus.push_back({i,j}); 
			}
		}
		board.push_back(temp);
	}

	vector<int> ind={1,1,1};
	for(int i=0;i<blank.size()-3;i++){
		ind.push_back(0);
	}

	sort(ind.begin(),ind.end());
	vector<vector<int>> move={{1,0},{-1,0},{0,1},{0,-1}};

	do{
		int cnt=0;
		vector<vector<int>> temp = board;
		for(int i=0;i<ind.size();i++){
			if(ind[i]==1)
				temp[blank[i][0]][blank[i][1]]=3;
		}

		for(int i=0;i<virus.size();i++){
			vector<vector<int>> stack;
			stack.push_back(virus[i]);

			while(stack.size()!=0){
				vector<int> cur = stack.back();
				stack.pop_back();
				
				for(int j=0;j<move.size();j++){
					if(temp[cur[0]+move[j][0]][cur[1]+move[j][1]]==0){
						stack.push_back({cur[0]+move[j][0],cur[1]+move[j][1]});
						temp[cur[0]+move[j][0]][cur[1]+move[j][1]]=2;
						cnt++;
					}
				}

			}
		}

		if(blank.size()-3-cnt > answer) 
			answer = blank.size()-3-cnt;
	}while(next_permutation(ind.begin(),ind.end()));
	cout<<answer;
	return 0;
}