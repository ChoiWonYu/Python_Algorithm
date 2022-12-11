from collections import deque
graph=[
    [],[2,3,8],[1,7],[4,5],[3,5],[3,4],[7],[2,6,8],[1,7]
]
visited=[False]*9
def bfs(graph,start,visited):
    #deque를 라이브러리를 이용해 queue 구현
    queue=deque([start])
    #방문한 정점을 True로 변경
    visited[start]=True
    #queue가 빌 때까지 반복문
    while queue:
        #해당 정점과 인접한 정점의 visited값을 모두 True로 바꿨다면 pop하면서 print
        v=queue.popleft()
        print(v,end=' ')
        #현재 다루는 정점의 이어져 있는 정점을 탐색
        for i in graph[v]:
            #만약 방문한 적 없는 정점이라면 visited값을 바꾸고, queue에 넣어준다.
            if visited[i]==False:
                queue.append(i)
                visited[i]=True

bfs(graph,1,visited)