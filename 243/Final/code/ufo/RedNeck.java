public class RedNeck extends Human{
    public RedNeck(String nm, int res){
        super(nm, res);
    }

    public void probe(){
        System.out.println("\"Wut y'all doin wit dat der deevise?\", "
                                           + "inquires " + getName() );
        System.out.println("\"GAAAAH!!\", exlaims "+ getName() );
    }

    public void returnHome(){
        beGuestOnJerrySpringerToTalkAboutTheProbing();
    }

    public void beGuestOnJerrySpringerToTalkAboutTheProbing(){
        System.out.println("I's tellin ya Jerry!");
    }

}
