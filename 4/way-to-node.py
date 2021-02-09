#2-1
import queue

WAY,NOT_WAY = 1,0

def search_way_dfs(directed_graph,start_node=0,end_node=8):
    stack = [start_node] # use list as stack
    is_visited_arr = [False for _ in range(len(directed_graph))]
    while len(stack) != 0:
        current_node = stack[-1]
        adjacent_node_way = directed_graph[current_node]

        if adjacent_node_way[end_node] == WAY:
            return True

        all_adjacent_node_visited = True
        for adjacent_node in range(len(adjacent_node_way)):
            if (adjacent_node_way[adjacent_node] == WAY) and (not is_visited_arr[adjacent_node]):
                all_adjacent_node_visited = False
                stack.append(adjacent_node)
                break

        if all_adjacent_node_visited == True:
            visited_node = stack.pop()
            is_visited_arr[visited_node] = True

    return False


    

def search_way_bfs(directed_graph,start_node=0,end_node=8):
    q = queue.Queue()
    q.put(start_node)
    is_visited_arr = [False for _ in range(len(directed_graph))]
    while q.qsize() != 0:
        current_node = q.get()
        is_visited_arr[current_node] = True

        adjacent_node_way = directed_graph[current_node]

        if adjacent_node_way[end_node] == WAY:
            return True
        
        for adjacent_node in range(len(adjacent_node_way)):
            if (adjacent_node_way[adjacent_node] == WAY) and (not is_visited_arr[adjacent_node]):
                q.put(adjacent_node)

    return False

if __name__ == "__main__":
    directed_graph = [
        [0,1,0,1,1,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,1,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1],
        [0,0,0,0,0,0,0,0,0],
    ]
    print(search_way_dfs(directed_graph)) # True
    print(search_way_dfs(directed_graph,start_node=1,end_node=4)) # False
    print(search_way_bfs(directed_graph)) # True
    print(search_way_bfs(directed_graph,start_node=1,end_node=4)) # False
    