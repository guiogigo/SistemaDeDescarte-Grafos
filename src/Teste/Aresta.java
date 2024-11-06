package Teste;

public class Aresta<T> {
    private Double peso;
    private Vertice<T> vertice;

    public Aresta(Vertice<T> vertice, Double peso) {
        this.peso = peso;
        this.vertice = vertice;
    }

    public Vertice<T> getVertice() {
        return vertice;
    }

    public Double getPeso() {
        return peso;
    }
}
