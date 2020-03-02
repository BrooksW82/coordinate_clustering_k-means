import clusterAlgorithm

def main():
    test = clusterAlgorithm.ClusterAlgorithm("test.txt")

    for i in range(0,len(test.coordinates)):
        print(test.coordinates[i])

main()