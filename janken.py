import random

# handsというリストに、じゃんけんの手を覚（おぼ）えておいてもらう
hands=['グー','チョキ','パー']

# どの数字が、どの手を表（あらわ）しているのかを表示（ひょうじ）する
print('0:グー 1:チョキ 2:パー')

# プレイヤーからの入力をinput_strに覚えておいてもらう
input_str=input('ここに番号を入力してね！>>>')

# 入力されたものは文字列（もじれつ）になっているので、数値（すうち）に変換（へんかん）したものを、hand_numに覚えておいてもらう
hand_num=int(input_str)

# ランダムにコンピュータの手の数字を決めて、computer_hand_numに覚えておいてもらう
computer_hand_num=random.randrange(3)

# ランダムで作った数字から、コンピュータがどの手なのかを出して、computer_handに覚えておいてもらう
computer_hand=hands[computer_hand_num]

# 入力された数字から、どの手なのかを出して、player_handに覚えておいてもらう
player_hand=hands[hand_num]

# player_handに覚えておいてもらった手を表示する
print('あなたは'+player_hand+'を出しました')

# computer_handに覚えておいてもらった手を表示する
print('コンピュータは'+computer_hand+'を出しました')

###########################################
# # 勝（か）ったか負（ま）けたかを判断（はんだん）する
# プレイヤーの手と、コンピュータの手が、同じとき（あいこのとき）
if hand_num==computer_hand_num:
# 「あいこだね」と表示する
  print('あいこだね')
  #あいこじゃない時
else:
  # プレイヤーがグーのとき
  if hand_num==0:
    # コンピュータがチョキのとき
    if computer_hand_num==1:
      # 「あなたの勝ち」と表示する
      print('あなたの勝ち') 
    # コンピュータがパーのとき
    if computer_hand_num==2:
      # 「あなたの負け」と表示する
      print('あなたの負け')
  # プレイヤーがチョキのとき
  elif hand_num==1:
    # コンピュータがパーのとき
    if computer_hand_num==2:
      # 「あなたの勝ち」と表示する
     print('あなたの勝ち')
    # コンピュータがグーのとき
    if computer_hand_num==0:
      # 「あなたの負け」と表示する
      print('あなたの負け')
  # プレイヤーがパーのとき
  elif hand_num==2:
      # コンピュータがグーのとき
      if computer_hand_num==0:
        # 「あなたの勝ち」と表示する
        print('あなたの勝ち')
      # コンピュータがチョキのとき
      if computer_hand_num==1:
        # 「あなたの負け」と表示する
        print('あなたの負け')





      