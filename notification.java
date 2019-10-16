/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Brown-PC
 */
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package help;


import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;


public class notification{

   public  static void files_check(int counter1 , int counter2) throws Exception{
        String input = "C:\\Users\\Brown-PC\\Documents\\NetBeansProjects\\Help\\src\\help\\input.txt";
         String input2 = "C:\\Users\\Brown-PC\\Documents\\NetBeansProjects\\Help\\src\\help\\output.txt";

         
         for(int z = 1; z <= counter1 ; z++){
           FileReader in = new FileReader(input);
           BufferedReader in1 = new BufferedReader(in);
           String line = in1.readLine() ; 
           System.out.println(line);
                   }
          }
  
   
   public static int count_lines1() throws FileNotFoundException, IOException{
       String input = "C:\\Users\\Brown-PC\\Documents\\NetBeansProjects\\Help\\src\\help\\input.txt";
         String input2 = "C:\\Users\\Brown-PC\\Documents\\NetBeansProjects\\Help\\src\\help\\output.txt";
         FileReader in = new FileReader(input);
         BufferedReader in1 = new BufferedReader(in);
         int countlines1 = 0 ; 
         while (in1.readLine() != null){
          countlines1++ ;
         }
         return countlines1;
   }
   
      public static int count_lines2() throws FileNotFoundException, IOException{
         String output = "C:\\Users\\Brown-PC\\Documents\\NetBeansProjects\\Help\\src\\help\\output.txt";
         FileReader out = new FileReader(output);
         BufferedReader out1 = new BufferedReader(out);
         int countlines2 = 0 ; 
         while (out1.readLine() != null){
          countlines2++ ;
         }
         return countlines2;
   }
   
   
  }
