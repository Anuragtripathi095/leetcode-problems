class Solution {
    public String decodeString(String s) {

        Stack<Integer> numberStack = new Stack<>();
        Stack<String> stringStack = new Stack<>();

        String current = "";
        int number = 0;

        for (int i = 0; i < s.length(); i++) {

            char ch = s.charAt(i);

            if (Character.isDigit(ch)) {
                number = number * 10 + (ch - '0');
            }

            else if (ch == '[') {
                numberStack.push(number);
                stringStack.push(current);

                number = 0;
                current = "";
            }

            else if (ch == ']') {
                int repeat = numberStack.pop();
                String previous = stringStack.pop();

                String temp = "";

                for (int j = 0; j < repeat; j++) {
                    temp += current;
                }

                current = previous + temp;
            }

            else {
                current += ch;
            }
        }

        return current;
    }
}