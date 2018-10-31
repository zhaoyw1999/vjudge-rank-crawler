import get_contest_data, calculate_penalty, load_and_dump

def main():
    print('------ Welcome -----')
    vj_c_id = input('[contest id]: ')
    vj_u_nm = input('[ username ]: ')
    vj_pwd  = input('[ password ]: ')
    vj_grp  = int(input('[group type]: (PJ=1, TG=2, ALL=3) '))
    if vj_grp == 1:
        player = load_and_dump.load_user('普及组')
    elif vj_grp == 2:
        player = load_and_dump.load_user('提高组')
    else:
        player = load_and_dump.load_user()
    contest_data = get_contest_data.get_contest_data(vj_c_id, vj_u_nm, vj_pwd)
    tp = contest_data['participants']
    ts = contest_data['submissions']
    score_board, ac_board  = calculate_penalty.calculate_penalty(tp, ts)
    for x in player:
        if x[2] in score_board:
            x[3] = score_board[x[2]]
            x[4] = ac_board[x[2]]
        else:
            x[3] = 0
            x[4] = 0
    for x in range(0, len(player)):
        for y in range(x + 1, len(player)):
            if player[x][4] < player[y][4]:
                player[x], player[y] = player[y], player[x]
            if player[x][4] == player[y][4]:
                if player[x][3] > player[y][3]:
                    player[x], player[y] = player[y], player[x]
    flag = False
    flag_num = 0
    for i in range(0, len(player)):
        if not flag:
            player[i][5] = i + 1
            if player[i][4] == 0:
                flag = True
                flag_num = i + 1
        else:
            player[i][5] = flag_num
    for i in range(0, len(player)):
        for j in range(i + 1, len(player)):
            if int(player[i][0]) > int(player[j][0]):
                player[i], player[j] = player[j], player[i]
    print('Calculate rank successfully!')
    load_and_dump.dump_result(player, vj_c_id)
    print(vj_c_id + ': TXT and JSON file saved.')    

if __name__ == '__main__':
    main()