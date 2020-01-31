#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(string str1, string str2) {
    int answer = 0;
    vector<string> set1,set2;
    int inter=0,sum=0;

    //문자열 전처리(소문자로 다 바꾸고 string vector에 원소를 넣어 집합만듬)
    for(int i=0;i<str1.size();i++){
    	if(str1[i]>=65 && str1[i]<97) str1[i]+=32;
    }
    for(int i=0;i<str2.size();i++){
    	if(str2[i]>=65 && str2[i]<97) str2[i]+=32;
    }

    for(int i=0;i<str1.size()-1;i++){
    	if(str1[i]>=97 && str1[i]<=122 && str1[i+1]>=97 && str1[i+1]<=122){
    		set1.push_back(str1.substr(i,2));
    	}
	}
	for(int i=0;i<str2.size()-1;i++){
    	if(str2[i]>=97 && str2[i]<=122 && str2[i+1]>=97 && str2[i+1]<=122){
    		set2.push_back(str2.substr(i,2));
    	}
	}

	//둘 다 공집합일 경우 예외처리
	if(set1.size()==0 && set2.size()==0) return 65536;

	//첫 번째 집합의 원소들 교집합, 합집합 계산
	while(set1.size()!=0){
		string temp = set1[0];
		int cnt1=0,cnt2=0;

		//첫 번째 집합안의 중복 원소 개수 찾기
		for(vector<string>::iterator iter=set1.begin();iter!=set1.end();){
			if((*iter).compare(temp)==0){
				cnt1++;
				iter = set1.erase(iter);
			}else{
				iter++;
			}
		}

		//두 번째 집합안에 중복 원소 개수 찾기
		for(vector<string>::iterator iter=set2.begin();iter!=set2.end();){
			if((*iter).compare(temp)==0){
				cnt2++;
				iter = set2.erase(iter);
			}else{
				iter++;
			}
		}

		//중복 원소 개수가 큰 값을 합집합에 더하고 작은 값을 교집합에 더함
		if(cnt1<cnt2){
			inter+=cnt1;
			sum+=cnt2;
		}else{
			inter+=cnt2;
			sum+=cnt1;
		}
	}

	//두 번째 집합에 남아있는 원소 수만큼 합집합에 넣기
	while(set2.size()!=0){
			sum+=set2.size();
			set2.clear();
	}

    return (inter*65536)/sum;
}

int main(void){
	string str1 = "aa1+aa2";
	string str2 = "shake hands";

	cout<<solution(str1,str2)<<endl;
	return 0;
}