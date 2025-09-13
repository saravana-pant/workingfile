def format(n):
    binary=[]
    num=''
    for i in range(1,n+1):
        rem=0
        while(i>0):
            rem=i%2
            num=str(rem)+num
            i//=2
        binary.append(num)
        num=''
    ocatal=[]
    num=''
    for i in range(1,n+1):
        rem=0
        while(i>0):
            rem=i%8
            num=str(rem)+num
            i//=8
        ocatal.append(num)
        num=''
    hex=[]
    num=''
    c=0
    for i in range(1,n+1):
        rem=0
        if i>9 and i<=15:
            vari='ABCDEF'
            hex.append(vari[c])
            c+=1
        else:
            while(i>0):
                rem=i%16
                num=str(rem)+num
                i//=16
            hex.append(num)
            num=''
    size=int(len(binary[-1]))
    print(size)
    size+=1
    for i in range(n):
        print(str(i+1).rjust(size-1)+str(ocatal[i]).rjust(size)+str(hex[i]).rjust(size)+str(binary[i]).rjust(size))
        
format(17)
