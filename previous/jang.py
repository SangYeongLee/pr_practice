def solution(cacheSize, cities) :
    buffer = [0] * cacheSize
    cache = []
    time = 0
    answer = 0
    for i in cities :
        i = i.lower()
        if i in cache :
            idx = cache.index(i)
            buffer[idx] = time
            answer += 1
        else :
            if len(cache) < cacheSize :
                cache.append(i)
                buffer[cache.index(i)] = time
            elif buffer :
                LRUidx = buffer.index(min(buffer))
                cache[LRUidx] = i
                buffer[LRUidx] = time
            answer += 5
        time += 1
    return answer