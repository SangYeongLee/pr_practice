#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long vsum(vector<int> v){
	long long ret = 0;
	for(int i=0;i<v.size();i++){
		ret+=v[i];
	}
	return ret;
}

int solution(vector<int> food_times, long long k) {
    if(vsum(food_times)<=k) return -1;

    vector<int> sorted = food_times;
    sort(sorted.begin(),sorted.end());

    int idx1=0;
    int idx2=0;
    int prev=0;
    while(true){
    	while(idx1<sorted.size()-1 && sorted[idx1]==sorted[idx1+1]){
    		idx1++;
    	}

    	if(sorted.size()-1==idx2){
    		break;
    	}

    	if(int(k/(sorted.size()-idx2)) >= sorted[idx1]-prev){
    		k -= (sorted[idx1]-prev)*(sorted.size()-idx2);
    		prev = sorted[idx1];
    		idx2 = idx1+1;
    		idx1++;
    	}else{
    		break;
    	}
    }

    k=k%(sorted.size()-idx2) +1;
    for(int i=0;i<food_times.size();i++){
    	if(food_times[i]>prev) k--;
    	if(k==0) return i+1; 
    }
    
}

int main(void){
	vector<int> test = {5,1,4,2,2};

	//cout<<*min_element(test.begin(),test.end())<<endl;
	cout<<solution(test,11)<<endl;
	return 0;
}