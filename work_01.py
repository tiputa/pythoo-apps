import random

random_number = random.randint(1,100)
input_line = int(input("１〜１００までの数字を当ててください"))
for i in range(4):
    input_line = int(input("違う"))
    if input_line < random_number:
      print("もっと大きい")
    elif input_line == random_number:
      print("正解")
      break
    else:
      print("もっと小さい")

print("正解は" + {random_number})
