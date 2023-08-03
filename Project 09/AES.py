import time
def ADDROUNDKEY(p,k):
    ARK = []  
    for i in range(4):
        x = p[i]
        y = k[i]
        z = eval("0b"+x) ^ eval("0b"+y)
        xor = format(z,'b').zfill(32)
        ARK.append(xor)
    return ARK
def ShiftRows(plaintext):
    ShiftROW_chart = [1, 6, 11, 16,
                      5, 10, 15, 4,
                      9, 14, 3, 8,
                      13, 2, 7, 12]
    temp = [i for i in range(16)]
    for i in range(len(ShiftROW_chart)):
        temp[i] = plaintext[ShiftROW_chart[i] - 1]
    return temp
def SubBytes(plaintext):
    Subchart = [0x63,0x7c,0x77,0x7b,0xf2,0x6b,0x6f,0xc5,0x30,0x01,0x67,0x2b,0xfe,0xd7,0xab,0x76,
		        0xca,0x82,0xc9,0x7d,0xfa,0x59,0x47,0xf0,0xad,0xd4,0xa2,0xaf,0x9c,0xa4,0x72,0xc0,
		        0xb7,0xfd,0x93,0x26,0x36,0x3f,0xf7,0xcc,0x34,0xa5,0xe5,0xf1,0x71,0xd8,0x31,0x15,
		        0x04,0xc7,0x23,0xc3,0x18,0x96,0x05,0x9a,0x07,0x12,0x80,0xe2,0xeb,0x27,0xb2,0x75,
		        0x09,0x83,0x2c,0x1a,0x1b,0x6e,0x5a,0xa0,0x52,0x3b,0xd6,0xb3,0x29,0xe3,0x2f,0x84,
		        0x53,0xd1,0x00,0xed,0x20,0xfc,0xb1,0x5b,0x6a,0xcb,0xbe,0x39,0x4a,0x4c,0x58,0xcf,
		        0xd0,0xef,0xaa,0xfb,0x43,0x4d,0x33,0x85,0x45,0xf9,0x02,0x7f,0x50,0x3c,0x9f,0xa8,
		        0x51,0xa3,0x40,0x8f,0x92,0x9d,0x38,0xf5,0xbc,0xb6,0xda,0x21,0x10,0xff,0xf3,0xd2,
		        0xcd,0x0c,0x13,0xec,0x5f,0x97,0x44,0x17,0xc4,0xa7,0x7e,0x3d,0x64,0x5d,0x19,0x73,
		        0x60,0x81,0x4f,0xdc,0x22,0x2a,0x90,0x88,0x46,0xee,0xb8,0x14,0xde,0x5e,0x0b,0xdb,
		        0xe0,0x32,0x3a,0x0a,0x49,0x06,0x24,0x5c,0xc2,0xd3,0xac,0x62,0x91,0x95,0xe4,0x79,
		        0xe7,0xc8,0x37,0x6d,0x8d,0xd5,0x4e,0xa9,0x6c,0x56,0xf4,0xea,0x65,0x7a,0xae,0x08,
		        0xba,0x78,0x25,0x2e,0x1c,0xa6,0xb4,0xc6,0xe8,0xdd,0x74,0x1f,0x4b,0xbd,0x8b,0x8a,
		        0x70,0x3e,0xb5,0x66,0x48,0x03,0xf6,0x0e,0x61,0x35,0x57,0xb9,0x86,0xc1,0x1d,0x9e,
		        0xe1,0xf8,0x98,0x11,0x69,0xd9,0x8e,0x94,0x9b,0x1e,0x87,0xe9,0xce,0x55,0x28,0xdf,
		        0x8c,0xa1,0x89,0x0d,0xbf,0xe6,0x42,0x68,0x41,0x99,0x2d,0x0f,0xb0,0x54,0xbb,0x16]
    temp = []
    for i in plaintext:
        temp.append(bin(int("0x" + i,16))[2:].zfill(8))
    table = []
    for i in temp:
        x = int(eval("0b" + i[:4]))
        y = int(eval("0b" + i[4:]))
        table.append(format(int(Subchart[x*16+y]),'x').zfill(2).upper())
    return table
