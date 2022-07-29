import cv2
import numpy as np
import math

blur = np.array([
    [1, 3, 1],
    [3,  5,  3],
    [1, 3, 1]
])

blur = blur / 16

sobel3x3_x = np.array([
    [-1,0,1],
    [-2,0,2],
    [-1,0,1]
])
sobel3x3_x = sobel3x3_x

sobel3x3_y = np.array([
    [1,2,1],
    [0,0,0],
    [-1,-2,-1]
])
sobel3x3_y = sobel3x3_y

def convolucao3x3(img, conv, w, h, b):

    # Matriz nova
    convolved_img = img.copy()

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
            v = min(255, abs(v))
            convolved_img[i, j] = v
            
            
    return convolved_img

def gradiente(gx, gy, w, h):
    # Matriz nova
    final = np.zeros(shape=(h, w, 3))

    for i in range(h):
        for j in range(w):
            c = math.sqrt(gx[i,j][0]**2 + gy[i,j][0]**2)
            c = min(255, int(c))
            final[i,j] = [c,c,c]
    return final

def threshold(g, t):

    final = g.copy()

    for i in range(h):
        for j in range(w):
            final[i,j] = [0,0,0] if final[i,j][0] < t else [255,255,255]

    return final

def label(img, t, w, h):
    cv2.putText(img, t, (8,int(7*h/8)+22), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

# Leitura da imagem de entrada
img = cv2.imread('lena.png')

h,w,_ = img.shape

# Canal grayscale
for i in range(h):
    for j in range(w):
        m1 = sum(img[i,j])/3
        img[i,j] = [m1,m1,m1]

# Gaussiana
img2 = convolucao3x3(img, blur, w, h, True)

# Sobel X
img3 = convolucao3x3(img2, sobel3x3_x, w, h, False)

# Sobel Y
img4 = convolucao3x3(img2, sobel3x3_y, w, h, False)

# Sobel Final
img5 = gradiente(img3, img4, w, h)

# Threshold
th = 150
img6 = threshold(img5, th)

# Labeling
label(img, "P&B", w, h)
label(img2, "Gaussiana", w, h)
label(img3, "Sobel X", w, h)
label(img4, "Sobel Y", w, h)
label(img5, "Sobel X e Y", w, h)
label(img6, "Threshold", w, h)

alg1 = np.concatenate((np.concatenate( (img, img2, img3), axis=1), np.concatenate( (img4, img5, img6), axis=1)), axis=0)

data_u8 = alg1.astype('uint8')
cv2.imshow('Algoritmo 1: Sobel 3x3', cv2.resize(data_u8, (w*3,h*2)))
 
cv2.waitKey(0)
cv2.destroyAllWindows()