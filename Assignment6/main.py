def distance(point1, point2, m):
    return sum((point1[i] - point2[i]) ** 2 for i in range(m))

def kmeans(k, m, data):
    centers = [data[i] for i in range(k)]
    sizes = float("inf")
    while sizes > 0:
        new_centers = centerCluster(k, m, data, centers)
        sizes = sum([distance(new_centers[i], centers[i], m) for i in range(k)])
        centers = new_centers[:]
    return centers

def centerCluster(k, m, data, center):
    def nearest(p):
        index = -1
        best = float('inf')
        for i in range(k):
            dist = distance(p, center[i], m)
            if dist < best:
                index = i
                best = dist
        return index

    def centers(i, index):
        count = 0
        point = [0 for j in range(m)]
        for j in range(len(data)):
            if index[j] == i:
                count += 1
                for l in range(m):
                    point[l] += data[j][l]
        return [p / max(count, 1) for p in point]

    index = [nearest(p) for p in data]
    return [centers(i, index) for i in range(k)]

k = 2
m = 2
data = [[2, 2],[1.3, 1.1],[1.3, 0.2],[0.6, 2.8],
[3.0, 3.2],[1.2, 0.7],[1.4, 1.6],[1.2, 1.0],
[1.2, 1.1],[0.6, 1.5],[1.8, 2.6],[1.2, 1.3],[1.2, 1.0],[0.0, 1.9]]
print(kmeans(k,m, data))