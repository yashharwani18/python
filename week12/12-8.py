class String:
    def __init__(self, content):
        self.content = str(content)

    def __iadd__(self, other):
        if isinstance(other, String):
            self.content += other.content
        elif isinstance(other, str):
            self.content += other
        return self

    def toLower(self):
        self.content = self.content.lower()

    def toUpper(self):
        self.content = self.content.upper()

    def __str__(self):
        return self.content

s1 = String("Hello")
s2 = String(" World")

s1 += s2
print("Concatenated:", s1)  
s1.toLower()
print("Lowercase:", s1)  
s1.toUpper()
print("Uppercase:", s1)    
