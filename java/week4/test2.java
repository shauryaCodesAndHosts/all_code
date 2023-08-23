   abstract class A{
        final static int current_sem(){
        return 4;
        }
        abstract String sem_subjects();
   }
   class B extends A{
        public String sem_subjects(){
              return "DBMS, DSA and Programming concept using Java.";
        }
        public static void main(String args[]){
              A obj=new B();
             System.out.println("Current Semester: "+A.current_sem()
                       +"\nSubjects: "+obj.sem_subjects());
        }
   }