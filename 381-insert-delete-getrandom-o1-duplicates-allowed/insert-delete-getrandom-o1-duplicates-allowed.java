import java.util.*;

class RandomizedCollection {

    private ArrayList<Integer> list;
    private HashMap<Integer, Set<Integer>> map;
    private Random random;

    public RandomizedCollection() {
        list = new ArrayList<>();
        map = new HashMap<>();
        random = new Random();
    }

    public boolean insert(int val) {
        boolean notPresent = !map.containsKey(val);

        map.putIfAbsent(val, new HashSet<>());
        map.get(val).add(list.size());

        list.add(val);

        return notPresent;
    }

    public boolean remove(int val) {
        if (!map.containsKey(val))
            return false;

        // Get one occurrence of val
        int removeIndex = map.get(val).iterator().next();

        // Remove this index from val's set
        map.get(val).remove(removeIndex);

        int lastIndex = list.size() - 1;
        int lastValue = list.get(lastIndex);

        if (removeIndex != lastIndex) {
            // Move last value to removed position
            list.set(removeIndex, lastValue);

            // Update lastValue's index set
            map.get(lastValue).remove(lastIndex);
            map.get(lastValue).add(removeIndex);
        }

        list.remove(lastIndex);

        if (map.get(val).isEmpty()) {
            map.remove(val);
        }

        return true;
    }

    public int getRandom() {
        return list.get(random.nextInt(list.size()));
    }
}