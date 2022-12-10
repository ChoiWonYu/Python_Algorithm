class TreeNode:
    def __init__(self,newItem,left,right):
        self.item=newItem
        self.left=left
        self.right=right

class BinarySearchTree:
    def __init__(self):
        self.__root=None
    def insert(self,newItem):
        self.__root=self.__insertItem(self.__root,newItem)
    def returnRoot(self):
        return self.__root
    def __insertItem(self,tNode:TreeNode,newItem)->TreeNode:
        if(tNode==None):
            tNode=TreeNode(newItem,None,None)
        elif(newItem<tNode.item):
            tNode.left=self.__insertItem(tNode.left,newItem)
        else:
            tNode.right=self.__insertItem(tNode.right,newItem)
        return tNode
    def delete(self,x):
        self.__root=self.__deleteItem(self.__root,x)
    def __deleteItem(self,tNode:TreeNode,x)->TreeNode:
        if(tNode==None):
            return None
        elif x==tNode.item:
            tNode=self.__deleteItem(tNode)
        elif x<tNode.item:
            tNode.left=self.__deleteItem(tNode.left,x)
        else:
            tNode.right=self.__deleteItem(tNode.right,x)
        return tNode
    def __deleteNode(self,tNode:TreeNode)->TreeNode:
        if tNode.left==None and tNode.right==None:
            return None
        elif tNode.left==None:
            return tNode.right
        elif tNode.right==None:
            return tNode.left
        else:
            rtnItem,rtnNode=self.__deleteMinItem(tNode.right)
            tNode.item=rtnItem
            tNode.right=rtnNode
            return tNode
    def __deleteMinItem(self,tNode:TreeNode)->tuple:
        if tNode.left==None:
            return (tNode.item,tNode.right)
        else:
            (rtnItem,rtnNode)=self.__deleteMinItem(tNode.left)
            tNode.left=rtnNode
            return (rtnItem,tNode)
    def isEmpty(self)->bool:
        return self.__root==self.NIL
    def clear(self):
        self.__root=self.NIL
    def printInOrder(self,root):
        if root:
            self.printInOrder(root.left)
            print(root.item,end=' ')
            self.printInOrder(root.right)

    def printPostOrder(self, root):
        if root:
            self.printPostOrder(root.left)
            self.printPostOrder(root.right)
            print(root.item, end=' ')
    def printPreOrder(self,root):
        if root:
            print(root.item, end=' ')
            self.printPreOrder(root.left)
            self.printPreOrder(root.right)

bst1=BinarySearchTree()
bst1.insert(10)
bst1.insert(20)
bst1.insert(5)
bst1.insert(80)
bst1.insert(90)
bst1.insert(700)
bst1.insert(30)
bst1.insert(77)
bst1.insert(15)
bst1.insert(40)
bst1.insert(700)
bst1.insert(10)
print('InOrder : ',end=' ')
bst1.printInOrder(bst1.returnRoot())
print('\nPreOrder : ',end=' ')
bst1.printPreOrder(bst1.returnRoot())
print('\nPostOrder : ',end=' ')
bst1.printPostOrder(bst1.returnRoot())