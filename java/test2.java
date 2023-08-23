   class Bird{
     public void fly(){
           System.out.println("it can fly");
     }
  }
  class Duck extends Bird{
      public void swim(){
            System.out.println("it can swim");
     }
  }
   class test2{
      public static void doIt(Bird b){
            b.fly();
            if(b instanceof Duck)
                      ((Duck) b).swim();

     }
     public static void main(String[] args){
            Duck d = new Duck();
            doIt(d);
     }
  }