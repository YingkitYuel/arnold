import re

fp = open('1.txt', 'r')
train_iterations = []
train_loss = []

for ln in fp:
    #print(ln)
    if 'iter:' in ln and 'loss:' in ln:
        arr = re.findall(r'iter: \b\d+\b', ln)
        brr = re.findall(r'loss: \d+(\.\d+)?', ln)
        print(brr)
        train_iterations.append(int(arr[0][6:len(arr[0])]))
        train_loss.append(float(brr[0]))
print(train_iterations)
print(train_loss)
