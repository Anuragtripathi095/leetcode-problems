class Solution {
    public boolean isValidSerialization(String preorder) {

        String[] nodes = preorder.split(",");

        int slots = 1;

        for (String node : nodes) {

            // Every node uses one slot
            slots--;

            // No slot available
            if (slots < 0)
                return false;

            // Non-null node creates two new slots
            if (!node.equals("#"))
                slots += 2;
        }

        // All slots should be used exactly
        return slots == 0;
    }
}