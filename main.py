import clusterAlgorithm

def main():
    test = clusterAlgorithm.ClusterAlgorithm("test.txt")
    test.cluster_algorithm()
    for i in range(0,len(test.coordinates)):
        print(test.coordinates[i])
        #test.Print("outputTest.txt")
main()