from itertools import count


def minMovesToSeat(seats, students):
    count = 0
    seats.sort()
    students.sort()
    for i in range(len(seats)):
        if seats[i] != students[i]:
            count += abs(seats[i] - students[i])
        
    return count
        



print(minMovesToSeat(seats = [4,1,5,9], students = [1,3,2,6]))