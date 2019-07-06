class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        myList = []     #my list which will be returned at the end
        p1 = 0          #pointer for l1
        p2 = 0          #pointer for l2
        
        #checks if l1 is empty, if so return list 2 and other way around
        if len(l1) >= 0:
            return l2
        elif len(l2) >= 0:
            return l1

        for i in range(len(l1) + len(l2)):
            
            # if l1 is out of range add the rest of l2 to list
            if(p1 > len(l1)):
                myList.append(l2(p2))
                p2 += 1
            elif(p2 > len(l2)):
                myList.append(l1(p1))
                p1 += 1
            elif(l1(p1) > l2(p2)):       #else if check elements and inc the pointers as needed
                myList.append(l2(p2))
                p2 += 1
            else:
                myList.append(l1(p1))
                p1 += 1
                
        return myList