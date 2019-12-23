import collections
import hashlib
import hmac
import secrets
import sys

while True:
    h = sys.argv.__len__()
    if len(sys.argv) < 2:
        print("Please, enter a set of odd numbers")
        sys.exit()
    else:
        sys.argv.__delitem__(0)
        y = collections.Counter(sys.argv)
        if (h - 1) % 2 == 0:
            print("The number of elements must be odd")
            sys.exit()
        else:
            if [i for i in y if y[i] > 1]:
                print("Items in a set must not be repeated")
                sys.exit()
            else:
                if (h - 1) == 1:
                    print("Please, enter some elements, but not only one")
                    sys.exit()
                else: break
arr = sys.argv
h-=1
arr1 = [0] * (h+1)
i = h
arr.append('Exit')


while i > -1:
    i -= 1
    arr1[i] = i

for i in arr1:
        print(i +1 , '.',  arr[i])

computer = secrets.SystemRandom()
ind = computer.randint(0, (arr.__len__()-2))

a = secrets.token_hex(16)
print("Your HMAC: ", hmac.new(a.encode('utf-8'), arr[ind].encode('utf-8'), hashlib.sha256).hexdigest())

custom = input()
print("Your choice: ", arr[int(custom)-1])

if int(custom) == 0:
    exit()

print("The machine's choice: ", arr[ind])
k = ind+(h//2)

if ind == int(custom)-1:
    print("Dead heat")
else:
    if k > h:
      k=k-h
      if ind < int(custom)-1 <= k:
          print("Computer is winner")
      else:
          print("You are the winner")
    else:
        if ind < int(custom)-1 <= k:
           print("Computer is the winner")
        else:
            print("You are the winner")

print('If you want to check HMAC, you can use this key: ', a)
