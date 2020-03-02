
class ClusterAlgorithm:

    coordinates = []

    def __init__(self, text):
        f = open(text, "r")
        search_file = f.readline()
        self.k = int(search_file[search_file.find("k=")+2])
        self.setArray(f)
        f.close()

    def setArray(self, file):
        for x, line in enumerate(file):
            if x > 2:
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




    def Print(self):
        
