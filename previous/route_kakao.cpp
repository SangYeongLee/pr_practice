#include <iostream>
#include <vector>
#include <algorithm>

#define null 0

using namespace std;

class Node{
	friend class Tree;
	private:
		vector<int> info;
		Node* left;
		Node* right;
	public:
		Node(vector<int> info,Node* left=null, Node* right=null){
			this->info = info;
			this->left = left;
			this->right = right;
		}
};

class Tree{
	private:
		Node* root;
	public:
		Tree(vector<vector<int>> info){
			root = new Node(info.back());
			info.pop_back();
			buildTree(info,root);
		}

		void buildTree(vector<vector<int>> info,Node* curr){
			vector<vector<int>> left;
			vector<vector<int>> right;

			vector<int> temp = curr->info;
			for(int i=0;i<info.size();i++){
				if(info[i][0]<temp[0]){
					left.push_back(info[i]);
				}else{
					right.push_back(info[i]);
				}
			}

			if(left.size()!=0){
				Node* t = new Node(left.back());
				left.pop_back();
				if(left.size()!=0) buildTree(left,t);
				curr->left = t;
			}

			if(right.size()!=0){
				Node* t = new Node(right.back());
				right.pop_back();
				if(right.size()!=0) buildTree(right,t);
				curr->right = t;	
			}
		}

		Node* getRoot(){
			return root;
		}

		void preorder(vector<int> &ret,Node* curr){
			if(curr != null){
				ret.push_back(curr->info[2]);
				preorder(ret,curr->left);
				preorder(ret,curr->right);
			}
		}

		void postorder(vector<int> &ret,Node* curr){
			if(curr != null){
				postorder(ret,curr->left);
				postorder(ret,curr->right);
				ret.push_back(curr->info[2]);
			}
		}
};

bool cmp(vector<int> v1, vector<int> v2){
		return v1[1]<v2[1];
}

vector<vector<int>> solution(vector<vector<int>> nodeinfo) {
    vector<vector<int>> answer;
    for(int i=0;i<nodeinfo.size();i++){
		nodeinfo[i].push_back(i+1);
	}

	sort(nodeinfo.begin(),nodeinfo.end(),cmp);

	vector<int> temp;
	Tree t(nodeinfo);
	
	t.preorder(temp,t.getRoot());
    answer.push_back(temp);
    temp.clear();

    t.postorder(temp,t.getRoot());
    answer.push_back(temp);

    return answer;
}

int main(void)
{
	vector<vector<int>> test = {{5,3},{11,5},{13,3},{3,5},{6,1},{1,3},{8,6},{7,2},{2,2}};
	vector<vector<int>> ans = solution(test);

	for(int i=0;i<ans.size();i++){
		for(int j=0;j<ans[i].size();j++)
			cout<<ans[i][j]<<" ";
		cout<<endl;
	}

	return 0;
}