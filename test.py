from overloading import override , overload
# from overloading import *

class legal(override):
    def __init__(self , oi :str) -> None:
        self.oi = oi

    @overload
    def fun(self ,a : int):
        print("Sou inteiro")
    @overload
    def fun(self , a : float):
        print("Sou flutueiro")
    
    @overload
    def fun(self , a : str):
        print("Sou texto")

daora = legal("oi")
daora.fun("2.")