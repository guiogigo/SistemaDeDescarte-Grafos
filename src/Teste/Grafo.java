package Teste;

import java.util.ArrayList;

public class Grafo<T> {
    private int nVertices;
    private ArrayList<Vertice<T>> vertices = new ArrayList<Vertice<T>>();

    public Grafo(int vertices, int[][] pesos) {
        this.nVertices = vertices;

        for(int v = 0; v<vertices; v++) {
            Vertice<T> vertice = new Vertice<T>(v);
            this.vertices.add(vertice);
        }

        for(int v=0; v<vertices; v++){
            for(int i=0; i<=v; i++) {
                if(pesos[i][v] > 0) {
                    Vertice<T> v1 = this.vertices.get(i);
                    Vertice<T> v2 = this.vertices.get(v);
                    v1.setVizinho(v2, pesos[i][v]);
                    v2.setVizinho(v1, pesos[i][v]);
                }
            }
        }
    }

    public void BuscaLargura() {
        int[] marca = new int[this.nVertices];
        for(int i=0; i<this.nVertices; i++) {
            marca[i] = 0;
        }
        marca[0] = 1;
        ArrayList<Vertice<T>> F = new ArrayList<Vertice<T>>();
        F.add(this.vertices.get(0));
        while(F.size() != 0) {
            Vertice<T> u = F.removeFirst();
            ArrayList<Aresta<T>> w = u.getVizinhos();
            while(w.size() != 0) {
                Vertice<T> v = w.removeFirst().getVertice();
                if(marca[v.getDado()] == 0) {
                    marca[v.getDado()] = 1;
                    F.add(v);
                }
            }
            marca[u.getDado()] = 2;
            u.exibir();
        }
    }

    public void BuscaProfundidade(int v) {
        int[] marca = new int[this.nVertices];
        for(int i=0; i<this.nVertices; i++) {
            marca[i] = 0;
        }
        marca[v] = 1;
        Vertice<T> w = this.vertices.get(v);
        VisitaProfundidade(w, marca);
    }

    private void VisitaProfundidade(Vertice<T> v, int[] m) {
        ArrayList<Vertice<T>> P = new ArrayList<Vertice<T>>();
        P.add(v);
        Vertice<T> u = v.getVizinhos().removeFirst().getVertice();
        while(u != null) {
            if(m[u.getDado()] == 0) {
                m[u.getDado()] = 1;
                VisitaProfundidade(u, m);
            }
            u = u.getVizinhos().removeFirst().getVertice();
            if(m[u.getDado()] == 1) {
                u = null;
            }
        }
        m[v.getDado()] = 2;
        v.exibir();
        P.removeLast();
    }
}
