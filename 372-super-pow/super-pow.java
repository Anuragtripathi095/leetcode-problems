class Solution {

    private static final int MOD = 1337;

    public int superPow(int a, int[] b) {

        int result = 1;

        a %= MOD;

        for (int digit : b) {

            result = pow(result, 10);

            result = (result * pow(a, digit)) % MOD;
        }

        return result;
    }

    // Fast Modular Exponentiation
    private int pow(int a, int exp) {

        int result = 1;

        a %= MOD;

        while (exp > 0) {

            if ((exp & 1) == 1)
                result = (result * a) % MOD;

            a = (a * a) % MOD;

            exp >>= 1;
        }

        return result;
    }
}