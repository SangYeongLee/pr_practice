#include <iostream>
#include <vector>

using namespace std;

void merge(vector<int>& list,int left,int mid,int right){
	vector<int> sorted;
	int i=left;
	int j=mid+1;

	while(i<=mid && j<=right){
		if(list[i]<list[j]){
			sorted.push_back(list[i++]);
		}else{
			sorted.push_back(list[j++]);
		}
	}

	if(i<=mid){
		for(int k=i;k<=mid;k++)
			sorted.push_back(list[k]);
	}else{
		for(int k=j;k<=right;k++)
			sorted.push_back(list[k]);
	}

	int l=0;
	for(int k=left;k<=right;k++){
		list[k] = sorted[l];
		l++;
	}
}

void merge_sort(vector<int>& list,int left,int right){
	int mid = (left+right)/2;

	if(left<right){
		merge_sort(list,left,mid);
		merge_sort(list,mid+1,right);
		merge(list,left,mid,right);
	}
}

int main(void){
	vector<int> list = {4,15,17,7,1,9,12,8,3,10,11};

	merge_sort(list,0,list.size()-1);
	for (int i = 0; i < list.size(); i++)
	{
		cout<<list[i]<<" ";
	}
	cout<<endl;

	return 0;
}