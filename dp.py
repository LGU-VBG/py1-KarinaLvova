class Image:
    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self, new_resolution):
        self.resolution = new_resolution
        print(f"Изображение '{self.title}' изменило разрешение на {self.resolution}")


image1 = Image("1920x1080", "Sunset", "jpg")
image2 = Image("1280x720", "Sunrise", "png")

image1.resize("2560x1440")
image2.resize("1920x1080")