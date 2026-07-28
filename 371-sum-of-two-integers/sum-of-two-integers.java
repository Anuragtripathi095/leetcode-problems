class Solution {
    public int getSum(int a, int b) {

        while (b != 0) {

            // Sum without carry
            int sum = a ^ b;

            // Carry
            int carry = (a & b) << 1;

            a = sum;
            b = carry;
        }

        return a;
    }
}