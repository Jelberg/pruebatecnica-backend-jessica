arr=[1,2,3,4,5]
arr_des = [5,2,3,4,1]
comp =[]

    
                
def find_3(arr):
    n = len(arr)

    element = 0
    for i in range(0,n):
        if (i+1) not in arr:
            element = i+1
    
            
    return element 
   
     
                
        
        
print(find_3(arr))

