//https://www.acmicpc.net/problem/14890
#include <iostream>

#define abs(a) (a>0 ? a : -a)

using namespace std;

int main(){
	int N,L;
	int ans = 0;
	cin>>N;
	cin>>L;

	int board[100][100];

	for(int i=0;i<N;i++){
		for(int j=0;j<N;j++){
			cin>>board[i][j];
		}
	}

	//가로
	for(int i=0;i<N;i++){
		int cnt=1; //평평한 칸 개수 저장
		bool flag=true; //해당 행 혹은 열을 지나갈 수 있는지
		for(int j=0;j<N-1;j++){
			int diff = board[i][j]-board[i][j+1];
			if(diff==-1){ // 올라갈때
				if(cnt<L){
					flag = false;
					break;
				}
				else
					cnt=1;
			}else if(diff==1){ // 내려갈때
				cnt=1;
				j++;
				//앞에 몇개의 평평한 칸이 있는지 체크
				while(j<N-1 && board[i][j]==board[i][j+1]){
					cnt++;
					j++;
				}

				//경사로를 놓을 수 있는지
				if(cnt<L){
					flag=false;
					break;
				}else{
					//경사로를 놓고 남은 평평한 칸 개수
					cnt=cnt-L;
					j--;
				}
			}else if(abs(diff)>1){ //높이가 1 이상 차이나면 패스
				flag = false;
				break;
			}else{ // 평지
				cnt++;
			}
		}
		if(flag) ans++;

		//세로 반복
		cnt=1;
		flag = true;
		for(int j=0;j<N-1;j++){
			int diff = board[j][i]-board[j+1][i];
			if(diff==-1){
				if(cnt<L){
					flag = false;
					break;
				}
				else
					cnt=1;
			}else if(diff==1){
				cnt=1;
				j++;
				while(j<N-1 && board[j][i]==board[j+1][i]){
					cnt++;
					j++;
				}

				if(cnt<L){
					flag=false;
					break;
				}else{
					cnt=cnt-L;
					j--;
				}
			}else if(abs(diff)>1){
				flag = false;
				break;
			}else{
				cnt++;
			}
		}

		if(flag) ans++;
	}

	cout<<ans;
	return 0;
}