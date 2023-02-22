#  File: Geometry.py

# Description: This lab creates several classes for geometric shapes - Point, Sphere, Cube, and Cylinder - with
# features involving intersections and engulfment of other shapes

#  Student Name: Julian Wearden

#  Student UT EID: jfw864

#  Partner Name: N/A

#  Partner UT EID: N/A

#  Course Name: CS 313E

#  Unique Number: 52604

#  Date Created: 09/19/2021

#  Date Last Modified: 09/19/2021


import math
import sys


# Input: Two floating point numbers
# Output: Returns if they are equal with some degree of tolerance (tol)
def is_equal(a, b):
    tol = 1.0e-6
    return abs(a - b) < tol


class Point(object):
    # constructor with default values
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    # create a string representation of a Point
    # returns a string of the form (x, y, z)
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

    # get distance to another Point object
    # other is a Point object
    # returns the distance as a floating point number
    def distance(self, other):
        x_val = (self.x - other.x) ** 2
        y_val = (self.y - other.y) ** 2
        z_val = (self.z - other.z) ** 2
        return math.sqrt(x_val + y_val + z_val)

    # test for equality between two points
    # other is a Point object
    # returns a Boolean
    def __eq__(self, other):
        if is_equal(self.x, other.x) and is_equal(self.y, other.y) and is_equal(self.z, other.z):
            return True
        else:
            return False


