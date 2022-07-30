def flipAndInvertImage(image):
    return [[ 1- x[y] for y in range(len(x)-1,-1,-1)] for x in image]
 

print(flipAndInvertImage(image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))
