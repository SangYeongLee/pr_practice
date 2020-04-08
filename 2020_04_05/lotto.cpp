//https://www.acmicpc.net/problem/6603
#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> comb(vector<int> num,int n){
	vector<vector<int>> ret;


	if(n==1){
		for(int i=0;i<num.size();i++)
			ret.push_back({num[i]});
	}else{
		for(int i=0;i<num.size()-n+1;i++){
			vector<int> sub;
			sub.assign(num.begin()+i+1,num.end());
			vector<vector<int>> c = comb(sub,n-1);

			for(int j=0;j<c.size();j++){
				vector<int> origin = {num[i]};
				origin.insert(origin.end(),c[j].begin(),c[j].end());
				ret.push_back(origin);
			}
		}
	}


	return ret;
}

int main(){
	int n;
	int temp;
	while(true){
		cin>>n;
		if(n==0) break;

		vector<int> num;
		vector<vector<int>> ans;

		for(int i=0;i<n;i++){
			cin>>temp;
			num.push_back(temp);
		}
		ans = comb(num,6);
		
		for(int i=0;i<ans.size();i++){
			for(int j=0;j<6;j++){
				cout<<ans[i][j];
				if(j!=5) cout<<" ";
			}
			cout<<endl;
		}

		cout<<endl;
	}

	return 0;
}