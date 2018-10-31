class record:
    def __init__(self, now_time, now_problem, now_status):
        self.now_time    = now_time
        self.now_problem = now_problem
        self.now_status  = now_status

def calculate_penalty(participants, submissions):
    personal_submit = {}
    score_board = {}
    ac_board = {}
    for i in participants:
        personal_submit[str(i)] = []
        score_board[str(i)]     = 0
    for x in submissions:
        person  = str(x[0])
        one_rec = record(int(x[3]), int(x[1]), int(x[2]))
        personal_submit[person].append(one_rec)
    for p in personal_submit:
        try_table = []
        ac = 0
        for i in range(0, 100):
            try_table.append(int(0))
        for rec in personal_submit[p]:
            if rec.now_time > 9000:
                continue
            if try_table[rec.now_problem] == 'AC':
                continue
            else:
                if rec.now_status == 1:
                    score_board[p] = score_board[p] + try_table[rec.now_problem] * 1200 + rec.now_time
                    try_table[rec.now_problem] = 'AC'
                    ac = ac + 1
                else:
                    try_table[rec.now_problem] = try_table[rec.now_problem] + 1
        ac_board[p] = ac
    for p in score_board:
        score_board[p] = score_board[p] // 60
    print('Generate score board successfully!')
    return score_board, ac_board
    
