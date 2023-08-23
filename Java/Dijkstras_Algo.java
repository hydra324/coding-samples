class Solution {
    public int networkDelayTime(int[][] edges, int n, int k) {
        List<int[]> graph[] = new ArrayList[n+1];

        for(int i=0;i<=n;i++)
            graph[i] = new ArrayList<int[]>();
        for(int i=0;i<edges.length;i++){
            int a = edges[i][0];
            int b = edges[i][1];
            int wt = edges[i][2];
            graph[a].add(new int[]{b,wt});
        }

        PriorityQueue<Pair> pq = new PriorityQueue<>((a,b)->(a.dist-b.dist));
        int[] distance = new int[n+1];
        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[k]=0;
        pq.add(new Pair(k,0));
        Set<Integer> set = new HashSet<>();
        int total = 0;
        while(!pq.isEmpty()){
            Pair p = pq.poll();
            set.add(p.node);
            for(int[] i :graph[p.node]){   
                int neigh = i[0];
                int wt = i[1];     
                // System.out.println(neigh+" "+p.node);      
                if(wt+p.dist<distance[neigh]){
                    distance[neigh] = wt+p.dist;
                    pq.add(new Pair(neigh, wt+p.dist));
                }
            }
        }
        // if(set.size()<n) return -1;
        int ans = Integer.MIN_VALUE;
        for(int i=1;i<distance.length;i++){
            ans = Math.max(ans, distance[i]);
        }
            
        return ans == Integer.MAX_VALUE? -1: ans;

    }

    class Pair{
        int node;
        int dist;
        Pair(int node, int dist){
            this.node = node;
            this.dist = dist;
        }
    }
}
