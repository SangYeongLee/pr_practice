#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
//시간 -> int
int t2i(string time){
	int ret=0;
	ret+= stoi(time.substr(0,2))*60+stoi(time.substr(3,2));

	return ret;
}

//int -> 시간
string i2t(int num){
	string ret;
	int hh = num/60;
	int mm = num%60;
	if(hh<10) ret="0"+to_string(hh); else ret=to_string(hh);
	if(mm<10) ret+=":0"+to_string(mm); else ret+=":"+to_string(mm);

	return ret;
}

string solution(int n, int t, int m, vector<string> timetable) {
    string answer = "";
    sort(timetable.begin(),timetable.end(),greater<string>());
    int bus,cnt,prev;

    //마지막 셔틀을 제외한 나머지 셔틀 처리
    for(int i=0;i<n-1;i++){
    	bus = t2i("09:00")+i*t; //셔틀 출발 시간 계산
    	
    	cnt=0; //탑승 인원 count
    	while(true){
    		if(cnt==m || timetable.size()==0) break; //만석이거나 더 이상 탑승할 사람이 없을때

    		if(t2i(timetable.back())<=bus){
    			timetable.pop_back();
    			cnt++;
    		}else{
    			break;
    		}
    	}
    }

    //마지막 셔틀 처리
    cnt=0;
    bus = t2i("09:00")+(n-1)*t;
    while(true){
    	if(cnt==m || timetable.size()==0) break;

    	prev = t2i(timetable.back()); //마지막 탑승 인원 도착시간 기억
    	if(prev <= bus){
    		cnt++;
    		timetable.pop_back();
    	}else{
    		break;
    	}
    }

    if(cnt!=m) return i2t(bus); //마지막 셔틀이 만석이 아닐때 셔틀시간 return
    else return i2t(prev-1); //마지막 셔틀이 만석일 때 가장 늦게 탑승한 사람에서 1분 빼고 return
}

int main(void){
	vector<string> test = {"08:00", "08:00", "08:00", "08:00"};
	
	cout<<solution(1,1,5,test)<<endl;
	return 0;
}