import os
import cv2
import potrace

# from potrace import Bitmap
from PIL import Image, ImageFilter
import numpy as np

imagesDir = os.path.join(os.path.dirname(__file__), "../images")


def imagePath(fileName: str):
    return os.path.join(imagesDir, fileName)


def sketcher1(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # canny = cv2.Canny(blur, 50, 50)
    # ret, mask = cv2.threshold(canny, 70, 255, cv2.THRESH_BINARY)

    # (thresh, blackAndWhiteImage) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    (thresh, blackAndWhiteImage) = cv2.threshold(blur, 70, 255, cv2.THRESH_BINARY)
    return blackAndWhiteImage


def sketcher2(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    invertedGray = 255 - gray
    blur = cv2.GaussianBlur(invertedGray, (31, 31), 0)
    sketch = cv2.divide(gray, blur, scale=256.0)

    canny = cv2.Canny(sketch, 10, 70)

    (thresh, blackAndWhiteImage) = cv2.threshold(canny, 128, 255, cv2.THRESH_BINARY)
    return sketch


def sketcher3(img):
    # convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # blur
    blur = cv2.GaussianBlur(gray, (21, 21), sigmaX=33, sigmaY=33)

    # divide
    divide = cv2.divide(gray, blur, scale=255)

    # otsu threshold
    thresh = cv2.threshold(divide, 128, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # apply morphology
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    canny = cv2.Canny(morph, 100, 100)
    ret, mask = cv2.threshold(canny, 70, 255, cv2.THRESH_BINARY)

    # (thresh, blackAndWhiteImage) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    (thresh, blackAndWhiteImage) = cv2.threshold(mask, 70, 255, cv2.THRESH_BINARY)
    return blackAndWhiteImage


def sketcher4(img_path):
    from scipy.spatial.distance import pdist, squareform
    from tsp_solver.greedy_numpy import solve_tsp

    original_image = Image.open(img_path)
    bw_image = original_image.convert("1", dither=Image.NONE)

    bw_image_array = np.array(bw_image, dtype=np.int)
    black_indices = np.argwhere(bw_image_array == 0)
    # Changing "size" to a larger value makes this algorithm take longer,
    # but provides more granularity to the portrait
    chosen_black_indices = black_indices[
        np.random.choice(black_indices.shape[0], replace=False, size=10000)
    ]

    distances = pdist(chosen_black_indices)
    distance_matrix = squareform(distances)

    optimized_path = solve_tsp(distance_matrix)

    optimized_path_points = [chosen_black_indices[x] for x in optimized_path]

    data_arr_arr = []
    data_dict_arr = []
    for i in optimized_path_points:
        data_arr_arr.append([i[0], i[1]])
        data_dict_arr.append({"x": i[0], "y": i[1]})

    with open("arr_arr_4.txt", "w") as f:
        f.write("let P=" + str(data_arr_arr))

    with open("dict_arr_4.txt", "w") as f:
        f.write("let drawing =" + str(data_dict_arr))


def saveImg(img, fileName):
    img_numpy = img
    img_pil = Image.fromarray(img_numpy)
    file_out = fileName
    img_pil.save(file_out)
    os.system("potrace {0} --svg -o my.svg".format(fileName))


def imgTrace(img):
    bitmap = potrace.Bitmap(img)
    # potrace.TURNPOLICY_BLACK
    # potrace.TURNPOLICY_WHITE
    # potrace.TURNPOLICY_LEFT
    # potrace.TURNPOLICY_RIGHT
    # potrace.TURNPOLICY_MINORITY
    # potrace.TURNPOLICY_MAJORITY
    # potrace.TURNPOLICY_RANDOM
    path = bitmap.trace(
        turdsize=10,
        turnpolicy=potrace.POTRACE_TURNPOLICY_WHITE,
        alphamax=1.0,
        opticurve=0,
        opttolerance=0.2,
    )
    allPathsArr = []
    allPathsDict = []
    for i in path:
        print("i :", i.start_point.x, i.start_point.y)
        allPathsArr.append([i.start_point.x, i.start_point.y])
        allPathsDict.append({"x": i.start_point.x, "y": i.start_point.y})
        for j in i:
            allPathsArr.append([j.end_point.x, j.end_point.y])
            allPathsDict.append({"x": j.end_point.x, "y": j.end_point.y})

    with open("allPaths_arr.txt", "w") as f:
        f.write("let P=" + str(allPathsArr))
    with open("allPaths_dict.txt", "w") as f:
        f.write("let drawing=" + str(allPathsDict))

# cv2.imshow('image', img)
# cv2.imshow('sketch image',edges)
# cv2.imshow('black and white',blackAndWhiteImage)
# # cv2.imshow('sketch image',img_bitmap)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

if __name__ == "__main__":

    imgName = "image.png"
    # load image
    filePath = imagePath(imgName)
    img = cv2.imread(filePath)

    # sketch2 = sketcher2(img)
    # saveImg(sketch2, "out2.bmp")
    # imgTrace(sketch2)

    sketch1 = sketcher2(img)
    saveImg(sketch1, "out1.bmp")
    imgTrace(sketch1)

    # sketcher4(filePath)

    # sketch2 = sket
