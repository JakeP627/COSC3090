import numpy as np

def centerToCluster(data, centers, clusters, k):
    for item in data:
        #find closest cluseter to center
        mu_index = min([(i[0], np.linalg.norm(item - centers[i[0]])) \
                        for i in enumerate(centers)], key=lambda t: t[1])[0]
        try:
            clusters[mu_index].append(item)
        except KeyError:
            clusters[mu_index] = [item]

    for cluster in clusters:
        if not cluster:
            centers.append(data[np.random.randint(0, k)])
            #cluster.append(data[np.random.randint(0, len(data), size=1)].flatten().tolist())
    return clusters

def clustertoCenter():
    newCenter = 0
    return newCenter

def randomCenters(d, centers, k):
    for cluster in range(0, k):
        #centers.append(d[np.random.randint(0, len(d), size=1)].flatten().tolist())
        centers.append(d[np.random.randint(0,k)])
    return centers


def llyodAlgo(k, m, data):
    centers = []
    centers = randomCenters(data, centers, k)
    #print(centers)
    oldCent = [[] for i in range(k)]

    while not (oldCent == centers):
        clusters = [[] for i in range(k)]
        clusters = centerToCluster(data, centers, clusters, k)

        index = 0
        for cluster in clusters:
            oldCent[index] = centers[index]
            centers[index] = np.mean(cluster, axis=0).tolist()
            index += 1

    return centers


k = 2
m = 2
data = [[2, 2],[1.3, 1.1],[1.3, 0.2],[0.6, 2.8],
[3.0, 3.2],[1.2, 0.7],[1.4, 1.6],[1.2, 1.0],
[1.2, 1.1],[0.6, 1.5],[1.8, 2.6],[1.2, 1.3],[1.2, 1.0],[0.0, 1.9]]

print(llyodAlgo(k, m, data))