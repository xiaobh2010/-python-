def save_file(all_info):
    f=open('si.txt','w')
    for i in all_info:
        f.write('|%s|%s|%s|\n' % (i['name'].center(20),str(i['age']).center(6),str(i['score']).center(6)))
    f.close()

def read_file():
    f=open('si.txt','r')
    while True:
        s=f.readline()
        if s=='':
            break
        print(s)
    f.close()
