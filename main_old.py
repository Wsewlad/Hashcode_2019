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
    print("Photos:")
    for p in photos:
        print("id:", p.id, "count:", p.count, "pos:", p.pos, "tags:", p.tags)
    print("-----")


def print_slides(slides):
    print("Slides:")
    for s in slides:
        print("ids:", s.ids, "count:", s.count, "tags:", s.tags)
    print("-----")


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


def compare(object1, object2):
    equal = 0
    equal_tags = []
    diff1 = 0
    diff2 = 0
    for i in object1.tags:
        changed = False
        for j in object2.tags:
            if i == j:
                equal = equal + 1
                changed = True
                equal_tags.append(i)
                break
        if not changed:
            diff1 = diff1 + 1

    for i in object2.tags:
        if not (i in equal_tags):
            found = False
            for j in object1.tags:
                if j == i:
                    found = True
                    break
            if not found:
                diff2 = diff2 + 1

    values = [equal, diff1, diff2]
    return min(values)


def choose_by_tags(slides_array):
    result_array = []
    for i in range(len(slides_array) - 1):
        maximum = 0
        obj1_index = 0
        obj2_index = 0
        for j in range(i + 1, len(slides_array)):
            min_value_tags = compare(slides_array[i], slides_array[j])
            if min_value_tags > maximum:
                maximum = min_value_tags
                obj1_index = i
                obj2_index = j
        if maximum > 0:
            result_array.append(slides_array[obj1_index])
            result_array.append(slides_array[obj2_index])
            slides_array.pop(obj2_index)
    return result_array


def search_best_slide(photos):
    for i in range(len(photos) - 1):
        if i + 1 >= len(photos) - 1:
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
        slides.append(Slide([photos[obj1_index], photos[obj2_index]]))
        photos.pop(obj2_index)


if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        inputName = sys.argv[i]

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

        sort_by_count(photos)

        search_best_slide(photos)

        sort_by_count(slides)

        res_slides = choose_by_tags(slides)
        # print_slides(res_slides)

        f = open(inputName + ".res", "w")
        f.write(str(len(res_slides)) + '\n')
        for i in res_slides:
            if len(i.ids) == 2:
                f.write(str(i.ids[0]) + " " + str(i.ids[1]) + '\n')
            else:
                f.write(str(i.ids[0]) + '\n')

