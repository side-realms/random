import java.util.ArrayList;
import java.util.Random;

public class HelloWorld {
	public static void main(String[] args){
		Random rand = new Random();
        ArrayList<Integer> clue = new ArrayList<Integer>();
        ArrayList<Integer> output = new ArrayList<Integer>();

		for(int i = 0; i<20; i++){
			clue.add(rand.nextInt(16));
		}

		for(int i = 0; i<100; i++){
			output.add(rand.nextInt());
		}

		System.out.println("clue: " + clue.toString());
		System.out.println("output: " + output.toString());

	}
}
