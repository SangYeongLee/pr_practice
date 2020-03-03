#include <iostream>
#include <vector>

using namespace std;

void heapify(vector<int>& list,int size,int i){
	if(size<=1) return;

	int cur = i*2+1;
	if(cur < size-1 && list[cur] < list[cur+1]) cur++;

	if(list[i] < list[cur]){
		swap(list[i],list[cur]);
		if(cur <= size/2-1) heapify(list,size,cur);
	}
}

void heap_insert(vector<int>& list,int num){
	int i = list.size();
	list.push_back(num);

	while(i>0){
		if(list[(i-1)/2]<list[i])
			swap(list[(i-1)/2],list[i]);
		i=(i-1)/2;
	}
}

int heap_del(vector<int>& list){
	int ret = list[0];

	list[0]=list[list.size()-1];
	list.pop_back();

	heapify(list,list.size(),0);

	return ret;
}

void heap_sort(vector<int>& list){
	vector<int> sorted;
	int size =list.size(); 
	for(int i=size/2-1;i>=0;i--)
		heapify(list,size,i);

	while(size>0){
		swap(list[0],list[size-1]);
		size--;
		heapify(list,size,0);
	}
}

int main(void){
	vector<int> list = {9,5,4,1,3};

	heap_insert(list,7);
	//heap_sort(list);

	for(int i=0;i<list.size();i++){
		cout<<list[i]<<" ";
	}
	cout<<endl;

	return 0;
}