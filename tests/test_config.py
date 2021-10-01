import  pytest
class NotInRange(Exception):
    def __init__(self, message = 'Value out of range'):
#         self.input = input_
        self.message = message
        super().__init__(self.message)

def test_geneirc():
    a =  5
    with pytest.raises(NotInRange):
        if a not in range(10,20):
            raise NotInRange
