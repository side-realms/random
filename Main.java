import java.util.ArrayList;
import java.util.Random;

public class Main {
    public static void main(String[] args){
        Random rand = new Random();
        ArrayList<Integer> clue = new ArrayList<Integer>();
        ArrayList<Integer> output = new ArrayList<Integer>();

        for(int i=0; i<2; i++){
            int num = rand.nextInt();
            clue.add(num);
        }

        for(int i=0; i<100; i++){
            int num = rand.nextInt();
            output.add(num);
        }

        System.out.println("given: "+ clue.toString());
        System.out.println("output: "+ output.toString());
    }
}
