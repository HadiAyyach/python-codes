from typing import List
def kSumSubset(numArray: List[int], k: int) -> bool:
    # making array with the the indexes 
    index_arr = []
    for i in range(len(numArray)):
        index_arr.append(str(i))
    groups = []
    groups.append(index_arr)
    # this loop to loop for the number of elements inside the array
    # we can say that this one for incrementing the digits
    for i in range(1,len(index_arr)):
        #temp array 
        g=[]
        # this loop for looping over the last group
        for v1 in groups[-1] :
            #this loop for looping over the rest of the group elements
            for j in range(int(v1[-1])+1,len(index_arr)):
                g.append(v1+index_arr[j])
        groups.append(g)
    # here the main idea of this example 
    # here I see if any of the possible groups given the wanted number
    result = False
    for i in groups:
        for j in i :
            sum = 0
            for x in j :
                sum += int(numArray[int(x)])
            if sum == k :
                result = True
                break
        if result : break
    return result
        
            

            
            
    

    
    