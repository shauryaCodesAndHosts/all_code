         import java.util.Map;
import java.util.TreeMap;
         class Test{
                public static void main (String[] args){
                           Map<Integer, String> map = new TreeMap();
                           Integer i1= new Integer(1);
                           Integer i2= new Integer(2);
                           Integer i3= new Integer(1);
                           if(i1.equals(i3)){
                                   map.put(i2,"MNO");
                           }
                           map.put(i1,"UVW");
                           if(i1.equals(i3)){
                            System.out.println("yahan aaya hai ");
                                  map.put(i1,"ABC");
                                  map.put(i2,"XYZ");
                           }
                          System.out.println(map);
                 }
          }