from overloading.overloading import overload,override

class yourClass(override):
    def __init__(self , yourArgs ) -> None:
        self.yourArgs = yourClass

    @overload
    def yourFunction(a :int ):
        print(f"I am a int {a}")
    
    @overload
    def yourFunction(a :int , b : float ):
        print(f"I am a int {a} and a float {b}")