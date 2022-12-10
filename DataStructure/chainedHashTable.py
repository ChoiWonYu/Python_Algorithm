import LinkedListBasic
class ChainedHashTable:
    def __init__(self,n):
        self.__table=[LinkedListBasic() for _ in range(n)]
        self.__numItems=0
    def __hash(self,x):
        return x%len(self.__table)
    def insert(self,x):
        slot=self.__hash(x)
        self.__table[slot].insert(0,x)
        self.__numItems+=1
    def search(self,x):
        slot=self.__hash(x)
        if self.__table[slot].isEmpty():
            return None
        else:
            head=prev=self.__table[slot].getNode(-1)
            curr=prev.next
            while curr!=head:
                if curr.item==x:
                    return curr
                else:
                    prev=curr
                    curr=curr.next
            return None

