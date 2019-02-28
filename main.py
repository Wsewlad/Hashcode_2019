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


def sort_photos_by_count(photos):
    photos.sort(key=lambda x: x.id, reverse=True)



if len(sys.argv) > 1:
    inputName = sys.argv[1]

    photos = []

    with open(inputName) as f:
        countFoto = int(f.readline())
        for i in range(countFoto):
            line = f.readline()
            photos.append(Photo(line, i))

    print_photos(photos)
    sort_photos_by_count(photos)
    print "-----"
    print_photos(photos)
    test = [1,6,4,3,5,2]
    print test
    test.sort(reverse=True)
    print "---", test