#include <iostream>
#include <string>
#include <vector>

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


double timeSub(double s,double t){
	double ret = s-t;
	if(ret-int(ret/100)*100 > 60) ret-=40;
	if(ret-int(ret/10000)*10000 > 6000) ret-=4000;
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
    	double s = stod(tstr[0])*10000+stod(tstr[1])*100+stod(tstr[2]);
    	double t = stod(strtok(temp[2],'s')[0]);
    
    	t_list.push_back({timeSub(s,t-0.001),s});
    }

    for(int i=0;i<t_list.size();i++){
    	double begin = t_list[i][1];
    	double end = begin+0.999;

    	int temp=0;
    	for(int j=i;j<t_list.size();j++){
    		if(t_list[j][1]>=begin && t_list[j][0]<=end) temp++;
    	}

    	if(answer<temp) answer=temp;
    }

    return answer;
}

/*
double timeAdd(double s, double t){
	double ret = s+t;
	if(ret-int(ret/100)*100 > 60) ret+=40;
	if(ret-int(ret/10000)*10000 > 6000) ret+=4000;
	return ret;
}*/

int main(void){
	cout<<fixed;
	cout.precision(3);
	vector<string> test = { "2016-09-15 20:59:57.421 0.351s",
							"2016-09-15 20:59:58.233 1.181s",
							"2016-09-15 20:59:58.299 0.8s",
							"2016-09-15 20:59:58.688 1.041s",
							"2016-09-15 20:59:59.591 1.412s",
							"2016-09-15 21:00:00.464 1.466s",
							"2016-09-15 21:00:00.741 1.581s",
							"2016-09-15 21:00:00.748 2.31s",
							"2016-09-15 21:00:00.966 0.381s",
							"2016-09-15 21:00:02.066 2.62s"};
	//string a = strtok(test[0],'s')[0];
	//a.append("ddd");
	cout<<solution(test)<<endl;
	return 0;
}