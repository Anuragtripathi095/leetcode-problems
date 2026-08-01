/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation.
 * interface NestedInteger {
 *     // @return true if this NestedInteger holds a single integer.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds,
 *     // if it holds a single integer
 *     public Integer getInteger();
 *
 *     // @return the nested list that this NestedInteger holds,
 *     // if it holds a nested list
 *     public List<NestedInteger> getList();
 * }
 */

class NestedIterator implements Iterator<Integer> {

    private List<Integer> list;
    private int index;

    public NestedIterator(List<NestedInteger> nestedList) {
        list = new ArrayList<>();
        index = 0;
        flatten(nestedList);
    }

    private void flatten(List<NestedInteger> nestedList) {
        for (NestedInteger ni : nestedList) {
            if (ni.isInteger()) {
                list.add(ni.getInteger());
            } else {
                flatten(ni.getList());
            }
        }
    }

    @Override
    public Integer next() {
        return list.get(index++);
    }

    @Override
    public boolean hasNext() {
        return index < list.size();
    }
}