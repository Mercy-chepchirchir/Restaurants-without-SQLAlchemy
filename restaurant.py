class Restaurant:
    def __init__(self,name=None):
        self._name = None
        if name is not None:
            self.set_name(name)
        
    def set_name (self,name):
        if isinstance (name,str):
            self._name = name
  
        
        