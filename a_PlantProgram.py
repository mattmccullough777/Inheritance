import a_PlantClass as pc

primrose = pc.Plant("Green")

sunflower = pc.Flower("Yellow",20) #needs 2 arguments because it's a flower

print(primrose.get_color())

print(sunflower.get_color())
print(sunflower.get_petals())

# this gives an error
# print(primrose.get_petals())
