class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
     
        // sort then map
        Map<String, List<String>> mapping = new HashMap<>();
        for(String s: strs){
            char[] chars = s.toCharArray();
            Arrays.sort(chars);

            String sortString = new String(chars);
           
            if(!mapping.containsKey(sortString)){
                mapping.put(sortString, new ArrayList<>());
            }
            mapping.get(sortString).add(s);
            
        }
      
        return new ArrayList<>(mapping.values());
    }
}
