 interface A{
      default String goAhead(){
          return "Started.";
      }
      abstract String stop();
}
public class Main implements A{
      public String stop(){
            return "Break Pressed.";
      }
      public static void main(String args[]){
            //Invoke 
            System.out.println(new Main().goAhead());
      }
}