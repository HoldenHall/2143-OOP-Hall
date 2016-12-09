class ImageEd(object):
    def __init__(self,img):
        self.width = img.size[0]
        self.height = img.size[1]
        self.img = Image.open(file)

    def glass_filter(self,image,distance,imageout=None):
        for x in range(self.width):
            for y in range(self.height):
                rgb = img.getpixel((x,y))
        
                xnums = [x for x in range(x - distance, x + distance) if x >= 0]
                ynums = [y for y in range(y - distance, y + distance) if y >= 0]

                x_choice = random.choice(xnums)
                y_choice = random.choice(ynums)

                if x > self.width-distance:
                    break
                if y > self.height-distance:
                    break
                rgb2 = img.getpixel((x_choice,y_choice))
                rgb = (rgb2[0],rgb2[1],rgb[2])
                img.putpixel((x,y),rgb2)
        img.save(imageout)   


    def v_flip(self,image,imageout=None):
        for x in range(self.height//2):
            for y in range(self.width):
                rgb = img.getpixel((y,x))
                rgb2 = img.getpixel((y,self.height-1-x))
                img.putpixel((y,height-1-x),rgb)
                img.putpixel((y,x),rgb2)
        img.save(imageout)   



    def h_flip(self,image,imageout=None):
        for x in range(self.height):
            for y in range(self.width//2):
                rgb = img.getpixel((y, x))
                rgb2 = img.getpixel((width - 1 - y, x))
                img.putpixel((width - 1 - y, x), rgb)
                img.putpixel((y, x), rbg2)
        img.save(imageout)   


        
    def posterize(self,image,snap_val,imageout=None):
        class posterize(object):
            
            def __snap_color__(self,color,snap_val):
                color = int(color)
                m = color % snap_val
                if m < (snap_val // 2):
                    color -= m
                else:
                    color += (snap_val - m)

            return int(color)
        p1 = posterize()
        for x in range(self.width):
            for y in range(self.height):
                current = img.getpixel((x, y))
                r = p1.__snap_color__(current[0],snap_val)
                g = p1.__snap_color__(current[1],snap_val)
                b = p1.__snap_color__(current[2],snap_val)

                rbg = ((r,g,b))
                img.putpixel((x, y), rgb)
        img.save(imageout)
    
    def blur(self,image,kernel,imageout=None):
        class average(object):
            def average(self,c1,c2,c3,c4,c5):
                average = c1+c2+c3+c4+c5 /5
                return int(average)
        avg = average()

        for x in range(self.width):
            for y in range(self.height):
                current = img.getpixel((x, y))

                if x > self.width-kernel-1 or x < (kernel-1)-self.width:
                    continue
                if y > self.height-kernel-1 or y < (kernel-1)-self.height:
                    continue
                left = img.getpixel((x-kernal,y))
                right = img.getpixel((x+kernal,y))
                above = img.getpixel((x,y-kernal))
                below = img.getpixel((x,y+kernal))
                r= avg.average(current[0],left[0],right[0],above[0],below[0])
                g= avg.average(current[1],left[1],right[1],above[1],below[1])
                b= avg.average(current[2],left[2],right[2],above[2],below[2])

                rgb = ((r,g,b))
                img.putpixel((x, y), rgb)
        img.save(imageout)
        
    def solarize(self,image,intensity,imageout=None):
        class solarize(object):
            def solar(self,color,intensity):
                color = int(color)
                if color < intensity:
                    color = 255-color
                return int(color)
        s1 = solarize()
        for x in range(self.width):
            for y in range(self.height):
                current = img.getpixel((x, y))

                r = s1.solar(current[0],intensity)
                g = s1.solar(current[1],intensity)
                b = s1.solar(current[2],intensity)
                rgb = ((r,g,b))
                img.putpixel((x, y), rgb)
        img.save(imageout)   

        
    def warhol(self,image,intensity,imageout=None):
        class warhol(object):
            def color_set(self,r,b,g):
                if r < 100:
                    r = 66
                    g = 28
                    b = 82

                elif g < 100:
                    r = 115
                    g = 44
                    b = 123

                elif g < 140:
                    r = 156
                    g = 138
                    b = 168

                elif g < 170:
                    r = 189
                    g = 174
                    b - 198

                else:
                    r = 255
                    g = 255
                    b = 255
            return ((r,g,b))
        war = warhol()
        for x in range(self.width):
            for y in range(self.height):
                current = img.getpixel((x, y))
        
                r = self.posterize__snap_color__(current[0],intensity)
                g = self.posterize.__snap_color__(current[1],intensity)
                b = self.posterize.__snap_color__(current[2],intensity)
                rgb = war.color_set(r,g,b)
                img.putpixel((x, y), rgb)
        img.save(imageout)   