class Sphere(object):
    # constructor with default values
    def __init__(self, x=0.0, y=0.0, z=0.0, radius=1.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.radius = float(radius)
        self.center = Point(x, y, z)

    # returns string representation of a Sphere of the form:
    # Center: (x, y, z), Radius: value
    def __str__(self):
        return "Center: (" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "), " + "Radius: " + str(
            self.radius)

    # compute surface area of Sphere
    # returns a floating point number
    def area(self):
        return float(4 * math.pi * (self.radius ** 2))

    # compute volume of a Sphere
    # returns a floating point number
    def volume(self):
        return float((4 / 3) * math.pi * (self.radius ** 3))

    # determines if a Point is strictly inside the Sphere
    # p is Point object
    # returns a Boolean
    def is_inside_point(self, p):
        x_val = (p.x - self.x) ** 2
        y_val = (p.y - self.y) ** 2
        z_val = (p.z - self.z) ** 2
        # Check is distance between center & point < radius
        return math.sqrt(x_val + y_val + z_val) < self.radius  # If this is causing problems try <=

    # determine if another Sphere is strictly inside this Sphere
    # other is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, other):
        minX, maxX, minY, maxY, minZ, maxZ = self.min_maxXYZ()
        ominX, omaxX, ominY, omaxY, ominZ, omaxZ = other.min_maxXYZ()
        if ominX <= minX or omaxX >= maxX or ominY <= minY or omaxY >= maxY or ominZ <= minZ or omaxZ >= maxZ:
            return False
        else:
            return True

    # determine if a Cube is strictly inside this Sphere
    # determine if the eight corners of the Cube are strictly
    # inside the Sphere
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube(self, a_cube):
        d = a_cube.side / 2  # Distance change from center of cube by plane
        # Make point of each vertices
        point0 = Point(a_cube.x - d, a_cube.y - d, a_cube.z - d)
        point1 = Point(a_cube.x - d, a_cube.y - d, a_cube.z + d)
        point2 = Point(a_cube.x - d, a_cube.y + d, a_cube.z - d)
        point3 = Point(a_cube.x - d, a_cube.y + d, a_cube.z + d)
        point4 = Point(a_cube.x + d, a_cube.y - d, a_cube.z - d)
        point5 = Point(a_cube.x + d, a_cube.y - d, a_cube.z + d)
        point6 = Point(a_cube.x + d, a_cube.y + d, a_cube.z - d)
        point7 = Point(a_cube.x + d, a_cube.y + d, a_cube.z + d)
        # Return true if all points inside sphere
        return self.is_inside_point(point0) and self.is_inside_point(point1) and self.is_inside_point(point2) \
               and self.is_inside_point(point3) and self.is_inside_point(point4) and self.is_inside_point(point5) \
               and self.is_inside_point(point6) and self.is_inside_point(point7)

    # determine if a Cylinder is strictly inside this Sphere
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cyl(self, a_cyl):
        minX, maxX, minY, maxY, minZ, maxZ = self.min_maxXYZ()
        cminX, cmaxX, cminY, cmaxY, cminZ, cmaxZ = a_cyl.min_maxXYZ()
        if cminX <= minX or cmaxX >= maxX or cminY <= minY or cmaxY >= maxY or cminZ <= minZ or cmaxZ >= maxZ:
            return False
        else:
            return True

    # determine if another Sphere intersects this Sphere
    # other is a Sphere object
    # two spheres intersect if they are not strictly inside
    # or not strictly outside each other
    # returns a Boolean
    def does_intersect_sphere(self, other):
        if self.is_inside_sphere(other):  # Makre sure not strictly inside
            return False
        else:
            x_val = (self.x - other.x) ** 2
            y_val = (self.y - other.y) ** 2
            z_val = (self.z - other.z) ** 2
            # Check if distance between centers <= sum of radius
            return math.sqrt(x_val + y_val + z_val) <= (self.radius + other.radius)

    # determine if a Cube intersects this Sphere
    # the Cube and Sphere intersect if they are not
    # strictly inside or not strictly outside the other
    # a_cube is a Cube object
    # returns a Boolean
    def does_intersect_cube(self, a_cube):
        if self.is_inside_cube(a_cube):  # Make sure not strictly inside
            return False
        else:
            d = a_cube.side / 2  # Distance change from center of cube by plane
            # Make point of each vertices
            point0 = Point(a_cube.x - d, a_cube.y - d, a_cube.z - d)
            point1 = Point(a_cube.x - d, a_cube.y - d, a_cube.z + d)
            point2 = Point(a_cube.x - d, a_cube.y + d, a_cube.z - d)
            point3 = Point(a_cube.x - d, a_cube.y + d, a_cube.z + d)
            point4 = Point(a_cube.x + d, a_cube.y - d, a_cube.z - d)
            point5 = Point(a_cube.x + d, a_cube.y - d, a_cube.z + d)
            point6 = Point(a_cube.x + d, a_cube.y + d, a_cube.z - d)
            point7 = Point(a_cube.x + d, a_cube.y + d, a_cube.z + d)
            # Return true if any point inside sphere
            return self.is_inside_point(point0) or self.is_inside_point(point1) or self.is_inside_point(point2) \
                   or self.is_inside_point(point3) or self.is_inside_point(point4) or self.is_inside_point(point5) \
                   or self.is_inside_point(point6) or self.is_inside_point(point7)

    # return the largest Cube object that is circumscribed
    # by this Sphere
    # all eight corners of the Cube are on the Sphere
    # returns a Cube object
    def circumscribe_cube(self):
        side = 2 * self.radius / math.sqrt(3)
        side = "{:.1f}".format(side)
        side = float(side)
        return Cube(self.x, self.y, self.z, side)

    def min_maxXYZ(self):
        minX = self.x - self.radius
        maxX = self.x + self.radius
        minY = self.y - self.radius
        maxY = self.y + self.radius
        minZ = self.z - self.radius
        maxZ = self.z + self.radius
        return minX, maxX, minY, maxY, minZ, maxZ


class Cube(object):
    # Cube is defined by its center (which is a Point object)
    # and side. The faces of the Cube are parallel to x-y, y-z,
    # and x-z planes.
    def __init__(self, x=0.0, y=0.0, z=0.0, side=1.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.side = float(side)
        self.center = Point(x, y, z)

    # string representation of a Cube of the form:
    # Center: (x, y, z), Side: value
    def __str__(self):
        return "Center: (" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "), " + "Side: " + str(self.side)

    # compute the total surface area of Cube (all 6 sides)
    # returns a floating point number
    def area(self):
        return 6 * (self.side ** 2)

    # compute volume of a Cube
    # returns a floating point number
    def volume(self):
        return self.side ** 3

    # determines if a Point is strictly inside this Cube
    # p is a point object
    # returns a Boolean
    def is_inside_point(self, p):
        minX, maxX, minY, maxY, minZ, maxZ = self.min_maxXYZ()
        return minX < p.x < maxX and minY < p.y < maxY and minZ < p.z < maxZ

    # determine if a Sphere is strictly inside this Cube
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, a_sphere):
        minX, maxX, minY, maxY, minZ, maxZ = self.min_maxXYZ()
        sminX, smaxX, sminY, smaxY, sminZ, smaxZ = a_sphere.min_maxXYZ()
        if sminX <= minX or smaxX >= maxX or sminY <= minY or smaxY >= maxY or sminZ <= minZ or smaxZ >= maxZ:
            return False
        else:
            return True

    # determine if another Cube is strictly inside this Cube
    # other is a Cube object
    # returns a Boolean
    def is_inside_cube(self, other):
        minX, maxX, minY, maxY, minZ, maxZ = self.min_maxXYZ()
        ominX, omaxX, ominY, omaxY, ominZ, omaxZ = other.min_maxXYZ()
        if ominX <= minX or omaxX >= maxX or ominY <= minY or omaxY >= maxY or ominZ <= minZ or omaxZ >= maxZ:
            return False
        else:
            return True

    # determine if a Cylinder is strictly inside this Cube
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cylinder(self, a_cyl):
        minX, maxX, minY, maxY, minZ, maxZ = self.min_maxXYZ()
        cminX, cmaxX, cminY, cmaxY, cminZ, cmaxZ = a_cyl.min_maxXYZ()
        if cminX <= minX or cmaxX >= maxX or cminY <= minY or cmaxY >= maxY or cminZ <= minZ or cmaxZ >= maxZ:
            return False
        else:
            return True

    # determine if another Cube intersects this Cube
    # two Cube objects intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cube object
    # returns a Boolean
    def does_intersect_cube(self, other):
        minX, maxX, minY, maxY, minZ, maxZ = self.min_maxXYZ()
        ominX, omaxX, ominY, omaxY, ominZ, omaxZ = other.min_maxXYZ()
        if minX <= omaxX and maxX >= ominX and minY <= omaxY and maxY >= ominY and minZ <= omaxZ and maxZ >= ominZ and \
                not self.is_inside_cube(other):
            return True
        else:
            return False

    # determine the volume of intersection if this Cube
    # intersects with another Cube
    # other is a Cube object
    # returns a floating point number
    def intersection_volume(self, other):
        minX, maxX, minY, maxY, minZ, maxZ = self.min_maxXYZ()
        ominX, omaxX, ominY, omaxY, ominZ, omaxZ = other.min_maxXYZ()
        if self.does_intersect_cube(other):
            return abs(maxX - ominX) * abs(maxY - ominY) * abs(maxZ - ominZ)
        elif self.is_inside_cube(other):
            return other.volume()
        else:
            return 0.0

    # return the largest Sphere object that is inscribed
    # by this Cube
    # Sphere object is inside the Cube and the faces of the
    # Cube are tangential planes of the Sphere
    # returns a Sphere object
    def inscribe_sphere(self):
        return Sphere(self.x, self.y, self.z, self.side / 2)

    # returns the lowest and highest X, Y, and Z values of the cube
    def min_maxXYZ(self):
        minX = self.x - (self.side / 2)
        maxX = self.x + (self.side / 2)
        minY = self.y - (self.side / 2)
        maxY = self.y + (self.side / 2)
        minZ = self.z - (self.side / 2)
        maxZ = self.z + (self.side / 2)
        return minX, maxX, minY, maxY, minZ, maxZ


class Cylinder(object):
    # Cylinder is defined by its center (which is a Point object),
    # radius and height. The main axis of the Cylinder is along the
    # z-axis and height is measured along this axis
    def __init__(self, x=0.0, y=0.0, z=0.0, radius=1.0, height=1.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.radius = float(radius)
        self.height = float(height)
        self.center = Point(x, y, z)

    # returns a string representation of a Cylinder of the form:
    # Center: (x, y, z), Radius: value, Height: value
    def __str__(self):
        return "Center: (" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "), " + "Radius: " + str(
            self.radius) + ", Height: " + str(self.height)

    # compute surface area of Cylinder
    # returns a floating point number
    def area(self):
        return (2 * math.pi * self.radius * self.height) + (2 * math.pi * (self.radius ** 2))

    # compute volume of a Cylinder
    # returns a floating point number
    def volume(self):
        return math.pi * (self.radius ** 2) * self.height

    # determine if a Point is strictly inside this Cylinder
    # p is a Point object
    # returns a Boolean
    def is_inside_point(self, p):
        # center_point = Point(self.x, self.y, self.z)
        # distance = math.sqrt((center_point.x - p.x) ** 2 + (center_point.y - p.y) ** 2)
        # if (p.z > self.z) and (p.z < (self.z + self.height)) and (distance < self.radius):
        #     return True
        # else:
        #     return False
        minX, maxX, minY, maxY, minZ, maxZ = self.min_maxXYZ()
        if p.z >= maxZ or p.z <= minZ:
            return False
        else:
            return ((p.x - self.center.x) ** 2 + (p.y - self.center.y) ** 2) < self.radius ** 2

    # determine if a Sphere is strictly inside this Cylinder
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, a_sphere):
        minX, maxX, minY, maxY, minZ, maxZ = self.min_maxXYZ()
        sminX, smaxX, sminY, smaxY, sminZ, smaxZ = a_sphere.min_maxXYZ()

        # If the z value of the sphere + radius of the sphere is > maxZ of cylinder
        if smaxZ > maxZ:
            return False
        elif math.sqrt((self.x - a_sphere.x) ** 2 + (self.y - a_sphere.y) ** 2) + a_sphere.radius < self.radius:
            return True
        else:
            return False
        # # If distance between centers (xy only) > radius
        #
        # if sminX <= minX or smaxX >= maxX or sminY <= minY or smaxY >= maxY or sminZ <= minZ or smaxZ >= maxZ:
        #     return False
        # else:
        #     return True

    # determine if a Cube is strictly inside this Cylinder
    # determine if all eight corners of the Cube are inside
    # the Cylinder
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube(self, a_cube):
        minX, maxX, minY, maxY, minZ, maxZ = self.min_maxXYZ()
        cminX, cmaxX, cminY, cmaxY, cminZ, cmaxZ = a_cube.min_maxXYZ()
        if cminX <= minX or cmaxX >= maxX or cminY <= minY or cmaxY >= maxY or cminZ <= minZ or cmaxZ >= maxZ:
            return False
        else:
            return True

    # determine if another Cylinder is strictly inside this Cylinder
    # other is Cylinder object
    # returns a Boolean
    def is_inside_cylinder(self, other):
        minX, maxX, minY, maxY, minZ, maxZ = self.min_maxXYZ()
        ominX, omaxX, ominY, omaxY, ominZ, omaxZ = other.min_maxXYZ()
        if ominX < minX or omaxX > maxX or ominY < minY or omaxY > maxY or ominZ < minZ or omaxZ > maxZ:
            return False
        else:
            return True

    # determine if another Cylinder intersects this Cylinder
    # two Cylinder object intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cylinder object
    # returns a Boolean
    def does_intersect_cylinder(self, other):
        minX, maxX, minY, maxY, minZ, maxZ = self.min_maxXYZ()
        ominX, omaxX, ominY, omaxY, ominZ, omaxZ = other.min_maxXYZ()
        #print(self.center, self.radius, self.height, "\n", other.center, other.radius, other.height)
        if minX <= omaxX and maxX >= ominX and minY <= omaxY and maxY >= ominY and minZ <= omaxZ and maxZ >= ominZ and (
                not self.is_inside_cylinder(other)):
            return True
        else:
            return False

    def min_maxXYZ(self):
        minX = self.x - self.radius
        maxX = self.x + self.radius
        minY = self.y - self.radius
        maxY = self.y + self.radius
        minZ = self.z
        maxZ = self.z + self.height
        return minX, maxX, minY, maxY, minZ, maxZ


def read_line():
    line = sys.stdin.readline()
    line = line.rstrip('\n')
    line = line.split("#", 1)[0]
    line = line.split(" ")
    while '' in line:
        line.remove('')
    return line


def main():
    # read the coordinates of the first Point p
    file = read_line()
    # create a Point object
    p = Point(float(file[0]), float(file[1]), float(file[2]))

    # read the coordinates of the second Point q
    file = read_line()
    # create a Point object
    q = Point(float(file[0]), float(file[1]), float(file[2]))

    # read the coordinates of the center and radius of sphereA
    file = read_line()
    # create a Sphere object
    sphereA = Sphere(float(file[0]), float(file[1]), float(file[2]), float(file[3]))

    # read the coordinates of the center and radius of sphereB
    file = read_line()
    # create a Sphere object
    sphereB = Sphere(float(file[0]), float(file[1]), float(file[2]), float(file[3]))

    # read the coordinates of the center and side of cubeA
    file = read_line()
    # create a Cube object
    cubeA = Cube(float(file[0]), float(file[1]), float(file[2]), float(file[3]))

    # read the coordinates of the center and side of cubeB
    file = read_line()
    # create a Cube object
    cubeB = Cube(float(file[0]), float(file[1]), float(file[2]), float(file[3]))

    # read the coordinates of the center, radius and height of cylA
    file = read_line()
    # create a Cylinder object
    cylA = Cylinder(float(file[0]), float(file[1]), float(file[2]), float(file[3]), float(file[4]))

    # read the coordinates of the center, radius and height of cylB
    file = read_line()
    # create a Cylinder object
    cylB = Cylinder(float(file[0]), float(file[1]), float(file[2]), float(file[3]), float(file[4]))

    ##POINTS##
    # print if the distance of p from the origin is greater
    # than the distance of q from the origin
    origin = Point()
    if p.distance(origin) > q.distance(origin):
        print("Distance of Point p from the origin is greater than the distance of Point q from the origin")
    else:
        print("Distance of Point p from the origin is not greater than the distance of Point q from the origin")

    ##SPHERES##
    # print if Point p is inside sphereA
    if sphereA.is_inside_point(p):
        print("Point p is inside sphereA")
    else:
        print("Point p is not inside sphereA")
    # print if sphereB is inside sphereA
    if sphereA.is_inside_sphere(sphereB):
        print("sphereB is inside sphereA")
    else:
        print("sphereB is not inside sphereA")
    # print if cubeA is inside sphereA
    if sphereA.is_inside_cube(cubeA):
        print("cubeA is inside sphereA")
    else:
        print("cubeA is not inside sphereA")
    # print if cylA is inside sphereA
    if sphereA.is_inside_cyl(cylA):
        print("cylA is inside sphereA")
    else:
        print("cylA is not inside sphereA")
    # print if sphereA intersects with sphereB
    if sphereA.does_intersect_sphere(sphereB):
        print("sphereA does intersect sphereB")
    else:
        print("sphereA does not intersect sphereB")
    # print if cubeB intersects with sphereB
    if sphereB.does_intersect_cube(cubeB):
        print("cubeB does intersect sphereB")
    else:
        print("cubeB does not intersect sphereB")

    # print if the volume of the largest Cube that is circumscribed
    # by sphereA is greater than the volume of cylA
    if sphereA.circumscribe_cube().volume() > cylA.volume():
        print("Volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA")
    else:
        print("Volume of the largest Cube that is circumscribed by sphereA is not greater than the volume of cylA")

    ##CUBES##
    # print if Point p is inside cubeA
    if cubeA.is_inside_point(p):
        print("Point p is inside cubeA")
    else:
        print("Point p is not inside cubeA")
    # print if sphereA is inside cubeA
    if cubeA.is_inside_sphere(sphereA):
        print("sphereA is inside cubeA")
    else:
        print("sphereA is not inside cubeA")
    # print if cubeB is inside cubeA
    if cubeA.is_inside_cube(cubeB):
        print("cubeB is inside cubeA")
    else:
        print("cubeB is not inside cubeA")
    # print if cylA is inside cubeA
    if cubeA.is_inside_cylinder(cylA):
        print("cylA is inside cubeA")
    else:
        print("cylA is not inside cubeA")
    # print if cubeA intersects with cubeB
    if cubeB.does_intersect_cube(cubeA):
        print("cubeA does intersect cubeB")
    else:
        print("cubeA does not intersect cubeB")
    # print if the intersection volume of cubeA and cubeB
    # is greater than the volume of sphereA
    if cubeA.intersection_volume(cubeB) > sphereA.volume():
        print("Intersection volume of cubeA and cubeB is greater than the volume of sphereA")
    else:
        print("Intersection volume of cubeA and cubeB is not greater than the volume of sphereA")

    # print if the surface area of the largest Sphere object inscribed
    # by cubeA is greater than the surface area of cylA
    if cubeA.inscribe_sphere().area() > cylA.area():
        print("Surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA")
    else:
        print("Surface area of the largest Sphere object inscribed by cubeA is not greater than the surface area of "
              "cylA")

    ##CYLINDER##
    # print if Point p is inside cylA
    if cylA.is_inside_point(p):
        print("Point p is inside cylA")
    else:
        print("Point p is not inside cylA")
    # print if sphereA is inside cylA
    if cylA.is_inside_sphere(sphereA):
        print("sphereA is inside cylA")
    else:
        print("sphereA is not inside cylA")
    # print if cubeA is inside cylA
    if cylA.is_inside_cube(cubeA):
        print("cubeA is inside cylA")
    else:
        print("cubeA is not inside cylA")
    # print if cylB is inside cylA
    if cylA.is_inside_cylinder(cylB):
        print("cylB is inside cylA")
    else:
        print("cylB is not inside cylA")
    # print if cylB intersects with cylA
    if cylA.does_intersect_cylinder(cylB):
        print("cylB does intersect cylA")
    else:
        print("cylB does not intersect cylA")


if __name__ == "__main__":
    main()
