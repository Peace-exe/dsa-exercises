#lc 56- merge intervals

def merge(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []
    merged = []
    intervals.sort(key = lambda interval: interval[0])

    for i in intervals:
        if(not merged or merged[-1][1]<i[0]):
            merged.append(i)
        else:
            merged[-1]=[merged[-1][0], max(merged[-1][1], i[1])]
    
    return merged
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))            


