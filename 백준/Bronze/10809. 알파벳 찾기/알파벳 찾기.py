sentence = input()
key = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
answer = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
for char in sentence:
    if answer[key.index(char)] == -1:
        answer[key.index(char)] = sentence.index(char)
for num in answer:
    print(num,end =" ")