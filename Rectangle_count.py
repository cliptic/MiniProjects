''' Counting rectangles wiht vertical and horizontal sides from coordinated points.
EXAMPLE:
We have 6 points as below.
.1	.4	.5

.2	.3	.6
coordinated by x and y
1 (1,2)
2 (1,1)
3 (2,1)
4 (2,2)
5 (3,2)
6 (3,1)
We have 3 rectangles: 1234,1256,3456.
'''
# points = [(1,1), (1,2), (2,1), (2,2), (3,1), (3,2)]

#define the points as a list of tuples with coordinates of (x,y)
points = [(3,1), (1,2), (3,4), (1,4), (4,1), (4,2), (2,1), (1,1), (2,2), (3,2)]

import matplotlib.pyplot as plt

count = 0
vec = []
a = 0

points.sort()
print('You have defines the following points with coordinates (x,y): \n',points)
for i in range(len(points)):
	x = points[i][0]
	y = points[i][1]
	for m in range(len(points)-i):
		x1 = points[m+i][0]
		y1 = points[m+i][1]
		if (x1 == x) and (y1 != y) and (y1>y):
			# print('found a vertical line')
			# print('points number:', i+1, m+i+1)
			# after finding a vertical line do we look for a second vetical line 
			# or just a point on the right? point on the right
			for l in range(len(points)):
				x2 = points[l][0]
				y2 = points[l][1]
				if (x2 != x) and (y2 == y) and (x2>x):
					for k in range(len(points)-l):
						x3 = points[k+l][0]
						y3 = points[k+l][1]
						if (x2 == x3) and (y2 != y3) and (x1 != x3) and (y1 == y3):
							# print('found a rectangle')
							count += 1
							plt.plot([x,x2,x3,x1,x],[y,y2,y3,y1,y])
							

	# for above in point
plt.subplots
print('there are', count, 'rectangles')

a=[]
b=[]
for point in points:
	a.append(point[0])
	b.append(point[1])

plt.scatter(a,b)
plt.show()