class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort() 
        m=arr[1]-arr[0]
        #calculate minimun difference
        for i in range(len(arr)-1): 
            if m>arr[i+1]-arr[i]: 
                m=arr[i+1]-arr[i] 
        l=[] 
        #populate pairs with smallest difference
        for i in range(len(arr)-1): 
            if arr[i+1]-arr[i]==m: 
                l.append([arr[i],arr[i+1]])        
        return l   