def MixColumns(sfr):
    def GF256(x, y):  
        def leftround(x):
            return x[1:8] + "0"
        x = x.replace(" ", "")
        y = y.replace(" ", "")
        x = bin(int("0x" + x, 16))[2:].zfill(8)
        y = bin(int("0x" + y, 16))[2:].zfill(8)
        if x.count("1") >= y.count("1"):  
            num = y
            text = x
            temp = x
        else:
            num = x
            text = y
            temp = y
        px = 0b00011011  
        num = list(num)
        num.reverse()  
        num = "".join(num)
        word = []
        for i in range(len(text)):
            if text[0] == "0":
                text = leftround(text)
                word.append(text)
            elif text[0] == "1":
                text = leftround(text)
                xor = px ^ eval("0b" + text)
                text = format(xor, 'b').zfill(8)
                word.append(text)
        n = 0b00000000
        for index, value in enumerate(list(num)):
            if value == "1" and index == 0:  
                n ^= eval("0b" + temp)
            elif value == "1" and index > 0:
                n ^= eval("0b" + word[index - 1])
        n = format(n, 'b').zfill(8)
        return hex(int("0b" + n, 2))[2:].upper().zfill(2)
    def xor(word):
        key = []
        for i in word:
            key.append(bin(int("0x" + i, 16))[2:].zfill(8))
        n = 0
        for i in range(len(key)):
            n += int(key[i])
        n = str(n).zfill(8)
        xor = []
        for i in range(len(n)):
            z = int(n[i]) % 2
            xor.append(str(z))
        return hex(int("0b" + "".join(xor), 2))[2:].upper().zfill(2)
    def exchange(s):
        return [s[0],s[4],s[8],s[12],
                s[1],s[5],s[9],s[13],
                s[2],s[6],s[10],s[14],
                s[3],s[7],s[11],s[15]]
    Mc_chart = [["02","03","01","01"],
                ["01","02","03","01"],
                ["01","01","02","03"],
                ["03","01","01","02"]]
    gf256 = []
    for round in range(4):
        for row in range(4):
            for col in range(4):
                temp = GF256(Mc_chart[round][col],sfr[col+row*4])
                gf256.append(temp)
    temp = []
    for i in range(0,len(gf256),4):
        temp.append(gf256[i:i+4])
    result = []
    for i in temp:
        a = xor(i)
        result.append(a)
    b = exchange(result)
    new_chart=[]
    for v in range(0, len("".join(b)), 8):  
        new_chart.append(bin(int("0x" + "".join(b)[v:v + 8], 16))[2:].zfill(32))
    return new_chart
 
plaintext = "32 43 f6 a8 88 5a 30 8d 31 31 98 a2 e0 37 07 34".replace(" ","")
key = "2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c".replace(" ","")
p = []
k = []

start=time.time()
for i in range(0,len(plaintext),8):
    p.append(bin(int("0x" + plaintext[i:i+8],16))[2:].zfill(32))
for i in range(0,len(key),8):
    k.append(bin(int("0x" + key[i:i+8],16))[2:].zfill(32))
def rotwords(s):
    return s[2:4] + s[4:6] + s[6:8] + s[0:2]
chart = ["01000000","02000000","04000000","08000000","10000000",
         "20000000","40000000","80000000","1b000000","36000000"]
word = [[],[],[],[]]
n = 0
for i in range(0,len(key),8):
    word[n].append(key[i:i+8])
    n+=1
for i in range(4,44):
    word.append([])
    if i%4==0:
        subword = []
        a=rotwords(word[i-1][0])
        a=list(a)
        for n in range(0,len(a),2):
            subword.append(a[n]+a[n+1])
        b="".join(SubBytes(subword))
        c=eval("0x"+b)^eval("0x"+chart[int(i/4-1)])^eval("0x"+word[i-4][0])
        word[i].append(format(c,'x').zfill(8))
    else:
        d=eval("0x"+word[i-1][0]) ^ eval("0x"+word[i-4][0])
        word[i].append(format(d,'x').zfill(8))
newkey=[]
w=0
for num in range(4,44,4):
    newkey.append([])
    newkey[w].append(format(eval("0x"+word[num][0]),'b').zfill(32))
    newkey[w].append(format(eval("0x"+word[num+1][0]),'b').zfill(32))
    newkey[w].append(format(eval("0x"+word[num+2][0]),'b').zfill(32))
    newkey[w].append(format(eval("0x"+word[num+3][0]),'b').zfill(32))
    w+=1
temp = hex(int("0b"+"".join(ADDROUNDKEY(p,k)),2))[2:]
ark = []
for i in range(0,len(temp),2):
    ark.append(temp[i:i+2])

for i in range(10):
    if i <=8:
        sub = SubBytes(ark)
        sfr = ShiftRows(sub)
        mixcol = MixColumns(sfr)
        temp = hex(int("0b" + "".join(ADDROUNDKEY(mixcol,newkey[i])), 2))[2:]
        ark = []  
        for i in range(0, len(temp), 2):
            ark.append(temp[i:i + 2])
    else:
        sub = SubBytes(ark)
        sfr = ShiftRows(sub)
 
sfr=''.join(sfr)
last = []
for i in range(0,len(sfr),8):
    last.append(bin(int("0x"+sfr[i:i+8],16))[2:].zfill(32))
result = ADDROUNDKEY(last,newkey[9])
result = format(eval('0b'+''.join(result)),'x').upper()
outcome = []
for i in range(0,len(result),2):
    outcome.append(result[i:i+2])
end=time.time()

print(f"待加密消息为：{''.join(plaintext)}")    
print(f"AES加密结果为：{''.join(outcome)}")
print("共消耗",end-start,"秒")
