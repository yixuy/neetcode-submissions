class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // mapping
        Map<Integer, Integer> freq = new HashMap<>();
        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }
        // heap
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> ( b[0] - a[0]));
        for(Map.Entry<Integer, Integer> entry: freq.entrySet()){
            heap.offer(new int[]{entry.getValue(), entry.getKey()});
        }

        int[] res = new int[k];

        for(int i = 0 ; i < k; i++){
            res[i] = heap.poll()[1];
        }

        
        return res;
        
    }
}
