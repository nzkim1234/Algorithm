from math import ceil

def solution(fees, records):
    answer = []
    cars = {}

    for info in records:
        time, num, status = info.split()
        h, m = map(int,time.split(':'))
        time = h * 60 + m

        if not num in cars.keys():
            cars[num] = []
            
        cars[num].append(time)
    
    cars = sorted(cars.items(), key = lambda item: item[0])
    
    for i in cars:
        if len(i[1]) % 2 != 0:
            i[1].append(23 * 60 + 59)
    
        calc = 0
    
        for k in range(len(i[1]) - 1, -1, -2):
            calc += i[1][k] - i[1][k - 1]
            
        if calc <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + fees[3] * ceil((calc - fees[0]) / fees[2]))
        
    return answer


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
