#!/usr/bin/python3
#!/usr/bin/python3
"""This is a basic training module designed to teach us how to use classes

"""


class Square:
    """This is a class for a square

    We have a basic init function

    Note:
        Do not include the self parameter

    Args:
       size (int): The first parameter
    """
    def __init__(self, size=0, position=(0,0)):
        self.size = size
        self.position = position
            
    def area(self):
        return self._Square__size*self._Square__size

    @property
    def size(self):
        return self._Square__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self._Square__size = value

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(self._Square__size):
                for y in range(self._Square__position[0]):
                    print("_",end="")
                for x in range(self._Square__size):
                    print("#", end="")
                print()

    @property
    def position(self):
        return self._Square__position
    
    @position.setter
    def position(self, value):
        if not value == (0, 0):
            try:
                x = len(value)
                is_0_pos_int = isinstance(value[0], int) and value[0] >= 0
                is_1_pos_int = isinstance(value[1], int) and value[1] >= 0
                if isinstance(value, tuple) and x == 2 and is_0_pos_int == True and is_1_pos_int == True:
                    self._Square__position = value
            except TypeError:
                raise TypeError("position must be a tuple of 2 positive integers")
        elif value == (0, 0):
            self._Square__position = (0, 0)
