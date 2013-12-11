public abstract class Human implements Probable{
    private int mentalResolve;
    private String name;

    public Human(String nm, int res){
        name = nm;
        mentalResolve = res;
    }

    public abstract void probe();

    public abstract void returnHome();

    public String getName(){
        return name;
    }

    public int getMentalResolve(){
        return mentalResolve;
    }
}
