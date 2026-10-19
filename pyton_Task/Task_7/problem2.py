# Problem: The Captain's Room

k = int(input())
rooms = list(map(int, input().split()))

room_set = set(rooms)

for room in room_set:
    if rooms.count(room) == 1:
        print(room)
        break
