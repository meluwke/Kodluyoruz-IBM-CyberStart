# -*- coding: utf-8 -*-
def euclideanDistance(point1,point2):
    x1,y1=point1
    x2,y2=point2
    x_diff=((x1-x2)**2)
    y_diff=((y1-y2)**2)
    distance=(x_diff + y_diff)**0.5
    return distance
def calculate_distances(points):
    distances=[]
    for i in range(len(points)-1): #ilk noktanın indeksini buluyor
        #for j in range(i+1,len(points)): #i'nin bir fazlasını yani bir sonraki noktanın indeksini buluyor
            distance=euclideanDistance(points[i], points[i+1])
            distances.append(distance)
            print (distance)
    return print(f"{min(distances)} en küçük aralık.")

def main():
    points = [(3, 4), (0, 0), (5, 12), (1,12)]
    calculate_distances(points)            
main()   



    
 