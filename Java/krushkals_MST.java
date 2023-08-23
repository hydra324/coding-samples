// To find Mininum Spanning Tree in the graph 
class Solution {
    public int minCostConnectPoints(int[][] points) {
        Set<Integer> visited = new HashSet<>();
        PriorityQueue<Pair> pq = new PriorityQueue<>((a,b)->(a.wt - b.wt));

        for(int i=0;i<points.length;i++){
            for(int j=i+1;j<points.length;j++){
                int wt = distance(points[i],points[j]);
                pq.add(new Pair(i,j,wt));
            }
        }
        int result = 0;
        DSU ds = new DSU(points.length);
        while(!pq.isEmpty()){
            Pair p = pq.poll();
            // System.out.println(p.a+" "+ds.find(p.a)+" "+p.b+" "+ds.find(p.b));
            if(ds.find(p.a) == ds.find(p.b)) continue;
            ds.union(p.a, p.b);
            result+=p.wt;
            visited.add(p.a);
            visited.add(p.b);
        }

        return result;
    }

    int distance(int[] a, int[] b){
        return Math.abs(a[0]-b[0]) + Math.abs(a[1]-b[1]);
    }

    class DSU{
        int[] parent;
        int[] rank;

        DSU(int size){
            parent = new int[size];
            rank = new int[size];
            for(int i=0;i<size;i++)
                parent[i]=i;
            Arrays.fill(rank,1);
        }

        void union(int a, int b){
            int parentA = find(a);
            int parentB = find(b);
            if(parentA==parentB) return;

            if(rank[parentA]<rank[parentB]){
                parent[parentA]=parentB;
            }
            else if(rank[parentB]<rank[parentA]){
                parent[parentB]=parentA;
            }
            else{
                parent[parentA]=parentB;
                rank[parentB]++;
            }
        }

        int find(int a){
            if(a == parent[a]) return a;
            return parent[a]=find(parent[a]);
        }

    }

    class Pair{
        int a;
        int b;
        int wt;
        Pair(int a, int b, int wt){
            this.a = a;
            this.b = b;
            this.wt = wt;
        }
    }
}
