

public class Example{
          public static void main(String[] args){
              B ob=new B();
              ob.show();
          }
    }

class A{
         public void show(){
              System.out.println("A show() called");
         }
     }
     class B extends A{
         public void show(){
              System.out.println("B show() called");
         }
     }


    /* class Example{
        public static void main(String[] args){
              Northeast charming = new Northeast();   
        }
}

class India{
        public India(){
              System.out.println("Visit Northeast India.");
        }
}
class Northeast extends India{
        public Northeast(){        
              System.out.println("Kolkata connects Manipur, Assam, Nagaland and Tripura directly by air.");                
        }
}
*/