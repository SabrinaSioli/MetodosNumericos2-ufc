import cv2
import numpy as np
import math

blur = np.array([
    [1, 3, 1],
    [3,  5,  3],
    [1, 3, 1]
])

blur = blur / 16

laplacian3x3 = np.array([
    [1,4,1],
    [4,-20,4],
    [1,4,1]
])
laplacian3x3 = laplacian3x3 / 6

erro = 0.15

def convolucao3x3(img, conv, w, h, b):

    # Matriz nova
    convolved_img_1 = img.copy()

    for i in range(h):
        for j in range(w):
            masc = np.array([[0,0,0],[0,0,0],[0,0,0]])

            if i-1 < 0 and j-1 < 0:
                masc[0,0] = img[i,j][0]
            elif j-1 < 0 or i-1 < 0:
                masc[0,0] = img[i,j-1][0] if i-1 < 0 else img[i-1,j][0]
            else:
                masc[0,0] = img[i-1,j-1][0]

            masc[0,1] = img[i,j][0] if i-1 < 0 else img[i-1,j][0]

            if i-1 < 0 and j+1 == w:
                masc[0,2] = img[i,j][0]
            elif i-1 < 0 or j+1 == w:

                masc[0,2] = img[i,j+1][0] if i-1 < 0 else img[i-1,j][0]
            else:
                masc[0,2] = img[i-1,j+1][0]

            masc[1,0] = img[i,j][0] if j-1 < 0 else img[i,j-1][0]

            masc[1,1] = img[i,j][0]

            masc[1,2] = img[i,j][0] if j+1 == w else img[i,j+1][0]

            if i+1 == h and j-1 < 0:
                masc[2,0] = img[i,j][0]
            elif i+1 == h or j-1 < 0:
                masc[2,0] = img[i,j-1][0] if i+1 == h else img[i+1,j][0]
            else:
                masc[2,0] = img[i+1,j-1][0]

            masc[2,1] = img[i,j][0] if i+1 == h else img[i+1,j][0]

            if i+1 == h and j+1 == w:
                masc[2,2] = img[i,j][0]
            elif i+1 == h or j+1 == w:
                masc[2,2] = img[i,j-1][0] if i+1 == 0 else img[i-1,j][0]
            else:
                masc[2,2] = img[i+1,j+1][0]

            m = np.multiply(masc, conv)
            v = np.sum(m)
            v = min(255, v)
            l = np.sum(conv)
            v = v / l if b and l > 0 else v
            convolved_img_1[i, j] = v
            #convolved_img_2[i, j] = [0,0,0] if v < -erro or v > erro else [255,255,255]
            
    return convolved_img_1

def lap3x3(img, conv, w, h, b):

    # Matriz nova
    convolved_img_1 = img.copy()
    convolved_img_2 = img.copy()

    for i in range(h):
        for j in range(w):
            masc = np.array([[0,0,0],[0,0,0],[0,0,0]])

            if i-1 < 0 and j-1 < 0:
                masc[0,0] = img[i,j][0]
            elif j-1 < 0 or i-1 < 0:
                masc[0,0] = img[i,j-1][0] if i-1 < 0 else img[i-1,j][0]
            else:
                masc[0,0] = img[i-1,j-1][0]

            masc[0,1] = img[i,j][0] if i-1 < 0 else img[i-1,j][0]

            if i-1 < 0 and j+1 == w:
                masc[0,2] = img[i,j][0]
            elif i-1 < 0 or j+1 == w:

                masc[0,2] = img[i,j+1][0] if i-1 < 0 else img[i-1,j][0]
            else:
                masc[0,2] = img[i-1,j+1][0]

            masc[1,0] = img[i,j][0] if j-1 < 0 else img[i,j-1][0]

            masc[1,1] = img[i,j][0]

            masc[1,2] = img[i,j][0] if j+1 == w else img[i,j+1][0]

            if i+1 == h and j-1 < 0:
                masc[2,0] = img[i,j][0]
            elif i+1 == h or j-1 < 0:
                masc[2,0] = img[i,j-1][0] if i+1 == h else img[i+1,j][0]
            else:
                masc[2,0] = img[i+1,j-1][0]

            masc[2,1] = img[i,j][0] if i+1 == h else img[i+1,j][0]

            if i+1 == h and j+1 == w:
                masc[2,2] = img[i,j][0]
            elif i+1 == h or j+1 == w:
                masc[2,2] = img[i,j-1][0] if i+1 == 0 else img[i-1,j][0]
            else:
                masc[2,2] = img[i+1,j+1][0]

            m = np.multiply(masc, conv)
            v = np.sum(m)
            v = min(255, v)
            l = np.sum(conv)
            v = v / l if b and l > 0 else v
            convolved_img_1[i, j] = abs(v + 128)
            v = v / 100
            convolved_img_2[i, j] = [0,0,0] if v >= -erro and v <= erro else [255,255,255]
            
    return convolved_img_1, convolved_img_2

def label(img, t, w, h):
    cv2.rectangle(img, (0,int(7*h/8),int(w),int(h/8)), (0,0,0), -1)
    cv2.putText(img, t, (8,int(7*h/8)+22), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
    return img

# Leitura da imagem de entrada
img = cv2.imread('lena.png')

#w = 300
#h = 204

w = 256
h = 256

# Canal grayscale
for i in range(h):
    for j in range(w):
        m1 = sum(img[i,j])/3
        img[i,j] = [m1,m1,m1]

# Gaussiana
img2 = convolucao3x3(img, blur, w, h, True)

# Laplacian
img3, img4 = lap3x3(img2, laplacian3x3, w, h, False)

# Labeling
img = label(img, "P&B", w, h)
img2 = label(img2, "Gaussiana", w, h)
img3 = label(img3, "Laplacian 0-->128", w, h)
img4 = label(img4, "Threshold", w, h)

alg2 = np.concatenate((img, img2, img3, img4), axis=1)

data_u8 = alg2.astype('uint8')
cv2.imshow('Algoritmo 2: Laplace 3x3', cv2.resize(data_u8, (1024,256)))
 
cv2.waitKey(0)
cv2.destroyAllWindows()