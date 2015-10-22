import java.lang.System;
import java.util.Map;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileNotFoundException;
import java.util.HashMap;

public class Lema {
	//foram - ir vs ser
	private static Map<Bigram, Integer> foramIrBigrams;
	private static Map<Bigram, Integer> foramSerBigrams;
	private static Map<String, Integer> foramIrUnigrams;
	private static Map<String, Integer> foramSerUnigrams;

	//lida - lidar vs ler
	private static Map<Bigram, Integer> lidaLidarBigrams;
	private static Map<Bigram, Integer> lidaLerBigrams;
	private static Map<String, Integer> lidaLidarUnigrams;
	private static Map<String, Integer> lidaLerUnigrams;


	public static void main(String[] args) {
		System.out.println("Hello World!");
		if (args.length > 0) { //TODO: ver dos argumentos, casos de erro etc..
			foramIrBigrams = readBigrams(args[0]);
			foramSerBigrams = readBigrams(args[1]);
			foramIrUnigrams = readUnigrams(args[2]);
			foramSerUnigrams = readUnigrams(args[3]);

			lidaLidarBigrams = readBigrams(args[4]);
			lidaLerBigrams = readBigrams(args[5]);
			lidaLidarUnigrams = readUnigrams(args[6]);
			lidaLerUnigrams = readUnigrams(args[7]);
		}
	}

	private static Map<Bigram, Integer> readBigrams(String path) {
		Map<Bigram, Integer> map = new HashMap<Bigram, Integer>();
		try {
			BufferedReader br = new BufferedReader(new FileReader(path));
			String line;
			while ((line = br.readLine()) != null) {
				String[] tokens = line.split("\\s");
       			map.put(new Bigram(tokens[0], tokens[1]), Integer.parseInt(tokens[2]));
			}
		} catch (FileNotFoundException e) {
			System.err.println("Could not find file with name " + path);
		} catch (Exception e) {
			System.err.println(e.getMessage());
		}
		return map;
	}

	private static Map<String, Integer> readUnigrams(String path) {
		return null;
	}

	private static class Bigram {
		private String gram1;
		private String gram2;

		public Bigram(String gram1, String gram2) {
			this.gram1 = gram1;
			this.gram2 = gram2;
		}
	}
}