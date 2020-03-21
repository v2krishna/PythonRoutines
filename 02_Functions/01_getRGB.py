"""Using the bit wise operators a sample program
"""

def getRGBfromInt(in_rgbinterger):
    blue = in_rgbinterger & 255
    green = (in_rgbinterger >> 8) & 255
    red = (in_rgbinterger >> 16) & 255
    return [red, green, blue]


def getIntFromRgb(in_rgb):
    red = in_rgb[0]
    green = in_rgb[1]
    blue = in_rgb[2]
    print(red, green, blue)
    o_rgbint = (red << 16) + (green<<8) + blue
    return o_rgbint


v_i1 = 20000
v_color = getRGBfromInt(v_i1)
print(v_color)

rgb1 = getIntFromRgb(v_color)
print(rgb1)