import Teste.Grafo;

public class App {
    public static void main(String[] args) throws Exception {
           
        /*int[][] matriz = new int[7][7];
        matriz[0][0] = 0; 
        matriz[0][1] = 3; 
        matriz[0][2] = 2; 
        matriz[0][3] = 0; 
        matriz[1][0] = 3; 
        matriz[1][1] = 0; 
        matriz[1][2] = 0; 
        matriz[1][3] = 4; 
        matriz[2][0] = 2; 
        matriz[2][1] = 0; 
        matriz[2][2] = 0; 
        matriz[2][3] = 0; 
        matriz[3][0] = 0; 
        matriz[3][1] = 4; 
        matriz[3][2] = 0; 
        matriz[3][3] = 0; */

        int[][] matriz = new int[7][7];

        // Atribuindo valores específicos
        matriz[0][1] = 2;
        matriz[0][4] = 5;
        matriz[0][3] = 3;
        matriz[1][0] = 2;
        matriz[1][5] = 5;
        matriz[1][2] = 10;
        matriz[2][1] = 10;
        matriz[2][6] = 1;
        matriz[3][0] = 3;
        matriz[4][0] = 5;
        matriz[4][5] = 7;
        matriz[6][4] = 7;
        matriz[6][1] = 5;

        Grafo<String> g = new Grafo<String>(7, matriz);
        g.BuscaProfundidade(0);
        //System.out.println(new Vertice<String>("Ola").getTeste());
    }
}
