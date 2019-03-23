def score_high2low(all_info):
    res=sorted(all_info,key=lambda all_info:all_info['score'],reverse=True)
    print('按成绩从高至低打印学生信息:')
    for n in res:
        print('|%s|%s|%s|' % (n['name'].center(20),str(n['age']).center(6),str(n['score']).center(6)))

def score_low2high(all_info):
    res=sorted(all_info,key=lambda all_info:all_info['score'])
    print('按成绩从低至高打印学生信息:')
    for n in res:
        print('|%s|%s|%s|' % (n['name'].center(20),str(n['age']).center(6),str(n['score']).center(6)))

def age_high2low(all_info):
    res=sorted(all_info,key=lambda all_info:all_info['age'],reverse=True)
    print('按年龄从高至低打印学生信息:')
    for n in res:
        print('|%s|%s|%s|' % (n['name'].center(20),str(n['age']).center(6),str(n['score']).center(6)))

def age_low2high(all_info):
    res=sorted(all_info,key=lambda all_info:all_info['age'])
    print('按年龄从低至高打印学生信息:')
    for n in res:
        print('|%s|%s|%s|' % (n['name'].center(20),str(n['age']).center(6),str(n['score']).center(6)))
