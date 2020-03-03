import math
import random

class ClusterAlgorithm:

    coordinates = []

    def __init__(self, text):
        f = open(text, "r")
        search_file = f.readline()
        self.k = int(search_file[search_file.find("k=")+2])
        self.set_array(f)
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
                self.coordinates.append([int(first_int), int(second_int), 0])

    #creates a list of k amount of random points, where x-axis ranges between 0-1000 and y-axis ranges from 0-500
    def cluster_algorithm(self):
        ran_points = []
        for x in range(self.k):
            ran_points.append([random.randrange(1000),random.randrange(500)])
        finished = False
        while not finished:
            for x in range(len(self.coordinates)):
                farthest = 0
                for i in range(self.k):
                    dis = int(math.sqrt((self.coordinates[x][0] - ran_points[i][0])**2
                                    + (self.coordinates[x][1] - ran_points[i][1])**2))
                    if dis > farthest:
                        self.coordinates[x][2] = i+1
                        farthest = dis

            for y in range(self.k):
                new_point = []
                new_x = 0
                new_y = 0
                sum   = 0
                for j in range(len(self.coordinates)):
                    if self.coordinates[j][2] == y+1:
                        new_x += self.coordinates[j][0]
                        new_y += self.coordinates[j][1]
                        sum += 1
                new_point.append([int(new_x/sum), int(new_y/sum)])

            if new_point != ran_points:
                

    def Print(self, file_name):
        f = open(file_name, "w")
        for x in range(0,len(self.coordinates)):
            f.write("{}\t{}\t{}\n".format(self.coordinates[x][0] ,self.coordinates[x][1] , self.coordinates[x][2]))
        f.close()
