import java.util.*;

class SummaryRanges {

    TreeSet<Integer> set;

    public SummaryRanges() {
        set = new TreeSet<>();
    }

    public void addNum(int value) {
        set.add(value);
    }

    public int[][] getIntervals() {

        ArrayList<int[]> result = new ArrayList<>();

        if (set.isEmpty()) {
            return new int[0][0];
        }

        int start = set.first();
        int previous = start;

        for (int num : set) {

            if (num == start) {
                continue;
            }

            if (num == previous + 1) {
                previous = num;
            }
            else {
                result.add(new int[]{start, previous});
                start = num;
                previous = num;
            }
        }

        result.add(new int[]{start, previous});

        return result.toArray(new int[result.size()][]);
    }
}