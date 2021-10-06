ジャンケン

def generate_enemy_hands():

    while True:

        yield '1'

        yield '2'

        yield '3'

hands_dict={

      '1':'グー',

      '2':'チョキ',

      '3':'パー',

}

def is_win(my_hands,enemy_hands):

　if my_hands==1 and enemy_hands==2:

  　return True

　elif my_hands==2 and enemy_hands==3:

  　return True

　elif my_hands==3 and enemy_hands==1:

  　return True

enemy_hands=generate_enemy_hands()

while True:

　my_hands=input('出したい手を入力してください　1,グー 2,チョキ 3,パー')

　if my_hands not in (1,2,3):

  　print('間違った入力')

  　continue

　enemy_hands=next(enemy_hands)

　print('自分の出した手は{},空いての出した手は   　{}.format(hands_dict.get(my_hands),hands_dict.get(enemy_hands)))

　if my_hands==enemy_hands:

  　print('あいこ')

　elif is_win(my_hands,enemy_hands):

  　print('あなたは勝ちました')

else:

　　print('あなたは負けです')

　　break