file_a_name = "core-image-sato.manifest"
file_b_name = "rpilinux-image.manifest"

class ImageModules:
    def __init__(self, filename:str):
        self.modules = []
        self.filename = filename
        self.__read_modules()

    def __read_modules(self):
        with open(self.filename) as file:
            current_line = file.readline()
            while current_line != "":
                self.modules.append(current_line.removesuffix("\n"))
                current_line = file.readline()
            
    def print_modules(self):
        i = 1
        for module in self.modules:
            print(str(i) + ". " + module)
            i += 1


class CompareImages:
    def __init__(self):
        self.repeated_modules = []
        self.different_modules = []

    def compare(self, imageA:ImageModules, imageB:ImageModules):
        for module in imageA.modules:
            if module in imageB.modules:
                self.repeated_modules.append(module)
            else:
                self.different_modules.append(module)

    def print_repeated_modules(self):
        print("Repeated modules:")
        i = 1
        for module in self.repeated_modules:
            print(str(i) + ". " + module)
            i += 1

    def print_different_modules(self):
        print("Different modules:")
        i = 1
        for module in self.different_modules:
            print(str(i) + ". " + module)
            i += 1

    def print_comparison(self):
        self.print_different_modules()
        self.print_repeated_modules()

    def print_different_kernel_modules(self):
        print("Different kernel modules:")
        i = 1
        for module in self.different_modules:
            if "kernel-module" in module:
                print(str(i) + ". " + module)
                i += 1

image_a = ImageModules(file_a_name)
image_b = ImageModules(file_b_name)

comparison = CompareImages()
comparison.compare( image_a, image_b )
comparison.print_repeated_modules()
comparison.print_different_kernel_modules()