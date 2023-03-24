seqLength=int(input())
seq=list(map(int,input().split(" ")))
favLength=int(input())
favSeq=list(map(int,input().split(" ")))



def lisToStr(s):
    s1=" "
    for i in s:
        s1+=str(i)
    return s1


seqStr=(lisToStr(seq)).replace(" ","")
favStr=(lisToStr(favSeq)).replace(" ","")


if favStr in seqStr:
    print("Yes")
else:
    print("No")