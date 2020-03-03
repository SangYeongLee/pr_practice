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
    //모든 음식 다 먹은 시간이 k보다 작을때
    if(vsum(food_times)<=k) return -1;

    vector<int> sorted = food_times;
    sort(sorted.begin(),sorted.end());

    int idx1=0; //최소값의 index 중 가장 큰 값
    int idx2=0; //최소값의 index 중 가장 작은 값
    int prev=0; //이전에 처리한 최소값을 저장한 값
    while(true){
    	//정렬된 배열에서 같은 시간을 가진 음식의 index구하기
    	while(idx1<sorted.size()-1 && sorted[idx1]==sorted[idx1+1]){
    		idx1++;
    	}

    	if(sorted.size()-1==idx2){
    		break;
    	}
    	//배열 안에 남은 가장 작은 값만큼 도는 시간이 k보다 작을 경우
    	if(int(k/(sorted.size()-idx2)) >= sorted[idx1]-prev){
    		k -= (sorted[idx1]-prev)*(sorted.size()-idx2);
    		prev = sorted[idx1];
    		idx2 = idx1+1;
    		idx1++;
    	}else{
    		break;
    	}
    }

    //배열안에 0이 아닌 수를 나눈 나머지 구해서 +1
    k=k%(sorted.size()-idx2) +1;
    //k만큼 돌면서 다음 음식이 뭔지 찾음
    for(int i=0;i<food_times.size();i++){
    	if(food_times[i]>prev) k--;
    	if(k==0) return i+1; 
    }
    
}

int main(void){
	vector<int> test = {5,1,5,2,2};

	//cout<<*min_element(test.begin(),test.end())<<endl;
	cout<<solution(test,14)<<endl;
	return 0;
}