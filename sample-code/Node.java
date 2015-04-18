import java.util.ArrayList;

/**
 * Created by christophersprague on 4/17/15.
 */
public class Node {
    public String val;
    public ArrayList<Node> neighbors;
    public Node(String val){
        this.val = val;
        this.neighbors = new ArrayList<>();
    }
    public Node(String val, ArrayList<Node> neighbors){
        this.val = val;
        this.neighbors = neighbors;
    }
}
