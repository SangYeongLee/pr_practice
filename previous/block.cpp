#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool chk_empty(int row,int col,vector<vector<int>> board){
	for(int i=row-1;i>=0;i--){
		if(board[i][col]!=0) return false;
	}
	return true;
}

bool remove23(int row,int col,vector<vector<int>> board){
	int target;
	int t_cnt=0;
	int b_cnt=0;
	
	if(board[row+1][col+2]==0) return false;
	else target = board[row+1][col+2];

	for(int i=0;i<2;i++){
		for(int j=0;j<3;j++){
			if(board[row+i][col+j]==target) t_cnt++;
			else if(board[row+i][col+j]==0 && chk_empty(row+i,col+j,board)) b_cnt++;
		}
	}

	if(t_cnt==4 && b_cnt==2) return true;
	else return false;
}

bool remove32(int row,int col,vector<vector<int>> board){
	int target;
	int t_cnt=0;
	int b_cnt=0;
	
	if(board[row+2][col+1]==0) return false;
	else target = board[row+2][col+1];

	for(int i=0;i<3;i++){
		for(int j=0;j<2;j++){
			if(board[row+i][col+j]==target) t_cnt++;
			else if(board[row+i][col+j]==0 && chk_empty(row+i,col+j,board)) b_cnt++;
		}
	}

	if(t_cnt==4 && b_cnt==2) return true;
	else return false;
}

int solution(vector<vector<int>> board) {
    int answer = 0;
    int size = board.size();

    while(true){
    	int cnt=0;

    	for(int i=0;i<size-1;i++){
	    	for(int j=0;j<size-1;j++){
	    		if(i<size-2 && remove32(i,j,board) ){
	    			for(int y=0;y<3;y++){
	    				for(int x=0;x<2;x++)
	    					board[i+y][j+x] = 0;
	    			}
	    			cnt++;
	    		}else if(j<size-2 && remove23(i,j,board) ){
	    			for(int y=0;y<2;y++){
	    				for(int x=0;x<3;x++)
	    					board[i+y][j+x] = 0;
	    			}
	    			cnt++;
	    		}
	    	}
	    }

    	if(!cnt) break;
    	answer+=cnt;
    }

    return answer;
}

int main(void)
{
	vector<vector<int>> test = {{0,0,0,0,0},
								{0,0,1,3,3},
								{1,1,1,3,0},
								{0,0,2,3,0},
								{0,0,2,2,2}};
	cout<<solution(test)<<endl;
	return 0;
}