class Client:
    def __init__(self, n, fone):
        
        self._name = n
        self._telephone = fone

    #method get
    def get_name(self):
        return self._name

    #method set
    def set_name(self, name):
        self._name = name