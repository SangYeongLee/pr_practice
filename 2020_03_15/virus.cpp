//https://www.acmicpc.net/problem/14502
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
	int N,M;
	int answer=0;
	vector<vector<int>> board;
	vector<vector<int>> blank;	//빈 칸 좌표
	vector<vector<int>> virus;	//바이러스 좌표
	cin>>N>>M;

	//입력 받아서 위에 3가지 벡터 채움
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

	//벽을 세울 위치 3개를 조합으로 구하기 위한 index 벡터
	vector<int> ind={1,1,1};
	for(int i=0;i<blank.size()-3;i++){
		ind.push_back(0);
	}
	sort(ind.begin(),ind.end());

	//dfs 돌때 인접한 칸 4개 비교를 편하게 하기위한 벡터
	vector<vector<int>> move={{1,0},{-1,0},{0,1},{0,-1}};

	//3개의 벽을 세울 수 있는 모든 조합에 대해 dfs
	do{
		//새로 세운 벽(3)
		int cnt=0;
		vector<vector<int>> temp = board;
		for(int i=0;i<ind.size();i++){
			if(ind[i]==1)
				temp[blank[i][0]][blank[i][1]]=3;
		}

		//virus 벡터에 있는 모든 좌표 스택에 push
		vector<vector<int>> stack;
		for(int i=0;i<virus.size();i++){
			stack.push_back(virus[i]);
		}

		//dfs돌면서 퍼진 바이러스 개수 count
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

		//빈 칸 개수에서 새로 세운 벽 3개랑 퍼진 바이러스 개수 빼서 최대값 계산
		if(blank.size()-3-cnt > answer) 
			answer = blank.size()-3-cnt;
	}while(next_permutation(ind.begin(),ind.end()));
	cout<<answer;
	return 0;
}