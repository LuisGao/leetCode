def firstUniqChar(s):
    lenth = len(s)
    temp = {}
    temp1 = {}
    for i in range(lenth):
        ts = s[i]
        if ts not in temp.keys():
            temp[ts] = 1
        else:
            temp[ts] = 2
    po = 0
    for it in s():
        if temp[it] == 1:
            return temp1[it]
        po += 1
    return -1


def abc(s, t):
    lt = []
    for l in s:
        lt.append(l)
    for l in t:
        if l in lt:
            lt.remove(l)
        else:
            return False
    return len(lt) == 0


def ifCir(str):
    pl = 0
    ph = len(str)- 1
    str = str.lower()
    punc = [',','.',' ']
    while pl < ph:
        if str[pl] in punc:
            pl += 1
            continue
        elif str[ph] in punc:
                ph -= 1
                continue
        if str[pl] == str[ph]:
            pl += 1
            ph -= 1
            continue
        else:
            return False
    return True

def newStr(str1):
    restr = ''
    lenth = len(str1)
    count = 1
    for i in range(lenth):
        if count == 0:
            restr += '11'
        elif i < lenth - 1 and str1[i + 1] == str1[i]:
            count += 1
        else:
            restr += str(count)
            restr += str1[i]
            count = 1
    return restr

def strStr( haystack, needle):
    if needle == '':
        return 0
    elif haystack == '':
        return -1
    a = haystack.split(needle)
    if len(a) > 0:
        return len(a[0])
    else:
        return -1

def getBs(strs):
    slen = len(strs)
    count = 0
    if slen > 0:
        ml = len(strs[0])
        while count < ml:
            ts = strs[0][count]
            for s in strs:
                if count >= len(s):
                    return strs[0][:count]
                if s[count] != ts:
                    return strs[0][:count]
            count += 1
        return strs[0][:count]
    else:
        return ''

print(getBs(['abde','abde','abd']))