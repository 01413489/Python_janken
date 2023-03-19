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
# あいこのときは0、プレイヤーが負けたときは-1か2、プレイヤーが勝ったときは-2か1という数字を、変数win_or_loseに覚えておいてもらう
win_or_loss=computer_hand_num-hand_num

# じゃんけんの勝ち負けを表示する
if win_or_loss==0:
    print('あいこだね')
elif win_or_loss==-1 or win_or_loss==2:
    print('あなたの負け')
elif win_or_loss==-2 or win_or_loss==1:
    print('あなたの勝ち')