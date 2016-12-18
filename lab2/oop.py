class MapObject:
    map = dict()

    def __setattr__(self, key, value):
        self.map[key] = value

    def __str__(self):
        return str(self.map)


if __name__ == '__main__':
    obj = MapObject()
    obj.x = 12
    obj.y = 10
    obj.x = 100
    print(obj)
