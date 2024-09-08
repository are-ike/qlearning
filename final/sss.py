
# Data abstraction in programming is a concept that involves hiding 
# the complex implementation details of data structures 
# and providing a simplified interface to interact with the data.
# def three ():
#     res = []
#     i = 0
    
#     while i < 5:
#         try:
#             val = float(input(f"Enter float {i + 1} "))
#             res.append(val)
#             i = i + 1

#         except ValueError:
#             print("Enter floar jare")

#     print(res) 
    
# three()


# import calendar

# cal = calendar.TextCalendar(calendar.SUNDAY)

# month_cal = cal.formatmonth(2024, 7)

# print(month_cal)


import array

def getstuff (arr2):
    arr = array.array('i', arr2)

    address = arr.buffer_info()[0]

    length = arr.buffer_info()[1]

    element_size = arr.itemsize

    buffersize = length * element_size

    print(address, buffersize, length)

getstuff([3,4,55,5])

print(450//100)