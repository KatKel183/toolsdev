camera = {"aperture": 1.4,
          "focal length": 10,
          "name": "renderCam"}

print("    Testing Camera Functions")
print(camera.get("name"))

# to add something to a dictionary: camera[key]
camera["name"] = "shotCam"
print(camera)
# remove an item from dictionary:
del camera['focal length']
print(camera)

try:
    camera['position']
except KeyError as err:
    print("Unable to find key {}".format(err))
