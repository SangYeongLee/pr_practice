#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

bool chk(vector<vector<string>> relation, vector<int> index){
	set<vector<string>> chkSet;
	vector<string> temp;

	for(int i=0;i<relation.size();i++){
		temp={};
		for(int j=0;j<index.size();j++)
			temp.push_back(relation[i][index[j]]);

		chkSet.insert(temp);
	}
	if(chkSet.size()==relation.size())
		return true;
	else
		return false;
}

int compareBit(int a,int b){
	int cnt1=0,cnt2=0;

	while(a){
		if(a&1) cnt1++;
		a = (a>>1);
	}

	while(b){
		if(b&1) cnt2++;
		b = (b>>1);
	}
	return cnt1>cnt2;
}

vector<int> comb(int num){
	vector<int> ret;
	int i=0;

	while(num>=(1<<i)){
		if((num&(1<<i))==(1<<i)){
			ret.push_back(i);
		}
		i++;
	}

	return ret;
}

int solution(vector<vector<string>> relation) {
    vector<int> uniqueSet;
    int anwser=0;

    for(int i=1;i<(1<<relation[0].size());i++){
    	if(chk(relation,comb(i))){
    		uniqueSet.push_back(i);
    	}
    }

    sort(uniqueSet.begin(),uniqueSet.end(),compareBit);
    
    while(!uniqueSet.empty()){
    	int minSet = uniqueSet.back();
    	uniqueSet.pop_back();
    	anwser++;

    	for(vector<int>::iterator iter=uniqueSet.begin(); iter!=uniqueSet.end();iter++){
    		if((*iter&minSet)==minSet){
    			uniqueSet.erase(iter);
    			iter--;
    		}
    	}
    }

    return anwser;
}

int main(void)
{
	vector<vector<string>> v;
	v.push_back({"100","ryan","music","2"});
	v.push_back({"200","apeach","math","2"});
	v.push_back({"300","tube","computer","3"});
	v.push_back({"400","con","computer","4"});
	v.push_back({"500","muzi","music","3"});
	v.push_back({"600","apeach","music","2"});

	cout<<solution(v)<<endl;
	return 0;
}