d = {}
param = []
choose = ''
dlr = open('keymap.txt','r+')
dlr.write('{\n')
with open("mouse_log2.txt","r+") as f:
    for line in f:
        flr = line.split()
        d[flr[0]] = (int(flr[2]), int(flr[3]))
        
        for k in d:
            #print(k, d.get(k))
            choose = k
            param = list(d.get(k))
            dlr.write(f'{choose}: {param}\n')
            print(choose, param)

dlr.write('}\n')
f.close()
dlr.close()