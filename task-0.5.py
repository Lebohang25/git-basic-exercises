import math

def rectangle_area(rec1, rec2, rec3):
    
    s = 0.5 * (rec1 + rec2 + rec3)
    
    area = s * (s - rec1) * (s - rec2) * (s - rec3)
    
    print(math.sqrt(area))

rectangle_area( rec1, rec2, rec3)  
    
