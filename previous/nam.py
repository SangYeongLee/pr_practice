def timeToInt(stime):
    h = int(stime.split(":")[0])
    m = int(stime.split(":")[1])
    return h * 60 + m

def intToTime(time):
    return str(time // 60).zfill(2) + ":" + str(time % 60).zfill(2)

def isLastBus(bus, btime):
    return btime[-1] == bus

def solution(n, t, m, timeTable):
    answer = ''
    baseTime = 540

    btime = []
    time = []
    for tt in timeTable:
        time.append(timeToInt(tt))
    time.sort()
    
    secondLate = time[-1] - 1

    for i in range(n):
        btime.append(baseTime + i * t)
        
    for bus in btime:
        on = 0
        for idx, crew in enumerate(time):
            if crew <= bus:
                on += 1
            else:
                break
            if on == m:
                break

        lastcrew = time[on - 1]
        for i in range(on - 1, -1, -1):
            time.pop(i)
            
        if isLastBus(bus, btime):
            if on == m:
                answer = intToTime(lastcrew - 1)
            else:
                answer = intToTime(bus)
                
    return answer