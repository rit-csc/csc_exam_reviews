import java.util.ArrayList;

public class WonkyHashTable {
	private int size;
	private ArrayList<String> table;

	public WonkyHashTable(int s) {
		size = s;
		table = new ArrayList<String>(size);
		for(int i = 0; i < s; i++) {
			table.add("");
		}
	}

	public void add(String element) {
		int hash = bad_hash(element);
		table.set(hash, element);
		System.out.println(table.toString());
	}

	private boolean contains(String element) {
		for(String t : table) {
			if(element.equals(t)) {
				return true;
			}
		}
		return false;
	}

	private int bad_hash(String element) {
		return element.length() % table.size();
	}

	public static void main(String args[]) {
		WonkyHashTable htable = new WonkyHashTable(4);
		for(String s : "I wrestled a bear once".split(" ")) {
			htable.add(s);
		}
	}
}
