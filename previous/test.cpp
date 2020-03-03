#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
 
using namespace std;
 
bool compare(pair<double, int> a, pair<double, int> b)
{
    // 실패율이 같다면 스테이지 번호가 작은것!
    if(a.first == b.first)
        return a.second < b.second;
    
    // 실패율이 큰것이 앞!
    return a.first > b.first;
}
 
vector<int> solution(int N, vector<int> stages) {
    vector<int> answer;
    int users[501]={0};
    int userSize = stages.size();
    vector<pair<double, int>> failure;
    
    // 각각의 스테이지에 도달한 유저수
    for(vector<int>::iterator it = stages.begin(); it!=stages.end(); it++)
        users[*it-1]++;
    
    for(int i=0; i<N; i++)
    {
        if(users[i] == 0)
            failure.push_back(make_pair(0, i+1));
        else
        {
            failure.push_back(make_pair((double)users[i]/userSize, i+1));
            userSize -= users[i];
        }
    }
    
    sort(failure.begin(), failure.end(), compare);
    
    for(vector<pair<double, int>>::iterator it = failure.begin(); it!=failure.end(); it++)
        answer.push_back(it->second);
 
    return answer;
}

int main(void){
    vector<int> a;
    vector<int> test = {5,4,3,2,1};
    vector<vector<int>> st = {{1,2},{2,3},{3,4},{4,5}};
    //a=solution(11,test);
    for(vector<vector<int>>::iterator i=st.begin();i!=st.end();){
        vector<int>::iterator temp = i->begin();
        if(temp[1]==4){
            i = st.erase(i);
        }else{
            i++;
        }
        //cout<<temp[1]<<endl;
    }

    /*
    for (vector<vector<int>>::iterator iter=st.begin();iter!=st.end();iter++){
        for(vector<int>::iterator j=iter->begin();j!=iter->end();j++){
            cout<<(*j)<<" ";
        }
        cout<<endl;
    }*/

    return 0;
}