import sys
import os.path


class Photo:
    def __init__(self, line, id):
        self.id = id
        self.count = int(line.split()[1])
        self.pos = line.split()[0]
        self.tags = line[line.find(line.split()[2]):].split()


class Slide:
    def __init__(self, photos):
        nb = len(photos)
        self.ids = []
        self.ids.append(photos[0].id)
        self.tags = photos[0].tags
        self.count = photos[0].count
        if nb == 2:
            self.ids.append(photos[1].id)
            self.tags = list(set((self.tags + photos[1].tags)))
            self.count = len(self.tags)


def print_photos(photos):
    print "Photos:"
    for p in photos:
        print "id:", p.id, "count:", p.count, "pos:", p.pos, "tags:", p.tags
    print "-----"


def print_slides(slides):
    print "Slides:"
    for s in slides:
        print "ids:", s.ids, "count:", s.count, "tags:", s.tags
    print "-----"


def sort_by_count(list):
    list.sort(key=lambda x: x.count, reverse=True)


def similar_tags_count(t1, t2):
        res = 0
        for x in t1:
            if x in t2:
                res += 1
        return res


def get_unique(tags):
    unique_list = []
    for x in tags:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

# def search_best_slide(photos):
#     if not photos[1]:
#         return
#     first = photos.pop[0]
#     stags = similar_tags_count(first.tags, photos[0].tags)
#     second_best = {"idx": 0, "res": stags}
#
#     for i in range(1, len(photos)):
#         stags = unique_tags_count(first.tags, photos[i].tags)
#         if second_best["res"] < stags:
#             second_best["res"] = stags
#             second_best["idx"] = i


def search_best_slide(photos):
    for i in range(len(photos) - 1):
        if not photos[i + 1]:
            break
        min = similar_tags_count(photos[i].tags, photos[i + 1].tags)
        obj1_index = i
        obj2_index = i + 1
        for j in range(i + 2, len(photos)):
            min_value_tags = similar_tags_count(photos[i].tags, photos[j].tags)
            if min_value_tags < min:
                min = min_value_tags
                obj1_index = i
                obj2_index = j
        print obj1_index, obj2_index
        slides.append(Slide([photos[obj1_index], photos[obj2_index]]))
        photos.pop(obj2_index)



if len(sys.argv) > 1:
    inputName = sys.argv[1]

    photos = []
    slides = []

    with open(inputName) as f:
        countFoto = int(f.readline())
        for i in range(countFoto):
            line = f.readline()
            obj = Photo(line, i)
            if obj.pos == "H":
                slides.append(Slide([obj]))
            else:
                photos.append(obj)

    # test = Slide([photos[0], photos[1]])
    sort_by_count(photos)

    search_best_slide(photos)
    sort_by_count(slides)

    print_photos(photos)
    print_slides(slides)
