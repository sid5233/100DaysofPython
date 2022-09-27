for i in range (1,100):
    if i%2 == 0:
        print("Tic")
    elif i%3 == 0:
        print("Tac")
    elif i%2 ==0 & i%3 == 0 :
        print("TicTac")
    else:
        print(i)