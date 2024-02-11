class Image:
    def __init__(self, resolution, title, extention):
        self.resolution = resolution
        self.title = title
        self.extention = extention
    def resize_(self, new_size):
        self.resolution = new_size
    def __str__(self):
        return f"{self.resolution}, {self.title}, {self.extention}"
        
exaple = Image("1920X1800", "picture", "png")
print(exaple.resolution)

exaple.resize_("800X600")
print(exaple.resolution)

print(exaple)