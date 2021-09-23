from PIL import Image

def tiff_to_png( src, dst ):
    im = Image.open(src)
    str = dst.__str__() +".png"
    im.mode = 'I'
    im.point(lambda i:i*(1./1)).convert('L').save(str)

def main():
    tiff_to_png("1.tiff", "1")

if __name__ == "__main__":
    main()
