import clusterAlgorithm

def main():
    test = clusterAlgorithm.ClusterAlgorithm("test.txt")

    for i in range(0,len(test.coordinates)):
        test.Print("outputTest.txt")
main()