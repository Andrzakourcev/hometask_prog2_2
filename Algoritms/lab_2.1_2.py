d = int(input())
m = int(input())
n = int(input())
stops = list(map(int, input().split()))
stops = [0] + stops + [d]


def MinStations(m, stops):
    current_station, num_station = 0, 0
    while current_station < len(stops) - 1:
        last_station = current_station
        while current_station < len(stops) - 1 and stops[current_station + 1] - stops[last_station] <= m:  # Доедем ли?
            current_station += 1
        if current_station == last_station:
            return -1
        if current_station < len(stops) - 1:  # Дозаправка
            num_station += 1
    return num_station


print(MinStations(m, stops))
