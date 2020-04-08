//https://www.acmicpc.net/problem/2156
#include <iostream>

using namespace std;

int main(){
	int n,ans;
	cin>>n;

	int* grape = new int[n];
	int* dpo = new int[n];
	int* dpx = new int[n];
	
	for(int i=0;i<n;i++){
		cin>>grape[i];
	}
	if(n==1){
		cout<<grape[0];
		return 0;
	}

	dpo[0] = grape[0];
	dpx[0] = grape[0];
	dpo[1] = grape[0]+grape[1];
	dpx[1] = grape[1];

	ans = max(max(dpx[0],dpo[0]),max(dpx[1],dpo[1]));

	for(int i=2;i<n;i++){
		dpo[i] = dpx[i-1]+grape[i];
		if(i==2)
			dpx[i] = max(dpo[i-2],dpx[i-2])+grape[i];
		else
			dpx[i] = max(max(dpo[i-2],dpx[i-2]),max(dpo[i-3],dpx[i-3]))+grape[i];

		if(max(dpx[i],dpo[i])>ans) ans = max(dpx[i],dpo[i]);
	}

	cout<<ans;
	return 0;
}