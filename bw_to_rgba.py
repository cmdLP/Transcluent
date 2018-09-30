 ###
##
##  Copyright cmdlp
##
##  LICENSE: You are allowed to include this code in your product, but you need to refer to this repository.
##
##  Convert two images with black and white background to RGBA image.
##
 ###

 
from PIL import Image


def bw_to_rgba(black_img : Image.Image, white_img : Image.Image) -> Image.Image:

    black_img = black_img.convert("RGB")
    white_img = white_img.convert("RGB")

    result_img = Image.new("RGBA", black_img.size)

    black  = black_img.load()
    white  = white_img.load()
    result = result_img.load()

    range_y = range(black_img.height)
    range_x = range(black_img.width)

    for y in range_y:
        for x in range_x:
            black_pix = black[x, y]
            white_pix = white[x, y]
            
            a = 255 - sum(map(lambda b, w: w-b, black_pix, white_pix)) / 3

            if a <= 0:
                a = 0
                r = 0
                g = 0
                b = 0
            else:
                r = black_pix[0] / a * 255
                g = black_pix[1] / a * 255
                b = black_pix[2] / a * 255
            
            result[x, y] = tuple(map(int, (r, g, b, a)))
            
    return result_img

    
    
if __name__ == "__main__":
    from sys import argv

    if len(argv) == 1:
        num = "1"
        argv += ["test-images/"+num+"-black.png", "test-images/"+num+"-white.png", "test-images/"+num+"-rgb.png"]
    elif argv != 4:
        print(
            "USAGE: black_white_to_rgba.py <black-image> <white-image> <output-image>\n"
            "\n"
            "It converts two images with black and white background to an rgba-image"
        )
            
        exit(1)

    black_file_name  = argv[1]
    white_file_name  = argv[2]
    output_file_name = argv[3]

    black_img  = Image.open(black_file_name).convert("RGB")
    white_img  = Image.open(white_file_name).convert("RGB")

    result_img = bw_to_rgba(black_img, white_img)
    
    result_img.save(output_file_name)

