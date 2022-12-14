class Heap:
    def __init__(self,*args):
        if len(args)!=0:
            self.__A=args[0]
        else:
            self.__A=[]
    def __percolateUp(self,i):
        parent=(i-1)//2
        if i>0 and self.__A[i]>self.__A[parent]:
            self.__A[i],self.__A[parent]=self.__A[parent],self.__A[i]
            self.__percolateUp(parent)

    def insert(self,x):
        self.__A.append(x);
        self.__percolateUp(len(self.__A)-1)

    def deleteMax(self):
        if(not self.isEmpty()):
            max=self.__A[0]
            self.__A[0]=self.__A.pop()
            self.__percolateDown(0)
            return max
        else:
            return None
    def __percolateDown(self,i):
        child=2*i+1 #left child
        right=2*i+2 #right child
        if child<=len(self.__A)-1:
            if right<=len(self.__A)-1 and self.__A[child]<self.__A[right]:
                child=right
            if(self.__A[i]<self.__A[child]):
                self.__A[i],self.__A[child]=self.__A[child],self.__A[i]
    def max(self):
        return self.__A[0]
    def buildHeap(self):
        for i in range((len(self.__A)-2)//2,-1,-1):
            self.__percolateDown(i)
    def isEmpty(self):
        return len(self.__A)==0
    def clear(self):
        self.__A=[]
    def size(self):
        return len(self.__A)
    def printHeap(self):
        print(self.__A)


list=[]
list.pop()