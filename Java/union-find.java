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
