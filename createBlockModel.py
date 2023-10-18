from panda3d.core import Point3D
from panda3d.egg import *
from panda3d.egg import EggData, EggGroup, EggLine, EggPolygon, EggVertex, EggVertexPool

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
        [vertices[0], vertices[1], vertices[5], vertices[4]],
        [vertices[0], vertices[2], vertices[6], vertices[4]],
        [vertices[4], vertices[5], vertices[7], vertices[6]],
        [vertices[2], vertices[3], vertices[7], vertices[6]],
        [vertices[1], vertices[3], vertices[7], vertices[5]],
    ]

    for i in range(0, 6):
        face = EggPolygon(name + ".Face" + str(i))
        face.set_color(RED)
        face.set_bface_flag(True)
        for vert in faceVertices[i]:
            face.add_vertex(vert)
        cube.add_child(face)

    for i in range(0, 6):
        line = EggLine(name + ".Line" + str(i))
        line.set_color(BLACK)
        line.set_bface_flag(True)
        line.set_thick(3)
        for vert in faceVertices[i]:
            line.add_vertex(vert)
        cube.add_child(line)

    return cube


def createBlockModel():
    block = EggGroup("Block")

    cube0 = createCube(Point3D(0.5, 0.5, 0.5), 1, "Cube0")
    block.add_child(cube0)

    cube1 = createCube(Point3D(1.5, 0.5, 0.5), 1, "Cube1")
    block.add_child(cube1)

    data = EggData()
    data.add_child(block)

    data.writeEgg("models/blockModel.egg")


if __name__ == "__main__":
    createBlockModel()
