import java.util.ArrayList;
import java.util.Collection;

public class UFO{
    private Collection<Probable> toProbe;
    private int aggression;

    public UFO(int agg){
        toProbe = new ArrayList<Probable>();
        aggression = agg;
    }

    public void probeEverything(){
        for( Probable p : toProbe ){
            p.probe();
        }
    }

    public void sendHome(){
        for( Probable p: toProbe ){
            p.returnHome();
        }
    }

    public void abduct(Collection<Probable> potentialAbductees){
        for( Probable p : potentialAbductees ){
            if( p.getMentalResolve() < aggression){
                toProbe.add(p);
            }
        }
    }

    public static void main(String[] args){
        UFO ufo = new UFO(1199999999);	
        ArrayList<Probable> field = new ArrayList<Probable>();

        field.add(new Cow("Bessie"));
        //10 = mentalResolve
        Human cleatus = new RedNeck("Cleatus", 10);
        
        // 50 == mentalResolve and 100 == academicRespect
        Human brown = new Professor("Brown", 50, 100);         
        
        field.add(cleatus);
        field.add(brown);

        ufo.abduct(field);
        ufo.probeEverything();
        ufo.sendHome();
    }
}
