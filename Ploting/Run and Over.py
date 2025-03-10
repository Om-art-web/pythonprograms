import matplotlib.pyplot as plt

overs=[]
runs=[]
scores=[]
totalovers=5
currentover=1
while True:
    print("0-Exit, 1-Enter score, 2-View Chart, 3-Increase Chart")
    option=int(input(" Read option: "))
    
    if option==0:
        break
    if option==1:
        print("Enter Score For Over No",currentover)
        run=int(input())
        overs.append(currentover)
        if currentover>totalovers:
            print("Error")
        if currentover==1:
            scores.append(run)
        else:
            scores.append(run+scores[-1])
        currentover=currentover+1
        runs.append(run)
    if option==2:

        plt.plot(overs,runs)
        plt.scatter(overs,runs)
        plt.show()

    if option==3:

        plt.plot(overs,runs)
        plt.scatter(overs,runs)
        plt.show()
    
    print(overs,runs,scores)