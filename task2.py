

f = open("task02.csv")
data = f.read()
lineData = data.split("\n")

newList = []
for line in lineData:
    tempList = line.split(',')
    newList.append(tempList)



def find(A):
    global newList
    a = 0
    answer = False
    for i in newList:
        if A in i[0]:
            a = a+1
        if A == i[0]:
            print(i[1])
            answer = True
    if answer == False:
        if a != 0:
            print("There are "+str(a)+" stocks with that symbol")
        else :
            print("No matches")

def main():
    while True:
        x = input("Enter Stock Symbol, put 0000 to exit: ")
        if x != "0000":
            find(x)
        elif x =="0000":
            break


main()
