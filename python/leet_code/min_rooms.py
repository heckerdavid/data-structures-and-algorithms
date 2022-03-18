# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.


def minimum_rooms(hours_list):
    hours_list.sort( key = lambda item: item[0] )
    rooms = 0

    while hours_list:
        current = hours_list[0]
        current_close = current[1]
        time_slots = []
        for i, class_time in enumerate(hours_list):
            if i == 0:
                time_slots.append(class_time)
            elif class_time[0] > current_close:
                current_close = class_time[1]
                time_slots.append(class_time)

        for time_slot in time_slots:
            hours_list.remove(time_slot)

        rooms +=1

    return rooms
