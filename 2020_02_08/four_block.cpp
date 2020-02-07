#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(int m, int n, vector<string> board) {
    int answer = 0;

    while(true){
	    int cnt=0;
	    //없앨 수 있는 블록들 소문자로 변경
	    bool flag=true;
	    for(int i=0;i<m-1;i++){
	    	for(int j=0;j<n-1;j++){
	    		if(board[i][j]==' ') continue;
	    		char temp = tolower(board[i][j]);
	    		if(temp == tolower(board[i][j+1]) && temp == tolower(board[i+1][j]) && temp == tolower(board[i+1][j+1])){
	    			board[i][j] = temp;
	    			board[i+1][j] = temp;
	    			board[i][j+1] = temp;
	    			board[i+1][j+1] = temp;
	    			flag=false;
	    		}
	    	}
	    }

	    if(flag) break; //지울게 없으면 break

	    for(int j=0;j<n;j++){
	    	vector<char> upper;
	    	int l=0;
	    	//대문자는 upper에 넣고, 소문자는 count
	    	for(int i=m-1;i>=0;i--){
	    		if(board[i][j]>=65 && board[i][j]<=96){
	    			upper.push_back(board[i][j]);
	    		}else if(board[i][j]>=97 && board[i][j]<=122){
	    			l++;
	    		}
	    	}

	    	//없앨 수 있는 게 없으면 스킵
			if(l==0) continue;
			else{
				int k=0;
				cnt+=l;
				//지워진 block자리 채우기
				for(int i=m-1;i>=0;i--){
		    		if(k<upper.size()){
		    			board[i][j]=upper[k];
		    			k++;
		    		}else{
		    			board[i][j]=' ';
		    		}
		    	}
			}	
	    }
		answer+=cnt;
	}

    return answer;
}

int main(void){
	vector<string> test = { "CCBDE", 
							"AAADE", 
							"AAABF", 
							"CCBBF"};
	
	cout<<solution(4,5,test)<<endl;
	return 0;
}