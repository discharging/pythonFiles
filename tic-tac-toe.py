def disp(v):
    for i in range(1,10,1):
        if(v[i]==i):
            print("_",end=" ")
        else:
            print(v[i],end=" ")
        if(i%3==0):
            print("\n")
v=[0,1,2,3,4,5,6,7,8,9]
print("Enter position between 1 to 9:")
disp(v)
for c in range(0,9,1):
    if(c%2==0):
        turn="x"
    else:
        turn="0"
    while(True):
        try:
            pos=int(input("play "+turn+":"))
            if(v[pos]!="x" and v[pos]!="0" and pos>0 and pos<10):
                v[pos]=turn;
                break
            print("This place is already occupied")
        except:
            print("Enter a valid input")
    disp(v)
    if(c>3):
        if(v[3]==v[5]==v[7] or v[1]==v[5]==v[9]):
            print("\nPlayer "+turn+" won");
            break
        for i in range(1,4,1):
            if(v[i]==v[i+3]==v[i+6]):
                print("\nPlayer "+turn+" won")
                exit()
        for i in range(1,8,3):
            if(v[i]==v[i+1]==v[i+2]):
                print("Player "+turn+" won")
                exit()
        if(c==8):
            print("Its a draw!")
