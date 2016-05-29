import socket,l
#http://patorjk.com/software/taag/#p=display&h=0&v=0&f=Ivrit&t=a%0Ab%0Ac%0Ad%0Ae%0Af%0Ag%0Ah%0Ai%0Aj%0Ak%0Al%0Am%0An%0Ao%0Ap%0Aq%0Ar%0As%0At%0Au%0Av%0Aw%0Ax%0Ay%0Az%0A0%0A1%0A2%0A3%0A4%0A5%0A6%0A7%0A8%0A9%0AA%0AB%0AC%0AD%0AE%0AF%0AG%0AH%0AI%0AJ%0AK%0AL%0AM%0AN%0AO%0AP%0AQ%0AR%0AS%0AT%0AU%0AV%0AW%0AX%0AY%0AZ%0A

m = [
"""  __ _
 / _` |
| (_| |
 \__,_|""".replace(' ','').replace('\n',''),

""" _
| |__
| '_ \\
| |_) |
|_.__/ """.replace(' ','').replace('\n',''),


"""  ___
 / __|
| (__
 \___|""".replace(' ','').replace('\n',''),

"""     _
  __| |
 / _` |
| (_| |
 \__,_|""".replace(' ','').replace('\n',''),


"""  ___
 / _ \\
|  __/
 \___|""".replace(' ','').replace('\n',''),

"""  __
 / _|
| |_
|  _|
|_|  """.replace(' ','').replace('\n',''),


"""  __ _
 / _` |
| (_| |
 \__, |
 |___/ """.replace(' ','').replace('\n',''),

""" _
| |__
| '_ \\
| | | |
|_| |_|""".replace(' ','').replace('\n',''),

""" _
(_)
| |
| |
|_|""".replace(' ','').replace('\n',''),

"""   _
  (_)
  | |
  | |
 _/ |
|__/ """.replace(' ','').replace('\n',''),

""" _
| | __
| |/ /
|   <
|_|\_\\""".replace(' ','').replace('\n',''),

""" _
| |
| |
| |
|_|""".replace(' ','').replace('\n',''),


""" _ __ ___
| '_ ` _ \\
| | | | | |
|_| |_| |_|""".replace(' ','').replace('\n',''),


""" _ __
| '_ \\
| | | |
|_| |_|""".replace(' ','').replace('\n',''),


"""  ___
 / _ \\
| (_) |
 \___/ """.replace(' ','').replace('\n',''),


""" _ __
| '_ \\
| |_) |
| .__/
|_|    """.replace(' ','').replace('\n',''),

"""  __ _
 / _` |
| (_| |
 \__, |
    |_|""".replace(' ','').replace('\n',''),

""" _ __
| '__|
| |
|_|   """.replace(' ','').replace('\n',''),


""" ___
/ __|
\__ \\
|___/""".replace(' ','').replace('\n',''),

""" _
| |_
| __|
| |_
 \__|""".replace(' ','').replace('\n',''),


""" _   _
| | | |
| |_| |
 \__,_|""".replace(' ','').replace('\n',''),


"""__   __
\ \ / /
 \ V /
  \_/  """.replace(' ','').replace('\n',''),


"""__      __
\ \ /\ / /
 \ V  V /
  \_/\_/  """.replace(' ','').replace('\n',''),


"""__  __
\ \/ /
 >  <
/_/\_\\""".replace(' ','').replace('\n',''),


""" _   _
| | | |
| |_| |
 \__, |
 |___/ """.replace(' ','').replace('\n',''),

""" ____
|_  /
 / /
/___|""".replace(' ','').replace('\n',''),

#25

"""  ___
 / _ \\
| | | |
| |_| |
 \___/ """.replace(' ','').replace('\n',''),

""" _
/ |
| |
| |
|_|""".replace(' ','').replace('\n',''),

""" ____
|___ \\
  __) |
 / __/
|_____|""".replace(' ','').replace('\n',''),

""" _____
|___ /
  |_ \\
 ___) |
|____/ """.replace(' ','').replace('\n',''),

""" _  _
| || |
| || |_
|__   _|
   |_|  """.replace(' ','').replace('\n',''),

""" ____
| ___|
|___ \\
 ___) |
|____/ """.replace(' ','').replace('\n',''),

"""  __
 / /_
| '_ \\
| (_) |
 \___/ """.replace(' ','').replace('\n',''),

""" _____
|___  |
   / /
  / /
 /_/   """.replace(' ','').replace('\n',''),

"""  ___
 ( _ )
 / _ \\
| (_) |
 \___/ """.replace(' ','').replace('\n',''),

"""  ___
 / _ \\
| (_) |
 \__, |
   /_/ """.replace(' ','').replace('\n',''),

"""    _
   / \\
  / _ \\
 / ___ \\
/_/   \_\\""".replace(' ','').replace('\n',''),

""" ____
| __ )
|  _ \\
| |_) |
|____/ """.replace(' ','').replace('\n',''),

"""  ____
 / ___|
| |
| |___
 \____|""".replace(' ','').replace('\n',''),

""" ____
|  _ \\
| | | |
| |_| |
|____/ """.replace(' ','').replace('\n',''),

""" _____
| ____|
|  _|
| |___
|_____|""".replace(' ','').replace('\n',''),

""" _____
|  ___|
| |_
|  _|
|_|    """.replace(' ','').replace('\n',''),

"""  ____
 / ___|
| |  _
| |_| |
 \____|""".replace(' ','').replace('\n',''),

""" _   _
| | | |
| |_| |
|  _  |
|_| |_|""".replace(' ','').replace('\n',''),

""" ___
|_ _|
 | |
 | |
|___|""".replace(' ','').replace('\n',''),

"""     _
    | |
 _  | |
| |_| |
 \___/ """.replace(' ','').replace('\n',''),

""" _  __
| |/ /
| ' /
| . \\
|_|\_\\""".replace(' ','').replace('\n',''),

""" _
| |
| |
| |___
|_____|""".replace(' ','').replace('\n',''),

""" __  __
|  \/  |
| |\/| |
| |  | |
|_|  |_|""".replace(' ','').replace('\n',''),

""" _   _
| \ | |
|  \| |
| |\  |
|_| \_|""".replace(' ','').replace('\n',''),

"""  ___
 / _ \\
| | | |
| |_| |
 \___/ """.replace(' ','').replace('\n',''),

""" ____
|  _ \\
| |_) |
|  __/
|_|    """.replace(' ','').replace('\n',''),

"""  ___
 / _ \\
| | | |
| |_| |
 \__\_\\""".replace(' ','').replace('\n',''),

""" ____
|  _ \\
| |_) |
|  _ <
|_| \_\\""".replace(' ','').replace('\n',''),

""" ____
/ ___|
\___ \\
 ___) |
|____/ """.replace(' ','').replace('\n',''),

""" _____
|_   _|
  | |
  | |
  |_|  """.replace(' ','').replace('\n',''),

""" _   _
| | | |
| | | |
| |_| |
 \___/ """.replace(' ','').replace('\n',''),

"""__     __
\ \   / /
 \ \ / /
  \ V /
   \_/   """.replace(' ','').replace('\n',''),

"""__        __
\ \      / /
 \ \ /\ / /
  \ V  V /
   \_/\_/   """.replace(' ','').replace('\n',''),

"""__  __
\ \/ /
 \  /
 /  \\
/_/\_\\""".replace(' ','').replace('\n',''),

"""__   __
\ \ / /
 \ V /
  | |
  |_|  """.replace(' ','').replace('\n',''),

""" _____
|__  /
  / /
 / /_
/____|""".replace(' ','').replace('\n','')

]


