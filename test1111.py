import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
class Graph {
	private int V;
	private int E;
	private List<Integer>[] adj;
	private int[][] a;

	public Graph(int V) {
		this.E = 0;
		this.V = V;
		adj = new ArrayList[V];
		a = new int[V][V];
		for (int i = 0; i < V; i++) {
			adj[i] = new ArrayList<>();
		}
	}

	public void addEdge(int v1, int v2) {
		a[v1][v2] = 1;
		a[v2][v1] = 1;
		adj[v1].add(v2);
		adj[v2].add(v1);
		E++;
	}

	public int V() {
		return V;
	}

	public int E() {
		return E;
	}


	public List<Integer> adj(int i) {
		return adj[i];
	}


	public List<Integer> adj1(int i) {
		List<Integer> list = new ArrayList<>();
		int[] adg1 = new int[V];
		adg1 = a[i];
		for (int v : adg1)
			if (v != 0)
				list.add(v);
		return list;
	}
}

public class Main {
	static boolean[] marked;
	static int count;
	static int[] edgeTo;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = Integer.valueOf(sc.nextLine());
		Graph g = new Graph(n);
		for(int i=0;i<n-1;i++){
			String str[] = sc.nextLine().split(" ");
			g.addEdge(Integer.valueOf(str[0])-1, Integer.valueOf(str[1])-1);
		}
		marked = new boolean[g.V()];
		edgeTo = new int[g.V()];
		dfs(g,0);
		System.out.println(count);
	}
	
	public static void dfs(Graph G, int s) {
		marked[s] = true;
		count++;
		for (int temp : G.adj(s))
			if (!marked[temp]) {
				edgeTo[temp] = s;
				dfs(G, temp);
			}
	}
}
