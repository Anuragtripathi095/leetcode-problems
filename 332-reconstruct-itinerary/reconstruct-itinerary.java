class Solution {

    Map<String, PriorityQueue<String>> graph = new HashMap<>();
    LinkedList<String> itinerary = new LinkedList<>();

    public List<String> findItinerary(List<List<String>> tickets) {

        // Build graph
        for (List<String> ticket : tickets) {
            graph.putIfAbsent(ticket.get(0), new PriorityQueue<>());
            graph.get(ticket.get(0)).offer(ticket.get(1));
        }

        // Start DFS from JFK
        dfs("JFK");

        return itinerary;
    }

    private void dfs(String airport) {

        PriorityQueue<String> pq = graph.get(airport);

        while (pq != null && !pq.isEmpty()) {
            String next = pq.poll();
            dfs(next);
        }

        // Add airport after visiting all outgoing edges
        itinerary.addFirst(airport);
    }
}