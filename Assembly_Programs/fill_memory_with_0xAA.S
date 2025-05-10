# a is the current address, b is the constant to store, c is the amount to increment the address by
000 ldh a 0
001 ldl a 1
002 ldh b 10
003 ldl b 10
004 add c a # This stores 1 in c
005 ldh a 15 
006 ldl a 15
007 add d a # This stores 255 in d
008 ldh a 0
009 ldl a 0
010 str b a
011 add a c
012 nand d c
013 bgt - 3
