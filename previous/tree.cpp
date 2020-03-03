#include <iostream>
#include <vector>
#include <queue>

#define null 0

using namespace std;

class Node{
	friend class BST;
	private:
		int num;
		Node* left;
		Node* right;
	public:
		Node(int val){
			this->num = val;
			this->left = null;
			this->right = null;
		}

		~Node(){}

		int getNum(){
			return this->num;
		}

		Node* getLeft(){
			return this->left;
		}

		Node* getRight(){
			return this->right;
		}
};

class BST{
	private:
		Node* root;
	public:
		BST(){root=null;};
		~BST();

		Node* getRoot();
		void BSTinsert(int val);
		void preorder(Node* cur);
		void inorder(Node* cur);
		void postorder(Node* cur);
		bool isComplete(Node* cur);
		bool isLeaf(Node* cur);
};

Node* BST::getRoot(){
	return root;
}

void BST::BSTinsert(int val){
	if(root==null){ 
		root = new Node(val);
		return;
	}

	Node* temp = root;
	while(true){
		if(temp->num < val){
			if(temp->right == null){
				temp->right = new Node(val);
				break;
			}else{
				temp = temp->right;
			}
		}else{
			if(temp->left == null){
				temp->left = new Node(val);
				break;
			}else{
				temp = temp->left;
			}
		}
	}
}

void BST::inorder(Node* cur){
	if(cur!=null){
		BST::inorder(cur->left);
		cout<<cur->num<<endl;
		BST::inorder(cur->right);
	}
}

void BST::preorder(Node* cur){
	if(cur!=null){
		cout<<cur->num<<endl;
		BST::preorder(cur->left);
		BST::preorder(cur->right);
	}
}

void BST::postorder(Node* cur){
	if(cur!=null){
		BST::postorder(cur->left);
		BST::postorder(cur->right);
		cout<<cur->num<<endl;
	}
}

bool isLeaf(Node* cur){
	if(cur->getLeft()==null && cur->getRight()==null)
		return true;
	else
		return false;
}

bool isFullNode(Node* cur){
	if(cur->getLeft()!=null && cur->getRight()!=null)
		return true;
	else
		return false;
}

bool isComplete(Node* root){
	if(root==null) return true;

	queue<Node> q;
	q.push(*root);

	while(q.size()!=0){
		Node temp = q.front();
		if(!isFullNode(&temp)){
			if(temp.getLeft()==null && temp.getRight()!=null)
				return false;
			else{
				if(temp.getLeft()!=null) q.push(*(temp.getLeft()));
				q.pop();
				break;
			}
		}else{
			q.push(*(temp.getLeft()));
			q.push(*(temp.getRight()));
			q.pop();
		}
	}

	while(q.size()!=0){
		Node temp = q.front();
		if(!isLeaf(&temp)) return false;
		else q.pop();
	}
	return true;
}

int main(void){
	vector<int> list = {15,9,20,5,12,17,22,2,7};
	
	BST* tree = new BST();
	for(int i=0;i<list.size();i++){
		tree->BSTinsert(list[i]);
	}

	if(isComplete(tree->getRoot()))
		cout<<"Tree is complete"<<endl;
	else
		cout<<"Tree is not complete"<<endl;

	tree->BSTinsert(10);
	tree->BSTinsert(14);

	if(isComplete(tree->getRoot()))
		cout<<"Tree is complete"<<endl;
	else
		cout<<"Tree is not complete"<<endl;

	tree->BSTinsert(6);

	if(isComplete(tree->getRoot()))
		cout<<"Tree is complete"<<endl;
	else
		cout<<"Tree is not complete"<<endl;

	return 0;
}