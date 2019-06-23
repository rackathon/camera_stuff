import numpy as np

from PIL import Image

def finalize(vertical, horizontal):
    h,w = vertical.shape

    new_img = np.zeros((h, w))

    for x in range(w):
        for y in range(h):
            new_img[y, x] = np.sqrt(vertical[y,x]**2 + horizontal[y,x]**2)
    return new_img



def convolve(img, kernel):
    imh, imw = img.shape
    kerh, kerw = kernel.shape

    new_img = np.zeros((imh, imw))

    for x in range(imw - kerw + 1):
        for y in range(imh - kerh + 1):
            slice = get_slice(img, x, y, kerw, kerh)
            #print(x,y)
            prod = np.multiply(slice, kernel)
            avg = np.average(prod)
            new_img[y + 1, x + 1] = avg
    return new_img

def get_slice(img, x, y, width, height):
    return img[y:y+height, x:x+width]


if __name__ == "__main__":
    sobel = np.array([[-1,0,1], [-1,0,1], [-1,0,1]])
    sobelT = np.transpose(sobel)
    im = Image.open("../../data/images/jet.png").convert("L")

    arr = np.array(im)
    vertical = convolve(arr, sobel)*10
    horizontal = convolve(arr, sobelT)*10
    edges = finalize(vertical, horizontal)
    vimg = Image.fromarray(vertical)
    himg = Image.fromarray(horizontal)
    final = Image.fromarray(edges)
    vimg.show()
    himg.show()
    final.show()