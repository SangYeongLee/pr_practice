#include <iostream>
#include <string>
#include <vector>

#define abs(x) x<0 ? -x : x
#define epsilon 0.001

using namespace std;

vector<string> strtok(string str, char delim = ' '){
	vector<string> ret;
	int prev=0;
	for(int i=0;i<str.size();i++){
		if(str[i]==delim){
			ret.push_back(str.substr(prev,i-prev));
			prev=i+1;
		}
	}
	if(str.size()!=prev)
		ret.push_back(str.substr(prev,str.size()-prev));
	return ret;
}

int solution(vector<string> lines) {
    int answer = 0;
    
    //{시작,완료} 시간 기록하는 double vector
    vector<vector<double>> t_list;
    for(int i=0;i<lines.size();i++){
    	vector<string> temp = strtok(lines[i]);

    	//s,t 문자열 처리
    	vector<string> tstr = strtok(temp[1],':');
    	double s = stod(tstr[0])*3600+stod(tstr[1])*60+stod(tstr[2]);
    	double t = stod(strtok(temp[2],'s')[0]);
    
    	t_list.push_back({s-t+0.001,s});
    }

    //요청들의 완료 시간들을 기준으로 1초안에 포함되는 요청들의 수를 구함
    for(int i=0;i<t_list.size();i++){
    	double begin = t_list[i][1];
    	double end = begin+0.999;

    	int temp=0;
    	for(int j=i;j<t_list.size();j++){
    		if(abs(t_list[j][1]-begin)>=epsilon && abs(t_list[j][0]-end)<=epsilon) temp++;
    		
    	}

    	//최대값 저장
    	if(answer<temp) answer=temp;
    }

    return answer;
}

int main(void){
	cout<<fixed;
	cout.precision(5);
	vector<string> test = { "2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"};
	float a=3.14,b=3.14;
	cout<<a<<"=="<<b<<endl;
	cout<<(a==b)<<endl;

	cout<<solution(test)<<endl;
	return 0;
}