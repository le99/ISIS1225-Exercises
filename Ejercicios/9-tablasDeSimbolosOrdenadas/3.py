# Completar la funcion
def heightNode(node):
  pass


tree = {
  "root": {
    "key": 50,
    "value": 3,
    "size": 3,
    "left": {
      "key": 10,
      "value": 3,
      "size": 3,
      "left": None,
      "right": None
    },
    "right": {
      "key": 90,
      "value": 3,
      "size": 3,
      "left": None,
      "right": None
    }
  }
}

print(heightNode(tree['root']))