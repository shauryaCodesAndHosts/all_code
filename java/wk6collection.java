class Example{
     public static void main(String args[]) {
         try {
              System.out.println("Quotient is:" + 0/0);
         }
         catch(ArithmeticException e) {
              System.out.println("Denominator should not be zero");
              //System.exit(1);
         }
         finally{
              System.out.println("you are in finally..");
         }
     }
}