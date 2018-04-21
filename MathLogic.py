

def MAIN():


    A = frozenset(['a','b','c','d','e','f','g','h','i'])
    B = frozenset(['g','h','i','j','k','l','m','n','o'])
    C = frozenset(['m','n','o','p','q','r','s','t','u'])
    D = frozenset(['r','s','t','u','v','w','x','y','z'])
    
    #test left side == right side
    print "Q1 a: the formula (A and B) or (C and D) ==  (A and D) or (C and B) is {}".format((A & B | C & D) == (A & D |C & B))
    
     
    print " "
    #part B using same sets as a
    print'Q1 b: The formula A - (B|C) == (A-B) &(A-C) is {}'.format(A-(B | C)== (A-B)&(A-C))
    
   






MAIN()
