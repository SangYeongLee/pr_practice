from string import ascii_uppercase
def solution(msg):
    answer = []

    dic = dict()
    num = 1
    for i, alpa in enumerate(list(ascii_uppercase)):
        dic[alpa] = i+1

    s = msg[0]
    idx = 0
    while True:
        print("s : ", s)
        print("msg : ", msg)
        print(answer)
        if s in dic:
            if len(msg) > idx+1:
                if s+msg[idx+1] not in dic:
                    answer.append(dic[s])
                    while idx >= 1:
                        msg = msg[1:]
                        idx -= 1
                    print("Here : ", msg)
                    
                elif len(s)+idx+1 == len(msg):
                    print("ajweofijaweoifjaoiwejfowiejfo")
                    answer.append(dic[msg])
                    break
            if len(msg) <= idx + 1:
                idx = 0
                msg = msg[1:]
                s = msg[0]
            else:
                s += msg[idx + 1]
                idx += 1
        else:
            dic[s] = len(dic)+1
            idx = 0
            msg = msg[1:]
            s = msg[0]
        '''
        if len(msg) == 1:
            answer.append(dic[msg[0]])
            break
        '''

    for key, val in dic.items():
        if val == 86:
            print(key, val)
        if val == 63:
            print(key, val)
            
    print(answer)
    return answer

if __name__ == "__main__":
    msg = "KAKAO"
    solution(msg)
    