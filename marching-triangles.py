// Um programador pretende implementar uma função para desenhar uma curva implícita definida pela equação f(x, y) = 5. Para ajudar este programador, você deve escrever o algoritmo Marching Triangles, assumindo que os valores x e y variam entre [− 2, 2] e a grade utilizada tem resolução 20 x 50.

from OpenGL.GL import *

def main():

// Inicializar a cena, tal como configurar luzes
GLvoid init(GLAutoDrawable drawable);

// Liberar recursos no contexto OpenGL
GLvoid dispose(GLAutoDrawable drawable);

// Inicializar o processo de rendering
GLvoid display(GLAutoDrawable drawable);

// Chamada que contém o viewport
GLvoid reshape(GLAutoDrawable drawable, -2, 2, 20, 50);

// Função de Escala
GLvoid glScalef(-2.0, 2.0, 5.0);

// Algoritmo Marching Tetrahedrons
GLvoid vMarchTetrahedron(GLvector*pasTetrahedronPosition, GLfloat*pafTetrahedronValue) {
    extern GLint aiTetrahedronEdgeFlags[16];
    extern GLint a2iTetrahedronTriangles[16][7];

    GLint iEdge, iVert0, iVert1, iEdgeFlags, iTriangle, iCorner, iVertex, iFlagIndex = 0;
    GLfloat fOffset, fInvOffset, fValue = 0.0;
    GLvector asEdgeVertex[6];
    GLvector asEdgeNorm[6];
    GLvector sColor;

    // Quais vértices estão dentro da superfície e quais fora
    for(iVertex = 0; iVertex < 4; iVertex++) {
        if(pafTetrahedronValue[iVertex] <= fTargetValue)
            iFlagIndex |= 1<<iVertex;
    }
    
    // Quais arestas são interceptadas pela superfície
    iEdgeFlags = aiTetrahedronEdgeFlags[iFlagIndex];

    // Não há interseções se o tetraedro está totalmente dentrou ou fora
    if(iEdgeFlags == 0)
        return;

    // Encontrar o ponto de intersecção da superfície com cada aresta
    for(iEdge = 0; iEdge < 6; iEdge++) {
        // se houver uma interseção nesta borda
        if(iEdgeFlags & (1<<iEdge)) {
            iVert0 = a2iTetrahedronEdgeConnection[iEdge][0];
            iVert1 = a2iTetrahedronEdgeConnection[iEdge][1];
            fOffset = fGetOffset(pafTetrahedronValue[iVert0], pafTetrahedronValue[iVert1], fTargetValue);
            fInvOffset = 1.0 - fOffset;
            
            asEdgeVertex[iEdge].fX = fInvOffset*pasTetrahedronPosition[iVert0].fX + fOffset*pasTetrahedronPosition[iVert1].fX;
            asEdgeVertex[iEdge].fY = fInvOffset*pasTetrahedronPosition[iVert0].fY + fOffset*pasTetrahedronPosition[iVert1].fY;
            asEdgeVertex[iEdge].fZ = fInvOffset*pasTetrahedronPosition[iVert0].fZ + fOffset*pasTetrahedronPosition[iVert1].fZ;

            vGetNormal(asEdgeNorm[iEdge], asEdgeVertex[iEdge].fX, asEdgeVertex[iEdge].fY, asEdgeVertex[iEdge].fZ);
        }
    }

    // Desenhar os triângulos que foram encontrados
    for(iTriangle = 0; iTriangle < 2; iTriangle++) {
        if(a2iTetrahedronTriangles[iFlagIndex][3*iTriangle] < 0)
            break;

        for(iCorner = 0; iCorner < 3; iCorner++) {
            iVertex = a2iTetrahedronTriangles[iFlagIndex][3*iTriangle+iCorner];
            vGetColor(sColor, asEdgeVertex[iVertex], asEdgeNorm[iVertex]);
            glColor3f(sColor.fX, sColor.fY, sColor.fZ);
            glNormal3f(asEdgeNorm[iVertex].fX, asEdgeNorm[iVertex].fY, asEdgeNorm[iVertex].fZ);
            glVertex3f(asEdgeVertex[iVertex].fX, asEdgeVertex[iVertex].fY, asEdgeVertex[iVertex].fZ);
        }
    }
}

if __name__ == "__main__":
    main()
