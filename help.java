/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package help;

/**
 *
 * @author Brown-PC
 */
import java.io.*  ; 
import java.lang.*;
import java.util.*;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Help {
  java.io.FileReader read;

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws Exception {
        //checklist();
        int counter1 = notification.count_lines1();
        int counter2 = notification.count_lines2();
        notification.files_check(counter1,counter2);
        System.out.println(notification.count_lines1());
        System.out.println(notification.count_lines2());
    }
    
    static void checklist(){
    System.out.println("1 - decorat bulk ACTION \n"
            + "2 - notification message \n");
    Scanner userInputScanner = new Scanner(System.in);
    int userin = userInputScanner.nextInt();
    
    if (userin == 1) {
        bulk_action();
    }if (userin == 2 ){
        send_notification();
    }else {
        System.out.println("invalid input try again ");
    long sleep_time = 500 ; 
        try {
            Thread.sleep(sleep_time);
        } catch (InterruptedException ex) {
            Logger.getLogger(Help.class.getName()).log(Level.SEVERE, null, ex); 
        }   
    }
    
    }
    static void  bulk_action(){
        // The name of the file to open.
   String fileName = "C:\\Users\\Brown-PC\\Documents\\NetBeansProjects\\Help\\src\\help\\input.txt"  ;
   String outName  = "C:\\Users\\Brown-PC\\Documents\\NetBeansProjects\\Help\\src\\help\\output.txt" ;
        // This will reference one line at a time
    String line = null;
    try {
            // FileReader reads text files in the default encoding.
            FileReader fileReader = 
                new FileReader(fileName);

            // Always wrap FileReader in BufferedReader.
            BufferedReader bufferedReader = 
                new BufferedReader(fileReader);

            FileWriter fileW =
                new FileWriter(outName);
            
            BufferedWriter bufferedwriter = 
                new BufferedWriter(fileW);
            
            while((line = bufferedReader.readLine()) != null) {
                String Result = "'" + line.replace("\n", "'") + "'" ;
                bufferedwriter.write("\n" + Result);
                System.out.println(Result);
            }   
            // Always close files.
            bufferedReader.close(); 
            bufferedwriter.close();         
        }
        catch(FileNotFoundException ex) {
            System.out.println(
                "Unable to open file '" + 
                fileName + "'");                
        }
        catch(IOException ex) {
            System.out.println(
                "Error reading file '" 
                + fileName + "'");                  
            // Or we could just do this: 
            // ex.printStackTrace();
        }
    }
    static void send_notification(){
    
    
    }
    
}
