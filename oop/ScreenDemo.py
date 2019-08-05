'''
    @property 属性的使用

'''
class Screen:

    def __init__(self,width,height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self,width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height


    @property
    def resolution(self):
        self.__resolution = self.width + self.height
        return self.__resolution

screen = Screen(10,20)
print(screen.height)

screen.height = 30
print(screen.height)

screen.resolution = 50  #不能对只读属性设置值
print(screen.resolution)



