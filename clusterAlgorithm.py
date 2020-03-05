import random
import math


class ClusterAlgorithm:
    x_pnts = []
    y_pnts = []
    clusters = []

    def __init__(self, text):
        f = open(text, "r")
        search_file = f.readline()
        self.k = int(search_file[search_file.find("k=") + 2])
        self.set_array(f)
        self.size = len(self.x_pnts)
        self.set_centroids()
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

    def set_centroids(self):
        self.centroids_x = []
        self.centroids_y = []
        for x in range(self.k):
            choice = random.randrange(self.size)
            self.centroids_x.append(self.x_pnts[choice])
            self.centroids_y.append(self.y_pnts[choice])

        filled = 0
        while filled < self.k:
            filled = self.k
            self.centroids_x = list(set(self.centroids_x))
            self.centroids_y = list(set(self.centroids_y))

            filled = len(self.centroids_x)
            if filled < self.k:
                choice = random.randrange(self.size)
                self.centroids_x.append(self.x_pnts[choice])
                self.centroids_y.append(self.y_pnts[choice])

    def cluster_algorithm(self):
        count = 0
        finished = False

        while not finished:
            for q in range(self.size):
                distance = []
                for i in range(0, self.k):
                    dis = math.sqrt(
                        (self.centroids_x[i] - self.x_pnts[q]) ** 2 + (self.centroids_y[i] - self.y_pnts[q]) ** 2)
                    distance.append(dis)
                new_dis = distance[0]
                placement = 1
                for d in range(1, self.k):
                    if distance[d] < new_dis:
                        new_dis = distance[d]
                        placement = d + 1
                self.clusters[q] = placement
                distance.clear()

            new_x_pnt = []
            new_y_pnt = []
            for y in range(self.k):
                new_x = 0
                new_y = 0
                sum = 0
                for j in range(self.size):
                    if self.clusters[j] == y + 1:
                        new_x += self.x_pnts[j]
                        new_y += self.y_pnts[j]
                        sum += 1
                new_x_pnt.append(round(new_x / sum, 2))
                new_y_pnt.append(round(new_y / sum, 2))

            if count == 2:
                finished = True
            for n in range(self.k):
                self.centroids_x[n] = new_x_pnt[n]
                self.centroids_y[n] = new_y_pnt[n]
            new_x_pnt.clear()
            new_y_pnt.clear()
            count += 1

    def Print(self, file_name):
        f = open(file_name, "w")

        for n in range(self.k):
            for x in range(0, self.size):
                if self.clusters[x] == n + 1:
                    f.write("{}\t{}\t{}\n".format(self.x_pnts[x], self.y_pnts[x], self.clusters[x]))
        f.close()
