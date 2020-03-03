#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int retmin(vector<int> v){
	int ret = 100000000;

	for(int i=0;i<v.size();i++){
		if(v[i]!=0 && v[i]<ret)
			ret = v[i];
	}

	return ret;
}

int solution(vector<int> food_times, long long k) {
    int answer = 0;
    int zero=0;

    while(true){
    	int min = retmin(food_times);
    	int temp = 0;
    	cout<<"min : "<<min<<" size : "<<k<<endl;

    	if(zero==food_times.size()) return -1;
	    if(int(k/(food_times.size()-zero)) >= min){
	    	for(vector<int>::iterator i = food_times.begin();i!=food_times.end();i++){
	    		if(*i!=0){
	    			*i = *i-min;
	    			if(*i==0) temp++;
	    		}
	    	}

	    	k -= min*(food_times.size()-zero);
	    	zero += temp;
	    	cout<<"min : "<<min<<" size : "<<k<<endl;
		    for(vector<int>::iterator i = food_times.begin();i!=food_times.end();i++){
		    		cout<<*i<<endl;
		    }
	    }else{
	    	break;
	    }
	}

	k = k%(food_times.size()-zero)+1;
	cout<<"  "<<k<<endl;
    for(vector<int>::iterator i = food_times.begin();i!=food_times.end();i++){
    		cout<<*i<<endl;
    }

    for(int i=0;i<food_times.size();i++){
    	if(food_times[i]!=0) k--;
    	if(k==0) return i+1;
    }
}

int main(void){
	vector<int> test = {5,2,3,1,2};

	//cout<<*min_element(test.begin(),test.end())<<endl;
	cout<<solution(test,10)<<endl;
	return 0;
}