from abc import ABC,abstractmethod
class shape(ABC):
    def __init__(self,perimeter=None,area=None,volume=None, **kwargs):
        self.volume=volume
        self.perimeter=perimeter
        self.area=area
        #Encapsulation
        self._name=None
    
    def Area(self, **kwargs):
        pass
    
    def Volume(self,**kwargs):
        pass
    
    def Perimeter(self,**kwargs):
        pass
    
    def __str__(self):
        return f'this is a shape with the area of {self.area} and volume of {self.volume} and perimeter of {self.perimeter}'
    
    def display(self):
        for key, value in vars(self).items():
            print(f'{key} : {value}')
   
    def __call__(self, **kwargs):
        pass

    @abstractmethod   
    def get_name(self,**kwargs):
        self._name=input('please enter your shape name: ')
        print(f'yor shapes name is {self._name}')
class three_d(shape):
    def __init__(self,side_area=None,total_area=None,**kwargs):
        super().__init__()
        self._side_area=side_area
        self._total_area=total_area

    def get_name(self):
        super().get_name()
        print('and this is a 3d shape')
        
    def side_area(self,**kwargs):
        print(f'your side area is {self._side_area}')
    
    def total_area(self,**kwargs):
        
        print(f'your total area is {self._total_area}')
    def Volume(self,**kwargs):
        pass
        
    def Perimeter(self,**kwargs):
        print('its 3d shape and dosent have perimeter')
    