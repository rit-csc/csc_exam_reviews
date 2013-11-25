public class Professor extends Human{
    private int academicRespect;

    public Professor(String name, int mental, int resp){
        super(name, mental);
        academicRespect = resp;
    }

    public void probe(){
        System.out.println("\"What an exhilarating day for mankind!\", "
                                  + "shouts Prof. " + getName());
        System.out.println("\"Oh my!\", exclaims Prof. " + getName());
    }

    public void returnHome(){
        adjustAcademicCareerToFocusOnAbductions();
    }

    public void adjustAcademicCareerToFocusOnAbductions(){
        academicRespect = 0;
    }
}
