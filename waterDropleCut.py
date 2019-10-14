import numpy
'''
水滴切割法
'''
class WaterCutting() :
    def __init__(self,x,y,pixel) :
        if  type(pixel) != numpy.ndarray :
            raise Exception("传入的参数不是列表")
        self.x = x
        self.y = y
        self.direct = 0
        self.pixel = pixel
        self.x_bound = (self.x - 2) if self.x > 2 else 0
        self.gravita = 0

    def __iter__(self) :
        return self

    def __next__(self) :
        m,n = 0,0
        self.gravita = self.getGravita()
        if self.gravita == 1 :
            m,n = self.x-1,self.y+1
            self.direct = 5
            self.x,self.y = self.x+1,self.y+1
        elif self.gravita == 2 :
            m,n = self.x,self.y+1
            self.direct = 0
            self.x,self.y = self.x,self.y+1
        elif self.gravita == 3 :
            m,n = self.x+1,self.y+1 
            self.direct = 4
            self.x,self.y = self.x+1,self.y+1 
        elif self.gravita == 4 and  self.direct==4 :
            m,n = self.x+1,self.y+1 
            self.direct = 4
            self.x,self.y = self.x+1,self.y+1
        elif self.gravita == 4 and self.direct==5  :
            m,n = self.x,self.y+1
            self.direct = 0
            self.x,self.y = self.x,self.y+1
        elif self.gravita ==4 and self.direct==0  :
            m,n = self.x+1,self.y
            self.direct = 4 
            self.x,self.y = self.x+1,self.y
        elif self.gravita == 5 :
            m,n = self.x-1,self.y
            self.direct = 5
            self.x,self.y = self.x-1,self.y
        elif self.gravita ==6 :
            m,n = self.x,self.y+1
            self.direct = 0
            self.x,self.y = self.x,self.y+1
        return m,n


    def getGravita(self) :
        x,y= int(self.x) ,int(self.y)
        poxil = self.pixel
        #max_g 当前点的势能，sum_g 周围点势能总和
        max_g,sum_g = 0,0

        #周围的点
        p_points = [(x,y),(x-1,y+1),(x,y+1),(x+1,y+1),(x+1,y),(x-1,y)]
        for index,item in enumerate(p_points)  :
            if (x-1) <= self.x_bound :
                max_g = 6
                
            if (y+1) >= len(self.pixel) :
                raise StopIteration()
            if (x+1) >=len(self.pixel[0]) :
                continue

            item_g = poxil[item[1]][item[0]]*index/255
            if max_g < item_g :
                max_g = item_g
            sum_g += poxil[int(item[1])][int(item[0])]*index/255
        
        if sum_g ==0 or sum_g ==15 :
            max_g  = 6
        return max_g 
            




'''
    x:横坐标 y:纵坐标，max_g：当前点的势能
    (x+1,y)  max_g=4
    (x-1,y) max_g = 5
    (x-1,y+1) max_g = 1
    (x+1,y+1) max_g = 3
    (x,y+1) max_g = 6 or 2
    (x+1,y+1) max_g = 4 and i=4
    (x,y+1) max_g = 4 and i=5
'''
def waterCutting(x,y,pixel,i) :
    max_g = getGravita(x,y,pixel)
    if max_g == 1 :
        return x-1,y+1
    elif max_g == 2 :
        return x,y+1
    elif max_g == 3 :
        return x+1,y+1  
    elif max_g == 4 and  i==4 :
        return x+1,y+1 
    elif max_g == 4 and i==5  :
        return x,y+1
    elif max_g == 4 :
        return x+1,y
    elif max_g ==6 :
        return x,y+1



def getGravita(x,y,poxil) :
    max_g = 0
    sum_g = 0
    #周围的点
    p_points = [(x,y),(x-1,y+1),(x,y+1),(x+1,y+1),(x+1,y),(x-1,y)]
    for index,item in enumerate(p_points)  :
        if item[0] >=84 : 
            max_g  =6 
        else  : 
            g = poxil[int(item[1])][int(item[0])]*index/255
            if max_g < g :
                max_g = g
            sum_g += poxil[int(item[1])][int(item[0])]*index/255
    if sum_g ==0 or sum_g ==15 :
        max_g  = 6
    return max_g 

__all__=["waterCutting"] 