//https://www.acmicpc.net/problem/14889
#include <iostream>
#include <vector>
#include <limits.h>

#define sumop(op) (op[0]+op[1]+op[2]+op[3])

using namespace std;

//연산 결과 반환하는 함수
int calc(int n1,int n2,int op){
	switch(op){
		case 0:	return n1+n2;
		case 1: return n1-n2;
		case 2: return n1*n2;
		default:
			return n1/n2;
	}
}

int main(){
	int n,temp;
	int max=INT_MIN,min=INT_MAX;
	vector<int> number;
	vector<int> op;
	cin>>n;

	//입력
	for(int i=0;i<n;i++){
		cin>>temp;
		number.push_back(temp);
	}

	for(int i=0;i<4;i++){
		cin>>temp;
		op.push_back(temp);
	}

	//dfs(스택 : [+,-,*,/,계산값])
	op.push_back(number[0]);

	vector<vector<int>> stack;
	stack.push_back(op);

	while(stack.size()!=0){
		vector<int> cur = stack.back();
		stack.pop_back();

		//연산자 모두 사용했을때
		if(sumop(cur)==0){
			if(cur[4]>max) max = cur[4];
			if(cur[4]<min) min = cur[4];
			continue;
		}

		//다음 자리에 넣을수 있는 경우 push
		for(int i=0;i<4;i++){
			if(cur[i]>0){
				vector<int> near = cur;
				near[i]-=1;
				near[4]=calc(cur[4],number[n-sumop(cur)],i);
				stack.push_back(near);
			}
		}
	}

	cout<<max<<endl;
	cout<<min<<endl;
	return 0;
}