class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> mapping = new HashMap<>();

        mapping.put(')', '(');
        mapping.put(']', '[');
        mapping.put('}', '{');
        for(char c: s.toCharArray()){
            if(c == '[' || c == '(' || c == '{'){
                stack.push(c);
            }else{
                if(stack.isEmpty() || stack.peek() != mapping.get(c)){
                   return false;
                }
                stack.pop();
            }
        }

     
        return stack.isEmpty();
    }
}
