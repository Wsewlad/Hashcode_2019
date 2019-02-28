import sys
import os.path


class Photo:
    def __init__(self, line, id):
        self.id = id
        self.count = int(line.split()[1])
        self.pos = line.split()[0]
        self.tags = line[line.find(line.split()[2]):].split()



def print_photos(photos):
    for p in photos:
        print "id:", p.id, "count:", p.count, "pos:", p.pos, "tags:", p.tags


if len(sys.argv) > 1:
    inputName = sys.argv[1]

    photos = []

    with open(inputName) as f:
        countFoto = int(f.readline())
        for i in range(countFoto):
            line = f.readline()
            photos.append(Photo(line, i))

    print_photos(photos)