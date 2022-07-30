def countGoodRectangles(rectangles):
    lst = [min(rec) for rec in rectangles]
    m = max(lst)
    return lst.count(m)

print(countGoodRectangles(rectangles = [[2,3],[3,7],[4,3],[3,7]]))