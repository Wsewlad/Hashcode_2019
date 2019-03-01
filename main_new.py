import sys
import os.path
import threading


class Photo:
    def __init__(self, line, id):
        self.id = id
        self.count = int(line.split()[1])
        self.pos = line.split()[0]
        self.tags = set(line[line.find(line.split()[2]):].split())


class Slide:
    def __init__(self, photos):
        nb = len(photos)
        self.ids = []
        self.ids.append(photos[0].id)
        self.tags = photos[0].tags
        self.count = photos[0].count
        if nb == 2:
            self.ids.append(photos[1].id)
            self.tags = self.tags.union(photos[1].tags)
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


def get_intersect_tags(t1, t2):
    return t1.intersection(t2)


def check_tags(t1, t2):
    return {"t1": len(t1.difference(t2)), "equal": len(t1.intersection(t2)), "t2": len(t2.difference(t1))}


def find_factor(slide1, slide2):
    slide_tags = check_tags(slide1.tags, slide2.tags)
    return min(slide_tags["t1"], slide_tags["equal"], slide_tags["t2"])


def search_best_slide(photos):
    for i in range(len(photos) - 1):
        if i + 1 > len(photos) - 1:
            break
        min_intersect = len(get_intersect_tags(photos[i].tags, photos[i + 1].tags))
        p1_idx = i
        p2_idx = i + 1
        for j in range(i + 2, len(photos)):
            intersections = len(get_intersect_tags(photos[i].tags, photos[j].tags))
            if intersections < min_intersect:
                min_intersect = intersections
                p1_idx = i
                p2_idx = j
                if min_intersect == 0:
                    break
        slides.append(Slide([photos[p1_idx], photos[p2_idx]]))
        photos.pop(p2_idx)


def choose_by_tags(slides_array):
    for i in range(len(slides_array) - 1):
        max_factor = 0
        s1_idx = 0
        s2_idx = 0
        for j in range(i + 1, len(slides_array)):
            factor = find_factor(slides_array[i], slides_array[j])
            if factor > max_factor:
                max_factor = factor
                s1_idx = i
                s2_idx = j
                if max_factor >= 3:
                    break
        if max_factor > 0:
            slideshow.append(slides_array[s1_idx])
            slideshow.append(slides_array[s2_idx])
            slides_array.pop(s2_idx)

            # print(i, max_factor)
    # return result_array


if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        inputName = sys.argv[i]

        photos = []
        slides = []
        slideshow = []

        with open(inputName) as f:
            countFoto = int(f.readline())
            for i in range(countFoto):
                line = f.readline()
                obj = Photo(line, i)
                if obj.pos == "H":
                    slides.append(Slide([obj]))
                else:
                    photos.append(obj)

        # print("H:", len(slides))
        # print("V:", len(photos))
        sort_by_count(photos)

        search_best_slide(photos)

        sort_by_count(slides)

        # print_slides(slides)

        choose_by_tags(slides)


        # print_slides(slideshow)

        f = open(inputName + ".res", "w")
        f.write(str(len(slideshow)) + '\n')
        for s in slideshow:
            if len(s.ids) == 2:
                f.write(str(s.ids[0]) + " " + str(s.ids[1]) + '\n')
            else:
                f.write(str(s.ids[0]) + '\n')

