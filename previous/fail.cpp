#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(vector<int> a, vector<int> b){
	double aval,bval;
	if(a[2]==0) aval=0;
	else aval = (double)a[1] / (double)a[2];

	if(b[2]==0) bval=0;
	else bval = (double)b[1] / (double)b[2];

	if(aval==bval) return a[0]<b[0];
	return aval>bval;
}

vector<int> solution(int N, vector<int> stages) {
    vector<int> answer;
    vector<vector<int>> total;

    for (int i = 0; i < N+1; i++){
    	total.push_back({i+1,0,0});
    }

    for(int i=0;i<stages.size();i++){
    	for(int j=0;j<stages[i];j++) total[j][2]+=1;
    	total[stages[i]-1][1]+=1;
    }

    total.pop_back();
    sort(total.begin(),total.end(),cmp);

    for(int i=0;i<total.size();i++){
    	answer.push_back(total[i][0]);
    }

    return answer;
}

int main(void){
	cout<<fixed;
	cout.precision(3);
	vector<int> a;
	vector<int> test = {2,2,1};
	a=solution(11,test);
	for(int i=0;i<a.size();i++)
		cout<<a[i]<<" ";
	cout<<endl;
	return 0;
}