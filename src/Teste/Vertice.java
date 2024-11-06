package Teste;

import java.util.ArrayList;

public class Vertice<T> {
    private int dado;
    private ArrayList<Aresta<T>> vizinhos = new ArrayList<Aresta<T>>();

    public Vertice(int dado) {
        this.dado = dado;
    }

    public void setVizinho(Vertice<T> vizinho, double peso) {
        this.vizinhos.add(new Aresta<>(vizinho, peso));
    }

    public void setVizinho(ArrayList<Aresta<T>> vizinhos) {
        this.vizinhos = vizinhos;
    }

    public ArrayList<Aresta<T>> getVizinhos() {
        return new ArrayList<Aresta<T>>(vizinhos);
    }

    public int getDado() {
        return dado;
    }

    public void exibir() {
        System.out.print("Vertice: " + this.dado + " Vizinhos: ");
        for (Aresta<T> aresta : vizinhos) {
            System.out.print("(" + aresta.getVertice().getDado() + "," + aresta.getPeso() + ") ");
        }
        System.out.print("\n");
    }
}
