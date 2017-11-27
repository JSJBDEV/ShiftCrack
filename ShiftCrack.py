#shift cracker
global iora;
iora = ""
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def crack(text):
    
    for integer in range(0,len(text)):
            
        v = text[integer]
        vv = text[integer+1]
        vvv = text[integer+2]
        if(v == " " and vvv == " "):
            iora = vv
            break
            
    

    #for the first 1 letter word being i
    shift = abs(8 - alpha.index(vv))
    print("assuming i the shift is: "+ str(shift))
    newlist = []
    for integer in range(0,len(text)):
        if text[integer] == ' ':
            newlist.append(" ")
            continue
        
        newlist.append(alpha[alpha.index(text[integer])-shift])
    out = ''.join(newlist)
    print(out)                

    #for the first 1 letter word being a
    shift = abs(0 - alpha.index(vv))
    print("assuming a the shift is: "+ str(shift))
    newlist = []
    for integer in range(0,len(text)):
        if text[integer] == ' ':
            newlist.append(" ")
            continue
        
        newlist.append(alpha[alpha.index(text[integer])-shift])
    out = ''.join(newlist)
    print(out)        
    
crack("wkh vwrub ri d yhub kxqjub fdwhusloodu")
