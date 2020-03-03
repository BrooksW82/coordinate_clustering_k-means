from sklearn.cluster import KMeans

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
                self.coordinates.append([int(first_int), int(second_int)])

    def cluster_algorithm(self):
        kmeans = KMeans(n_clusters=self.k)
        kmeans.fit(self.coordinates)
        self.labels = kmeans.labels_

    def Print(self, file_name):
        f = open(file_name, "w")
        counter = 0
        while counter < self.k:
            for x in range(0,len(self.coordinates)):
                if self.labels[x] == counter:
                    f.write("{}\t{}\t{}\n".format(self.coordinates[x][0] ,self.coordinates[x][1] , self.labels[x] + 1))
            counter += 1
        f.close()
