
abstract class NewYear {
    final abstract String resolution();
}
class Year_2022 extends NewYear{
    public String resolution() {
          return "Walk up early"+"\n"+"Do exercise"+"\n"+"Take shower everyday";
    }
    public static void main(String args[]) {
          System.out.print(new Year_2022().resolution());
    }
}