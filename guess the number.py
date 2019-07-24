from os import system
a = [0]*21
b = [0]*21

# a[0] = 1
system('cls')
for i in range(21):
    a[i] = str(i+1).zfill(2)
# print (a)

for i in range(7):
    print(str(a[i + (2*i)]) + "  " + str(a[(i)+1+(2*i)]) + "  " + str(a[(i)+2+(2*i)]))

def deckSuffle(option, arrayA, arrayB):
    if int(option) == 1:
        # for column first
        # print("first")
        for i in range(7):
            b[i] = a[(i)+1+(2*i)]
            # print(b[i])

        for i in range(7):
            b[i+7] = a[(i)+(2*i)]
            # print(b[i+7])

        for i in range(7):
            b[i+14] = a[(i)+2+(2*i)]
            # print(b[i+14])

    elif int(option) == 2:
        # print("Second")
        # for second first
        for i in range(7):
            b[i] = a[(i)+(2*i)]
            # print(i)

        for i in range(7):
            b[i+7] = a[(i)+1+(2*i)]

        for i in range(7):
            b[i+14] = a[(i)+2+(2*i)]

    elif int(option) == 3:
        # print("third")
        # for third first
        for i in range(7):
            b[i] = a[(i)+(2*i)]

        for i in range(7):
            b[i+7] = a[(i)+2+(2*i)]

        for i in range(7):
            b[i+14] = a[(i)+1+(2*i)]
    for i in range(21):
        a[i] = b[i]


for i in range (3):
    k = input("Enter coloum no.")
    system('cls')
    deckSuffle(k ,a ,b)
    # print("i:" + str(i))
    if i < 3:
        for i in range(7):
            print(str(b[i + (2*i)]) + "  " + str(b[(i)+1+(2*i)]) + "  " + str(b[(i)+2+(2*i)]))

system('cls')
print("Your no. is :"+ str(a[10]))
