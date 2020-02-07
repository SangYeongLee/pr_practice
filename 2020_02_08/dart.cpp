#include <iostream>
#include <string>

using namespace std;

int solution(string dartResult) {
    int answer = 0;
    int prev = 0;
    int cur=0;

    for(int i=0;i<dartResult.size();i++){
    	if(dartResult[i]>='0' and dartResult[i]<='9'){
    		answer+=prev;
    		prev = cur;
    		cur = stoi(&dartResult[i]);
    		if(cur==10) i++;
    	}else{
    		switch(dartResult[i]){
    			case 'D':
    				cur=cur*cur;
    				break;
    			case 'T':
    				cur=cur*cur*cur;
    				break;
    			case '*':
    				cur=cur*2;
    				prev=prev*2;
    				break;
    			case '#':
    				cur=-cur;
    				break;
    			default:
    			break;
    		}
    	}
    }
    answer+=cur+prev;

    return answer;
}

int main(void){
	string test = "1T2D3D#";
	cout<<solution(test)<<endl;
	return 0;
}