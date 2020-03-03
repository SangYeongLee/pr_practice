# 숫자의 글자수 세기
def cnt_digit(num):
    ret = 1
    while num//10!=0: 
        num = num//10
        ret+=1
    return ret

def solution(s):
    str_len = len(s)
    answer = str_len

    #반복 글자 단위 (1~문자열 길이의 절반)
    for l in range(1,str_len//2+1):
        cur=0
        i=0
        while True:
            if i+2*l > str_len: break

            # 길이가 l인 같은 문자열 개수 세기
            if s[i:i+l] == s[i+l:i+2*l]:
                cnt=1
                while s[i:i+l] == s[i+l:i+2*l]:
                    cnt+=1
                    i=i+l
                #(숫자)(문자열) 길이 add
                cur+=l+cnt_digit(cnt)
                i = i+l
            else:
                cur+=l
                i+=l
        #다 끝나고 남은 부분 더하기
        cur+=str_len-i

        #최소값 저장
        if answer>cur: answer = cur

    return answer

if __name__ == "__main__":
    test = "aaaaaaaaaaaaa"
    print(solution(test))