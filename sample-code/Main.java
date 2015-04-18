import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

public class Main {

    public static boolean hasPathToRec(Node start, Node end, Set<Node> visited) {
        if ( start.val.equals(end.val) ) {
            return true;
        }
        for ( Node n : getNeighbors(start)) {
            System.out.println(n.val);
            if ( ! visited.contains(n) ) {
                visited.add(n);
                if ( hasPathToRec(n, end, visited ) )
                    return true;
            }
        }
        return false;
    }

    public static ArrayList<Node> getNeighbors(Node n) {
        return n.neighbors;
    }

    public static void main(String[] args) {
        Node A = new Node("A");
        Node B = new Node("B");
        Node C = new Node("C");
        Node D = new Node("D");
        Node E = new Node("E");
        ArrayList<Node> an = new ArrayList<>();
        ArrayList<Node> bn = new ArrayList<>();
        ArrayList<Node> cn = new ArrayList<>();
        ArrayList<Node> dn = new ArrayList<>();
        ArrayList<Node> en = new ArrayList<>();

        an.add(B); an.add(C);
        bn.add(D);
        cn.add(E);

        A.neighbors = an;
        B.neighbors = bn;
        C.neighbors = cn;

        System.out.println(hasPathToRec(A, E, new HashSet<Node>()));

    }

}
