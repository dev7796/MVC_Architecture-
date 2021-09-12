ls = []
main_string = input("Enter the string")


def reverseWordSentence(main_string):
    words = main_string.split(" ")
    for i in words:
        newWords = i[::-1]
        newSentence = "".join(newWords)
        print(newSentence, end=" ")
print(" ")

reverseWordSentence(main_string)


def oddswap(main_string):
    p = main_string.split(" ")
    print("this is two character output")
    for i in p:

        for j in range(0, len(i), 2):
        # in i+2 it takes till i+1

            print(i[j:j + 2][::-1], end="")
        print(end=" ")


oddswap(main_string)
