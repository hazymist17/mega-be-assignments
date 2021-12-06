import math

wordList =[]
target=[]

#Number_of_wordLists
user_input=int(input("Number_of_wordLists = "))
#Input Wordlists
for index in range(user_input):
    wordList.append(input(str(index+1)+".word is "))
#Input Target
Target_data=input("target = ")
for r in range(math.ceil(len(Target_data)/2)):
    target.append(Target_data[0+(r*2):2+(r*2)])

print("wordList =", wordList)
print("target =", target)
#Solve
def solve(wordList, target):
    output=[]
    for n1 in range(len(wordList)):
        for n2 in range(len(target)):
            if wordList[n1]==target[n2]:
                output.append(target[n2])
                wordList[n1]=wordList[n1]+"0"
        if len(output)==2:    
              break  
    if len(output)!= math.ceil(len(Target_data)/2):
        output="none"
        print("output =", output)
    else:
        #output = (“output[0]”, “output[1]”) or (“output[1]”, “output[0]”)
        output='(“'+output[0]+'”, “'+output[1]+'”) or (“'+output[1]+'”, “'+output[0]+'”)'
        print("output =", output)

solve(wordList, target)
        




