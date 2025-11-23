import random, sys, threading as th
from random import randrange as rr

l_st = []; lk = th.Lock()

def MillerRabin(n, k=40):
    if n==2 or n==3: return 1
    if n%2==0: return 0
    r, s = 0, n - 1
    while s % 2 == 0: r += 1; s //= 2
    for _ in range(k):
        a = rr(2, n - 1); x = pow(a, s, n)
        if x==1 or x==n-1: continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1: break
        else: return 0
    return 1

def getP(b):
    while 1:
        c = random.getrandbits(b)|(1<<b-1)|1
        if MillerRabin(c):
            with lk:
                if len(l_st)<2: l_st.append(c)
            break
        with lk:
            if len(l_st)>=2: break

def egcd(a, b):
    if a == 0: return (b, 0, 1)
    else: g, y, x = egcd(b % a, a); return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1: raise Exception('err')
    else: return x % m

def MakeKeys():
    ts = []; sz=2048; h=sz//2
    for _ in range(4): t=th.Thread(target=getP,args=(h,));t.start();ts.append(t)
    for t in ts: t.join()
    p,q = l_st[0],l_st[1]; n=p*q; phi=(p-1)*(q-1); e=65537
    g = egcd(e,phi)[0]
    while g!=1: e=rr(1,phi); g=egcd(e,phi)[0]
    d = modinv(e,phi); return ((e,n),(d,n))

def cRYPT(pk,txt):
    key,n=pk
    if sys.version_info[0]<3: m=int(txt.encode('hex'),16)
    else: m=int.from_bytes(txt.encode('utf-8'),'big')
    if m>=n: return None
    return pow(m,key,n)

def uN_cRYPT(prk, c):
    k,n=prk; p=pow(c,k,n)
    if sys.version_info[0]<3:
        h=hex(p)[2:].rstrip("L"); h='0'+h if len(h)%2 else h; return h.decode('hex')
    else: l=(p.bit_length()+7)//8; return p.to_bytes(l,'big').decode('utf-8')

# execution
try:
    txt = raw_input("please input the text to be encrypted: ") if sys.version_info[0]<3 else input("please input the text to be encrypted: ")
    PUB,PRIV = MakeKeys()
    print("Public Key: "+str(PUB))
    c_txt = cRYPT(PUB,txt)
    print("Encrypted: "+str(c_txt))
    d_txt = uN_cRYPT(PRIV,c_txt)
    print("Decrypted: "+d_txt)
except Exception as e: print("Err")