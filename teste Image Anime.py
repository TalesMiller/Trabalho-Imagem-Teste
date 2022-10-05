import cv2
from cv2 import waitKey
from cv2 import imshow

path = "C:/Users/tales/Desktop/Facul/Teste Codigo/Anime/"

a = cv2.imread(path + "img_aluno.jpg")

#cv2.imshow("imagem 1", a)

b = cv2.imread(path + "img_aluno2.jpg")

#imshow("imagem 2", b)

a3 = a + b
#imshow("Imagem 1 + Imagem 2", a3)

a4 = a - b
#imshow("Imagem 1 - Imagem 2", a4)

a5 = b - a
#imshow("Imagem 2 - Imagem 1", a5)

#imshow("(Imagem 1 - Imagem 2)-(Imagem 1 + Imagem 2)", a4 - a3)
#imshow("(Imagem 1 + Imagem 2)-(Imagem 1 - Imagem 2)", a3 - a4)

#imshow("(Imagem 2 - Imagem 1)-(Imagem 1 + Imagem 2)", a5 - a3)
#imshow("(Imagem 1 + Imagem 2)-(Imagem 2 - Imagem 1)", a3 - a5)

#imshow("(Imagem 1 - Imagem 2)-(Imagem 2 - Imagem 1)", a4 - a5)
#imshow("(Imagem 2 - Imagem 1)-(Imagem 1 - Imagem 2)", a5 - a4) 

#imshow("(Imagem 1 + Imagem 2)+(Imagem 1 - Imagem 2)", a3 + a4)
#imshow("(Imagem 1 + Imagem 2)+(Imagem 2 - Imagem 1)", a3 + a5)
#imshow("(Imagem 1 - Imagem 2)+(Imagem 2 - Imagem 1)", a4 + a5)

c = cv2.imread(path + "img_aluno.jpg")

height = int(c.shape[0]) #pega a altura
width = int(c.shape[1]) #pega a largura

for i in range(0,height):
    for j in range(0,width):
        c[i, j] = (255,255,255) # mudar todos os pixels para branco (e)

#imshow("Imagem 1 invertida", c - a)
#imshow("Imagem 2 invertida", c - b)

waitKey(0)