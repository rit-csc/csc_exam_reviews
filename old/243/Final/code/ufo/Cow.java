public class Cow implements Probable{
    private String name;

    public Cow(String name){
        this.name = name;
    }

    public int getMentalResolve(){
        return 10;
    }

    public void probe(){
       System.out.println("moo.");
    }

    public void returnHome(){
        System.out.println(name + " is unimpressed.");
    }
}
