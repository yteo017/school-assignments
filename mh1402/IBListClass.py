class IBList:
    
    def __init__(self,S): #initializing
        self.lst = S

    def get(self,r):
        """return the element of S with index r
        an error condition occurs if r<0 or r>n-1,
        where n is the length of list S"""
        if r < 0 or r > len(S)-1:
            return('Error')
        else:
            return S[r]
    
    def set_(self,r,e):
        """replace with e the element ar index r
        and return it
        an error condition occurs if r<0 or r>n-1,
        where n is the length of list S"""
        if r < 0 or r > len(S)-1:
            return('Error')
        else:
            y = S[r] #let y be the old element at index r
            S[r] = e #set the new element to index r
            return y #return the old element
            
    
    def add(self,r,e):
        """insert a new element e into S to have index r
        an error condition occurs if r<0 or r>n,
        where n is the length of list S"""
        if r < 0 or r > len(S):
            return('Error')
        else:
            S.insert(r,e)
            return S
    
    def remove(self,r):
        """remove from S the element at index r
        an error condition occurs if r<0 or r>n-1,
        where n is the length of list S"""
        if r < 0 or r > len(S)-1:
            return('Error')
        else:
            x = S[r] #let x be the element to be removed at index r
            del S[r] #remove the element at index r by using the delete function
            return x #return the deleted element