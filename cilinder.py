// Utilizando a representação paramétrica, escreva um algoritmo para gerar uma triangulação para um cilindro de altura 2,
// cuja base é um círculo de raio 3 posicionado na origem do plano XY

from OpenGL.GL import *

def main():

// limpa os pixels
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

// triângulo superior
glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0.0, 2.0, 0.0)
    for(i=0; i<=2*Pi; i+=resolution)
        glVertex3f(3.0*cos(i), 2.0, 3.0*sin(i))
glEnd()

// triângulo da base
glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0.0, 0.0, 0.0)
    for(i=2*Pi; i>=0; i-=resolution)
        glVertex3f(3.0*cos(i), 0.0, 3.0*sin(i))
    glVertex3f(3.0, 2.0, 0.0)
glEnd()

// estrutura do cilindro
glBegin(GL_QUAD_STRIP)
    for(i=0; i<=2*Pi; i+=resolution){
        glVertex3f(3.0*cos(i), 0.0, 3.0*sin(i))
        glVertex3f(3.0*cos(i), 2.0, 3.0*sin(i))
    }
    // volta ao grau zero
    glVertex3f(3.0, 0.0, 0.0)
    glVertex3f(3.0, 2.0, 0.0)
glEnd()
glFlush()


if __name__ == "__main__":
    main()
