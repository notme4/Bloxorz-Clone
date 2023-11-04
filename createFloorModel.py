from panda3d.core import Mat4D, Point3D, Vec2D
from panda3d.egg import *
from panda3d.egg import EggData, EggGroup, EggPolygon, EggVertex, EggVertexPool

from draw import *


def createCube(center: Point3D, sideLength: float, name: str):
    cube = EggGroup(name)

    pts = [
        Point3D(-1, -1, -1),
        Point3D(-1, -1, 1),
        Point3D(-1, 1, -1),
        Point3D(-1, 1, 1),
        Point3D(1, -1, -1),
        Point3D(1, -1, 1),
        Point3D(1, 1, -1),
        Point3D(1, 1, 1),
    ]

    vertices = EggVertexPool(name + ".Vertices")

    for i in range(0, 8):
        v = EggVertex()
        offset = Point3D(sideLength / 2, sideLength / 2, sideLength / 2)
        offset.componentwise_mult(pts[i])
        v.set_pos(center + offset)
        vertices.add_vertex(v)

    cube.add_child(vertices)

    faceVertices = [
        [vertices[0], vertices[1], vertices[3], vertices[2]],
        [vertices[2], vertices[3], vertices[7], vertices[6]],
        [vertices[6], vertices[7], vertices[5], vertices[4]],
        [vertices[4], vertices[5], vertices[1], vertices[0]],
        [vertices[2], vertices[6], vertices[4], vertices[0]],
        [vertices[7], vertices[3], vertices[1], vertices[5]],
    ]

    UVBase = [
        Vec2D(0.015625, 0.015625),
        Vec2D(0.015625, 0.109375),
        Vec2D(0.109375, 0.109375),
        Vec2D(0.109375, 0.015625),
    ]
    UVOffset = [
        Vec2D(0.125, 0),
        Vec2D(0.125, 0.125),
        Vec2D(0.125, 0.250),
        Vec2D(0.125, 0.375),
        Vec2D(0.000, 0.250),
        Vec2D(0.250, 0.250),
    ]

    for i in range(0, 6):
        face = EggPolygon(name + ".Face" + str(i))
        face.set_bface_flag(True)

        faceVerticesPool = EggVertexPool(face.name + ".Vertices")
        for j, vertBase in enumerate(faceVertices[i], 0):
            vert = EggVertex(vertBase)
            faceVerticesPool.add_vertex(vert)
            vert.set_uv(UVBase[j] + UVOffset[i])
            face.add_vertex(vert)
        cube.add_child(faceVerticesPool)
        cube.add_child(face)

    return cube


def createBlockModel():
    from math import cos, sin

    block = EggGroup("Block")

    cube0 = createCube(Point3D(0.5, 0, 0), 1, "Cube0")
    block.add_child(cube0)

    cube1 = createCube(Point3D(-0.5, 0, 0), 1, "Cube1")
    block.add_child(cube1)

    data = EggData()
    data.add_child(block)

    data.writeEgg("models/floor.egg")


def deg2Rad(deg: float):
    from math import pi

    return pi * deg / 180


if __name__ == "__main__":
    createBlockModel()
