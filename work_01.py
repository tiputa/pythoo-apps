import random

while True:
   
   num = random.randint(1,100)
   print(num)

   result = False

   for i in range(5):
      
      input_line = int(input("数字を入力してください:"))

      if input_line == num:
         print("正解")
         break
      else:
         print("不正解")
         if input_line < num:
           print("もっと大きいです")
         else:
           print("もっと小さいです")
   if result:
    print("ゲームに勝ちました")
   else:
    print(f"ゲームに負けました。正解は{num}でした。")
   ans = input("もう一度やりますか？(YES/NO):")
   if ans != "YES":