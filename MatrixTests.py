#from sets import Set
from itertools import product





def SUPERSET(S):  # Generate relation containing all the subsets
       
        R= frozenset([])      
        R=[(i,j) for i,j in product(S,S)];
        return R

def THEMATRIX(A,c): # matrix builder assumes relation is built from a monotonous set of integers
        #in which for each a!=0 there is a b = a-1
    m = [[ 0 for x in xrange(c)] for y in xrange(c)]
    
    for x in range (c):
        for y in range (c):
           #if x in B and y in B:
             for i in range(len(A)):
                if A[i] == (x,y):
                        m[x][y]=1
                      # Remove else statement which brings everything back to 0!       
                #else:
                     #   m[x][y]=0
                        
    return m
     #Other trials   
    #while  x < c:
       # while y < c:
             #   B=Set([(x,y)])
              #  if B < A:
               #         m[x][y]=1
                #else:
                 #       m[x][y]=0
   # return m
    #for x in range(c-1):
       #     for y in range (c-1):
                #if(x,y) in A:
        #      
         #               m[x][y]=1
          #          elif i!= (x,y):
         #              m[x][y]=0
    #return m
    



def REFLEXIVE(R,count): #If a is a node in the set  (a,a) must be in the relation
    test = 0 
    for i in range(count):
                if R[i][i]==1:
                    test = test + 1
    return test==count
    
def IRREFLEXIVE(R,count): #if and only if the main diagonal of the matrix contains only 0s. No node is reflexive 
     test = 0
     for i in range (count):
             if R[i][i] == 0:
                test = test +1
     return test == count
     
     #Symmetry test Method uses diagonal as a mirror
def SYMMETRIC(A,c): #If (a,b) is in R then (b,a) must be in R
     count = ((c**2)-c) #this is the number of possible elements that are not reflexive
     s=0
     for x in range(c):
        for y in range(c):
            if x!=y and A[x][y] ==1 and A[y][x]==1:
                   s= s+1         
     return s==count

def ASYMETRIC(A,c): #for at least one link (a,b) its reflection(b,a) is not in the relation
     test = False
     for x in range(c):
        for y in range(c):
            if x!=y and A[x][y] != A[y][x]:
                test = True
     return test
 
def ANTISYMMETRIC(A,c): #for all (a,b) in relation R (b,a) is not in R
     test =0
     for x in range(c):
        for y in range(c):
            if x!=y and A[x][y] == 1  and A[y][x] == 1:
                test = test +1
     return test==0

def TRANSITIVE(A,c):# if links (a,b) and (b,c) are in the relation, (a,c) must also be present
      #if cardinality of set = 2 test is reflexivity of a and b if ab and ba are in the relation
    test = True  
    if c < 3:
        if (A[0][1] ==1 and A[1][0]==1):
            test = (A[0][0] ==1 and A[1][1] ==1)
        else:
            test = False
        return test
     #  Tests transitivity for more than 2 nodes
     # Tests the indexes forward going from a to c
    else:
        for x in range(c):
            for y in range ((x + 1),c):
                for z in range ((y + 1),c):
                    if A[x][y] == 1  and A[y][z] == 1 and A[x][z] != 1:
                        test = False
         #The reverse
        #Tests the indexes backwards ie going from node c to a                   
        c=c-1   
        for i in range(c,1, -1):
            for j in range ((i-1),0, -1):
                for k in range ((j-1),-1, -1):
                    if A[i][j] == 1 and A[j][k] == 1 and A[i][k] != 1:
                        test = False     
           
        return test
 #PRINTER methopd passes all the relations through all the methods and displays the results
def PRINTER(R,L):
        print "The relation tuples"
        print R
        print "Its binary matrix"
        M =  THEMATRIX(R,L)
        for index, item in enumerate (M,start=1):
            print(item)
            if not index % L:
                print("")
        
       
        print "Reflexive test"
        print REFLEXIVE(M,L);
        print "Irreflexive test"
        print IRREFLEXIVE(M,L);
        print "Symmetry test?"
        print SYMMETRIC(M,L);
        print "Asymetic test?"
        print ASYMETRIC(M,L);
        print "Antisymmetry test"
        print ANTISYMMETRIC(M,L)
        print "Transitivity test"
        print TRANSITIVE(M,L)
        print " "

def Main():
        #Here are the sets
        A = frozenset ([0,1])
        B = frozenset([0,1,2,3])
        #set with all the relations
        sset= SUPERSET(B);
        #sset minus some links to test the methods especially transitivity             
        big = (0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 1),  (3, 2), (3, 3)
        # The relations
        R1 = (0,0),(0,1),(1,0),(1,1)
        R2 = (0,0),(0,1),(1,0)
        R3 = (0,0),(0,1),(1,1)
        R4 = (0,0),(1,0),(1,1)
        R5 = (0,1),(1,0),(1,1)	
        R6 = (0,0),(0,1)	
        R7 = (0,0),(1,0)	
        R8 = (0,0),(1,1)	
        R9 = (0,1),(1,0)	
        R10 = (0,1),(1,1)	
        R11 = (1,0),(1,1)
        R12 = (0,0),
        R13 = (0,1),
        R14 = (1,0),
        R15 = (1,1),	
        R16 = ()
        
        #print sset
        
        Rel = [R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16]
        for i in Rel:
           PRINTER(i,len(A))
        #Larger relations to test functions   
        PRINTER(sset,len(B))
        PRINTER(big,len(B))
       
        
        
        
Main()
