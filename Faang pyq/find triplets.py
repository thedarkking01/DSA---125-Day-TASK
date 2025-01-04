def findtriplets(arr):
    n = len(arr)
    triplets = []
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    triplets.append([arr[i], arr[j], arr[k]])
    return triplets
arr=[0,-1,2,-3,1]
triplets=findtriplets(arr)
for triple in triplets:
    print(triple)