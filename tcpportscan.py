from socket import *
import threading
import time

startTime = time.time()

def tcpscan(ip,start,end):
    
    for i in range(start, end):
        
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(0.2)

        conn = s.connect_ex((ip, i))
        if (conn == 0):
            print('Port %d: OPEN' % (i,))
        s.close()





def main():
    target = input('enter host:')
    startport = int(input('enter start port:'))
    endport = int(input('enter end port:'))

    targetip = gethostbyname(target)
    print("                ")    
    print('scanning host: ', targetip)

    tcpscan(targetip,startport,endport)

main()

