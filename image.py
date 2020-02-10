class picture:
    def __init__(self, n, w, h):
        self.name = n
        self.width, self.height = (w, h)
        self.pixels = [[[255, 255, 255] for i in range(self.width)] for j in range(self.height)]

def coolify_pic_ascii(g):
    a = 1
    b = 1
    for x in range(g.width):
        for y in range(g.height):
            n = g.pixels[x][y]
            n[0] = a % 256
            n[1] = b % 256
        a = a + 1
        b = b + 2

def print_pic_ascii(g):
    s = ""
    for x in range(g.width):
        for y in range(g.height):
            n = g.pixels[x][y]
            s += str(n[0]) + " " + str(n[1]) + " " + str(n[2]) + "  "
        s += "\n"
    #print(s)
    return s

def ppm_save_ascii(g):
    n = str(g.name)
    f = open(n + ".ppm", "w")
    f.write("P3\n" + str(g.width) + " " + str(g.height) + "\n255\n")
    f.write(print_pic_ascii(g))
    f.close()
    print(n + '.ppm')

def test(x, y, deltx, delty, y_int):
    return (delty *  x) - (deltx *  y) + (deltx * y_int)

def add_line(g, startx, starty, endx, endy):
    g.pixels[startx][starty] = [0, 0, 0]
    g.pixels[endx][endy] = [0, 0, 0]
    if endx - startx == 0:
        drawline_straight(g, startx, starty, endy)
    else:
        slope = (endy - starty)/(endx - startx)
        if (0 <= abs(slope) and abs(slope) < 1):
            drawline_octant_1(g, startx, starty, endx, endy)
        elif (1 <= abs(slope)):
            drawline_octant_2(g, startx, starty, endx, endy)
    # elif (slope < -1):
    #     drawline_octant_3(g, startx, starty, endx, endy)
    # elif (0 > slope and slope > -1):
    #     drawline_octant_4(g, startx, starty, endx, endy)
    # if (0 < slope && slope < 1):
    #     drawline_octant_5(g, startx, starty, endx, endy)
    # if (0 < slope && slope < 1):
    #     drawline_octant_6(g, startx, starty, endx, endy)
    # if (0 < slope && slope < 1):
    #     drawline_octant_7(g, startx, starty, endx, endy)
    # if (0 < slope && slope < 1):
    #     drawline_octant_8(g, startx, starty, endx, endy)
    # elif slope == 0:
    #     drawline_flat(g, startx, starty, endx)
    # else:
    #     drawline_straight(g, startx, starty, endy)
def drawline_straight(g, startx, starty, endy):
	# Reorder points to work with range loop
	if endy < starty:
		endy, starty = starty, endy
	for y in range(starty, endy):
		g.pixels[y][startx] = [0, 0, 0]

def drawline_octant_1(g, startx, starty, endx, endy):
	#This function will work for all gentle (not steep lines / abs(slope) <= 1). Quadrants 1, 4, 5, 8
	#Swap coordinates so you go from right to left. Turns quadrants 4 and 5 into quadrant 1 and 2 from a different perspective
	if endx < startx:
		endx, startx = startx, endx
		endy, starty = starty, endy
	deltax = (endx - startx)
	deltay = (endy - starty)
	y = starty
	#If your'e going to go up or down by 1 each time
	y_increment = int(deltay/abs(deltay)) if deltay else 1 # if horizantal, avoid divide be 0 error
	# If down, y_increment is negative
	if y_increment < 0:
		deltay = -deltay
	d = 2 * deltay - deltax
	for x in range(startx, endx):
		# Coordinates will be flipped when printed.
		g.pixels[g.height - 1 - y][x] = [0, 0, 0]
		if d >= 0:
			y += y_increment
			d -= 2 * deltax
		x += 1
		d += 2 * deltay
	print("initial y: " + str(y))
	print("deltax: " + str(deltax))
	print("deltay: " + str(deltay))

def drawline_octant_2(g, startx, starty, endx, endy):
    #This is the steep version of the shallow line function from before.
	if endy < starty:
		endx, startx = startx, endx
		endy, starty = starty, endy
	deltax = (endx - startx)
	deltay = (endy - starty)
	x = startx
	#If your'e going to go up or down by 1 each time
	x_increment = int(deltax/abs(deltax))
	# If down, y_increment is negative
	if x_increment < 0:
		deltax = -deltax
	d = 2 * deltax - deltay
	for y in range(starty, endy):
		# Coordinates will be flipped when printed.
		g.pixels[g.height - 1 - y][x] = [0, 0, 0]
		if d >= 0:
			x += x_increment
			d -= 2 * deltay
		y += 1
		d += 2 * deltax
	print("initial y: " + str(y))
	print("deltax: " + str(deltax))
	print("deltay: " + str(deltay))
# def drawline_octant_2(g, startx, starty, endx, endy):

# def drawline_octant_3(g, startx, starty, endx, endy):

# def drawline_octant_4(g, startx, starty, endx, endy):

# def drawline_octant_5(g, startx, starty, endx, endy):

# def drawline_octant_6(g, startx, starty, endx, endy):

# def drawline_octant_7(g, startx, starty, endx, endy):

# def drawline_octant_8(g, startx, starty, endx, endy):

n = picture('image', 500, 500)
# add_line(n, 50, 220, 241, 300)
# add_line(n, 220, 50, 300, 241)
# add_line(n, 241, 220, 50, 300)
# add_line(n, 300, 50, 220, 241)
# add_line(n, 0, 0, 400, 400)
# add_line(n, 499, 0, 0, 499)
# add_line(n, 0, 499, 499, 0)
# add_line(n, 499, 499, 0, 0)
# add_line(n, 50, 50, 250, 50)
# add_line(n, 50, 250, 50, 50)
add_line(n, 250, 400, 100, 100)
add_line(n, 250, 400, 400, 100)
add_line(n, 100, 100, 400, 100)
add_line(n, 250, 100, 175, 250)
add_line(n, 250, 100, 325, 250)
add_line(n, 175, 250, 325, 250)
#could make a method to generate sierpinski triangles but am too tired rn
ppm_save_ascii(n)
# coolify_pic(n)
#
# f = open("image.ppm", "w")
# f.write("P3\n500 500\n255\n")
#
# f.write(print_pic(n))
#
#
# f.close()
# print('image.ppm')