sock = socket.socket()
sock.connect(('p.tjctf.org', 8008))
success=0
while not success:
    data = str(sock.recv(1024)).replace('\\n','\n').replace('\\\\','\\')
    print(data)
    print(1)
    n = data.split('\n')
    #yznaem nomer cled str c 'continue'
    cont = 0
    for x in n:
        cont+=1
        if 'continue' in x:break

    #yznaem nomer str c "   "
    pysto = len(n)-3

    #[cont,pysto]

    le = len(n[cont])
    promegytki = [0]
    for x in range(1,le):
            z = cont
            s = 1
            while z<=pysto:
                if n[z][x]!=' ':s = 0
                z+=1
            if s==1: promegytki.append(x)

    promegytki.append(le)
    print(promegytki)
    k = len(promegytki)

    i = 1
    ans = ''
    while i<len(promegytki):
        z = cont
        cross=''
        while z<=pysto:
            cross+=n[z][promegytki[i-1]+1:promegytki[i]]
            z+=1
        cross = cross.replace(' ','').replace('\n','')
        w = m.index(cross)
        if w>=0 and w<=25:
            ans+=chr(97+w)
        elif w>=26 and w<=35:
            ans+=chr(48+w-26)
        else:
            ans+=chr(65+w-36)
        i+=1
    print(ans)
    sock.send(ans.encode('utf-8')+b'\n')