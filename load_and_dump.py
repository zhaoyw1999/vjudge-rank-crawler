import json

def load_user(group_type='ALL'):
    with open('acmer.json', 'r') as f:
        data = json.load(f)
    f.close()
    ret = []
    if group_type == 'ALL':
        for x in data:
            ret.append([x['order_id'], x['student_name'], x['vjudge_id'], 0, 0, 0])
    else:
        for x in data:
            if x['group'] == group_type:
                ret.append([x['order_id'], x['student_name'], x['vjudge_id'], 0, 0, 0])
    print('Load user successfully!')
    return ret

def dump_result(player, contest_id):
    f = open(contest_id + '.txt', 'w')
    for x in player:
        f.write(x[0] + '\t' + x[1] + '\t' + str(x[3]) + '\t' + str(x[4]) + '\t' + str(x[5]) + '\n')
    f.close()
    res = [{} for i in range(0, len(player))]
    for i in range(0, len(player)):
        res[i]['order_id'] = player[i][0]
        res[i]['student_name'] = player[i][1]
        res[i]['vjudge_id'] = player[i][2]
        res[i]['penalty'] = player[i][3]
        res[i]['ac_num'] = player[i][4]
        res[i]['rank'] = player[i][5]
    f = open(contest_id + '.json', 'w')
    json.dump(res, f)
    f.close

