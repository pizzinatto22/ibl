import math
import random

def spiral(width, height, number_of_points, angle, angle_step, distance, max_noise):
    data = []

    width = int(width / 2)
    height = int(height / 2)


    qt = 0
    i = 0
    while (qt < number_of_points):
        b = angle + angle_step * i
        
        i = i + 1

        x = i * math.cos(b) + random.randint(0,max_noise)
        y = i * math.sin(b) + random.randint(0,max_noise)

        size = len(data)

        if size == 0:
            d = 0
        else:
            row = data[size-1]
            dx = row['x'] - (x + width)
            dy = row['y'] - (y + height)
            d = math.sqrt(dx**2 + dy**2)

        if (size == 0 or d >= distance):
            qt = qt + 1

            if (abs(x) < width and abs(y) < height):
                data.append({'x': x + width, 
                             'y': y + height})
        

    
    return data

def spiralDouble(width, height, number_of_points, angle, angle_step, distance, max_noise):
    data0 = spiral(width, height, number_of_points, angle, angle_step, distance, max_noise)
    data1 = spiral(width, height, number_of_points, angle + math.pi, angle_step, distance, max_noise)

    for d in data0:
        d['class'] = 0
    
    for d in data1:
        d['class'] = 1
    

    return data0 + data1
