# print("Hello world")
def main():
    #print("Hello world")
    result = print(" ".join([str(i * 2) for i in range(1, 16, 3) if i % 2 == 0]))
    print(result)
#words = ["aye", "bee", "sea", "bee"]
#words.remove("bee")
#print(words.pop())

main()