import math
Locations=tuple()
Locations=[(37.571650, 126.976480),(37.570200, 126.982992),(37.576548, 126.985449),(37.574528, 126.957726),(37.563637, 126.975359)]
gyung=(37.575825, 126.973473)
d=list()
for i in Locations:
 distance=math.sqrt((i[0]-gyung[0])**2+(i[1]-gyung[1])**2)
 d.append(distance)
 print distance

print 'the minimum is %s' %min(d)
raw_input('201611069_w9main hw')