// Steps to remember before building segment tree

//  1. calculate the tree size correctly which is, size = 2*array_length -1

//  2. when passing start and end in every three methods start and end is array length not tree length, tree access will be with the index

//  3. mistakes you will make in building tree are
//      i. two function calls after calculating mid [start-mid] and [mid+1-end] here dont forget mid+1.
//      ii. put min from the left and right calls at current tree index.

//  4. mistakes you will make while updating tree are
//       i. here again two calls in building we take two calls but here either we go left or right respective to the update index
//       ii. if update index is less and equal than mid go left or right
//       iii. again after value returned from these calls make sure you update at current index is less or returned value is minimum.

//  5. mistakes you wil make while querying, this is specific to question in here it is related to finding min in given range L-R.
//             L - left, R - right, S - start, E - end
            
//             i.  first condition 
//              L ------- R
//                S-----E
//             ii. second condition
//                 L-R ---- S-E
//                 S-E ---- L_R

public class Main {
    static class SegmentTree{
        int[] tree;
        SegmentTree(int size){
            tree = new int[size];
        }
        
        int buildSegmentTree(int index,int start,int end, int[] arr){
            if(start==end){
                return tree[index]=arr[start];
            }

            int mid = (start+end)/2;
            int leftVal = buildSegmentTree(2*index+1,start,mid,arr);
            int rightVal = buildSegmentTree(2*index+2,mid+1,end,arr);
            
            tree[index] = Math.min(leftVal, rightVal);
             return tree[index];
        }
        
        // below function logic changes according to the question in this case it is finding min value in the give left-right range query.
        
        int traverseTree(int index, int start, int end, int left, int right){
            // below first condition 
            // L ------- R
            //   S-----E
            
            //second condition
            // L-R ---- S-E
            // S-E ---- L_R
            
            if(start>=left && end<=right) return tree[index];
            else if(end<left || right<start) return Integer.MAX_VALUE;
            int mid = (start+end)/2;
            int leftMin = traverseTree(2*index+1,start,mid,left,right);
            // mid+1 is important
            int rightMin = traverseTree(2*index+2,mid+1,end,left,right);
            return Math.min(leftMin,rightMin);
        }
        
        int updateTree(int index, int start, int end, int updateIndex, int num){
            if(start==end){
                tree[index]=num;
                return num;
            }
            int mid = (start+end)/2;
            int val = Integer.MAX_VALUE;
            // below if condition is important
            if(updateIndex<=mid && updateIndex>=start){
                val = updateTree(2*index+1,start,mid,updateIndex,num);
            }
            else{
                val = updateTree(2*index+2,mid+1,end,updateIndex,num);
            }
            
            return tree[index]= Math.min(tree[index],val);
            
        }
    }
    public static void main(String[] args) {
        int[] N = {5,4,5,7};
        int[][] Queries = {{1,2,4},{0,1,2},{1,1,4}};
      
        findMin(N,Queries);
        
    }
    
    static void findMin(int[] n,int[][] queries){
        int size = n.length;
        
        SegmentTree st = new SegmentTree(2*size-1);
        st.buildSegmentTree(0,0,size-1,n);
        
        int[] result = new int[queries.length];
        for(int i=0;i<result.length;i++){
            int a = queries[i][0];
            int b = queries[i][1];
            int c = queries[i][2];
            if(a==0){
                st.updateTree(0,0,size-1,b-1,c);
            }
            else{
                result[i]= st.traverseTree(0,0,size-1,b-1,c-1);
            }
        }
        
         for(int i=0;i<result.length;i++){
             System.out.println(result[i]+" ");
         }
        
    }
    
    
}
