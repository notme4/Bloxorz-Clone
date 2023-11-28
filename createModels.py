from panda3d.core import Point3D, Vec2D
from panda3d.egg import (
    EggData,
    EggGroup,
    EggMaterial,
    EggPolygon,
    EggTexture,
    EggVertex,
    EggVertexPool,
)

from draw import *


def createCube(
    center: Point3D,
    sideLength: float,
    name: str,
    texture: str | None = None,
    material: EggMaterial | None = None,
):
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

        if texture:
            face.add_texture(EggTexture("BlockTexture", texture))

        if material:
            face.set_material(material)

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
    block = EggGroup("Block")

    cube0 = createCube(Point3D(0, 0.5, 0), 1, "Cube0", "models/BlockTexture-V5.png")
    block.add_child(cube0)

    cube1 = createCube(Point3D(0, -0.5, 0), 1, "Cube1", "models/BlockTexture-V5.png")
    block.add_child(cube1)

    block.set_cs_type(EggGroup.CST_polyset)
    block.set_collide_flags(EggGroup.CF_keep | EggGroup.CF_descend)

    data = EggData()
    data.add_child(block)

    data.writeEgg("models/blockModel.egg")


def createFloorModel(color: Vec4):
    mat = EggMaterial("Floor.Mat")
    mat.set_base(color)
    mat.set_amb(color)
    mat.set_emit(Vec4(0, 0, 0, 1))
    mat.set_spec(color)
    mat.set_shininess(0.5)
    mat.set_roughness(0.5)
    mat.set_metallic(0)
    mat.set_ior(1.45)
    mat.set_local(True)

    floor = createCube(Point3D(0, 0, 0), 1, "Floor", "models/FloorTexture.png", mat)

    floor.set_cs_type(EggGroup.CST_polyset)
    floor.set_collide_flags(EggGroup.CF_keep | EggGroup.CF_descend)

    data = EggData()
    data.add_child(floor)

    return data


def createBaseFloorModel():
    data = createFloorModel(GRAY)
    data.writeEgg("models/baseTilePy.egg")


def createWinFloorModel():
    data = createFloorModel(RED)
    data.writeEgg("models/winTilePy.egg")

def createWinFloorModel():
    data = createFloorModel(YELLOW)
    data.writeEgg("models/fallTilePy.egg")


def deg2Rad(deg: float):
    from math import pi

    return pi * deg / 180


if __name__ == "__main__":
    createBlockModel()
    createBaseFloorModel()
    createWinFloorModel()
    createWinFloorModel()
