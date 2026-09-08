import java.util.*;

class Solution {
    public boolean isRectangleCover(int[][] rectangles) {

        int minX = Integer.MAX_VALUE;
        int minY = Integer.MAX_VALUE;
        int maxX = Integer.MIN_VALUE;
        int maxY = Integer.MIN_VALUE;

        long totalArea = 0;

        Set<String> set = new HashSet<>();

        for (int[] r : rectangles) {

            int x1 = r[0];
            int y1 = r[1];
            int x2 = r[2];
            int y2 = r[3];

            minX = Math.min(minX, x1);
            minY = Math.min(minY, y1);
            maxX = Math.max(maxX, x2);
            maxY = Math.max(maxY, y2);

            totalArea += (long)(x2 - x1) * (y2 - y1);

            String p1 = x1 + "," + y1;
            String p2 = x1 + "," + y2;
            String p3 = x2 + "," + y1;
            String p4 = x2 + "," + y2;

            toggle(set, p1);
            toggle(set, p2);
            toggle(set, p3);
            toggle(set, p4);
        }

        long boundingArea = (long)(maxX - minX) * (maxY - minY);

        if (totalArea != boundingArea) {
            return false;
        }

        if (set.size() != 4) {
            return false;
        }

        return set.contains(minX + "," + minY)
            && set.contains(minX + "," + maxY)
            && set.contains(maxX + "," + minY)
            && set.contains(maxX + "," + maxY);
    }

    private void toggle(Set<String> set, String point) {
        if (set.contains(point)) {
            set.remove(point);
        } else {
            set.add(point);
        }
    }
}