#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

vector<string> strtok(string str, char delim){
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

vector<string> solution(vector<string> record) {
    vector<string> answer;
    map<string,string> id;
    for (vector<string>::iterator iter=record.begin(); iter!=record.end();iter++)
    {
    	vector<string> temp = strtok(*iter, ' ');
    	if(!temp[0].compare("Enter") || !temp[0].compare("Change")){
    		id[temp[1]] = temp[2];
    	}	
    }
    
    for (vector<string>::iterator iter=record.begin(); iter!=record.end(); iter++)
    {
    	vector<string> temp = strtok(*iter, ' ');
    	
    	if(!temp[0].compare("Enter")){
    		answer.push_back(id[temp[1]]+"님이 들어왔습니다.");
    	}else if(!temp[0].compare("Leave")){
    		answer.push_back(id[temp[1]]+"님이 나갔습니다.");
    	}
    }

    return answer;
}

int main(void){
	vector<string> test = {"Enter uid1111 Sy","Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"};
	vector<string> ans;
	
	ans = solution(test);
	for(vector<string>::iterator iter=ans.begin();iter!=ans.end();iter++){
		cout<<*iter<<endl;
	}
	return 0;
}