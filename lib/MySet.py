class MySet:

    def __init__(self, collection = []):
        self.dictionary = {}
        for value in collection:
            self.dictionary[value] = True

    def has(self, value):
        return value in self.dictionary
    
    def add(self, value):
        self.dictionary[value] = True
        return self.dictionary
    
    def delete(self, value):
        self.dictionary.pop(value, None)
        return self
    
    def size(self):
        return len(self.dictionary)
    
    def clear(self):
        self.dictionary.clear()
        return self.dictionary
    
    def __str__(self):
        return "MySet: {" + ','.join(f'{key}' for key in self.dictionary.keys()) + "}"
    

