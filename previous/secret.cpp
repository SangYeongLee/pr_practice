#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<string> solution(int n, vector<int> arr1, vector<int> arr2) {
    vector<string> answer={};
    for(int i=0;i<n;i++){
    	string ret="";

    	for(int j=n-1;j>=0;j--){
    		if(arr1[i]&(1<<j) || arr2[i]&(1<<j)) ret+='#';
    		else ret+=' ';
    	}
    	answer.push_back(ret);
    }
    return answer;
}

int main(int argc, char const *argv[])
{
	vector<int> arr1 = {9, 20, 28, 18, 11};
	vector<int> arr2 = {30, 1, 21, 17, 28};

	vector<string> test = solution(5,arr1,arr2);
	for(int i=0;i<test.size();i++){
		cout<<test[i]<<endl;
	}

	return 0;
}