import clusterAlgorithm

def main():
#    test = clusterAlgorithm.ClusterAlgorithm("test.txt")
#    test.cluster_algorithm()
#    test.Print("outputTest.txt")

    input1 = clusterAlgorithm.ClusterAlgorithm("input1.txt")
    input1.cluster_algorithm()
    input1.Print("output1.txt")

    input2 = clusterAlgorithm.ClusterAlgorithm("input2.txt")
    input2.cluster_algorithm()
    input2.Print("output2.txt")

    input3 = clusterAlgorithm.ClusterAlgorithm("input3.txt")
    input3.cluster_algorithm()
    input3.Print("output3.txt")

    input4 = clusterAlgorithm.ClusterAlgorithm("input4.txt")
    input4.cluster_algorithm()
    input4.Print("output4.txt")

main()