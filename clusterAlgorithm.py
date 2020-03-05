import random
import math

class ClusterAlgorithm:

    x_pnts = []
    y_pnts = []
    clusters = []

    def __init__(self, text):
        f = open(text, "r")
        search_file = f.readline()
        self.k = int(search_file[search_file.find("k=")+2])
        self.set_array(f)
        self.size = len(self.x_pnts)
        f.close()
    def set_array(self, file):
        for x, line in enumerate(file):
            if x > 0:
                first_int = ""
                second_int = ""
                first_finished = False
                for char in line:
                    if char.isdigit():
                        if first_finished == False:
                            first_int = first_int + char
                        else:
                            second_int = second_int + char
                    else:
                        first_finished = True
                self.x_pnts.append(int(first_int))
                self.y_pnts.append(int(second_int))
                self.clusters.append(0)

    def cluster_algorithm(self):
        centroids_x = []
        centroids_y = []
        for x in range(self.k):
            choice = random.randrange(self.size)
            centroids_x.append(self.x_pnts[choice])
            centroids_y.append(self.y_pnts[choice])

        filled = 0
        while filled < self.k:
            filled = self.k
            centroids_x = list(set(centroids_x))
            centroids_y = list(set(centroids_y))

            filled = len(centroids_x)
            if filled < self.k:
                choice = random.randrange(self.size)
                centroids_x.append(self.x_pnts[choice])
                centroids_y.append(self.y_pnts[choice])

        finished = False
        while not finished:
            for q in range(self.size):
                farthest = 0
                for i in range(self.k):
                    print(self.clusters)
                    dis = int(math.sqrt((self.x_pnts[q] - centroids_x[i]) ** 2
                                        + (self.y_pnts[q] - centroids_y[i]) ** 2))
                    if dis > farthest:
                        self.clusters[q] = i+1
                        farthest = dis

            for y in range(self.k):
                new_x_pnt = []
                new_y_pnt = []
                new_x = 0
                new_y = 0
                sum = 0
                for j in range(self.size):
                    if self.clusters[j] == y + 1:
                        new_x += self.x_pnts[j]
                        new_y += self.y_pnts[j]
                        sum += 1

                new_x_pnt.append(new_x / sum)
                new_y_pnt.append(new_y / sum)

            if (new_x_pnt.sort() == centroids_x.sort())  & (new_y_pnt.sort() == centroids_y.sort()):
                finished = True
            else:
                centroids_x = new_x_pnt
                centroids_y = new_y_pnt

    def Print(self, file_name):
        f = open(file_name, "w")

        for n in range (self.k):
            for x in range(0,self.size):
                if self.clusters[x] == n+1:
                    f.write("{}\t{}\t{}\n".format(self.x_pnts[x] ,self.y_pnts[x] ,self.clusters[x]))
        f.close()
