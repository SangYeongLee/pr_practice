//https://www.acmicpc.net/problem/14501
#include <iostream>
#include <vector>

using namespace std;

vector<int> dp;

int maxpay(vector<int> time,vector<int> pay,int day){
	if(dp[day]!=-1) return dp[day];

	int ret;
	
	if(day+time[day]>time.size()){
		ret = 0;
	}else if(day+time[day]==time.size()){
		ret = pay[day];
	}else{
		ret = pay[day]+maxpay(time,pay,day+time[day]);
	}

	int i=1;
	while(day+i<time.size()){
		int temp = maxpay(time,pay,day+i);

		if(ret < temp)
			ret = temp;
		i++;
	}

	dp[day] = ret;
	return ret;
}

int main(){
	int n;
	int t,p;
	vector<int> time;
	vector<int> pay;

	cin>>n;
	for(int i=0;i<n;i++){
		cin>>t>>p;
		time.push_back(t);
		pay.push_back(p);
		dp.push_back(-1);
	}

	cout<<maxpay(time,pay,0);
	return 0;
}