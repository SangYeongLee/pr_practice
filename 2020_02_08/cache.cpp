#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool lru(vector<string>& cache,int cacheSize,string target){
	//cache에 해당 string있으면 해당 iterator return, 아니면 end() return
	vector<string>::iterator iter = find(cache.begin(),cache.end(),target);
	
	//cache가 다 차있지 않을때
	if(cache.size()<cacheSize){
		if(iter==cache.end()){	//cache안에 없을 경우 그냥 넣음
			cache.push_back(target);
			return false;
		}else{					//cache안에 있을 경우 그거 지우고 뒤로 밈
			cache.erase(iter);
			cache.push_back(target);
			return true;
		}
	}

	if(iter==cache.end()){	//cache 교체해야 할 경우 begin()지우고 넣음
		cache.erase(cache.begin());
		cache.push_back(target);
		return false;
	}else{					//있을 경우 그거 지우고 뒤로 밈
		cache.erase(iter);
		cache.push_back(target);
		return true;
	}
}

int solution(int cacheSize, vector<string> cities) {
    int answer = 0;
    vector<string> cache;
    //cacheSize 0일때 예외 처리
    if(cacheSize==0) return 5*cities.size();
    
    for(vector<string>::iterator iter=cities.begin();iter<cities.end();iter++){
    	//전부 소문자로
    	transform((*iter).begin(), (*iter).end(), (*iter).begin(), ::tolower);

    	if(lru(cache,cacheSize,(*iter))) answer+=1; //lru로 교체 안되면
    	else answer+=5; //lru로 교체되면
    }

    return answer;
}

int main(int argc, char const *argv[])
{
	vector<string> test = {"Jeju","NewYork","Seoul","newYork"};
	
	cout<<solution(0,test)<<endl;
	return 0;
}