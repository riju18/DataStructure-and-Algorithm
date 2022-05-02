# <span style="color: yellow;">**Graph**</span>

+ [Basic](#definition)
+ [Terminogloy](#terminogloy)

# **definition**:

> It's a collection of obj called Vertices & together with relationship between them called Edges. 
>> ![graph](http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/11-Graph/FIGS/Graphs/graph01.gif)
>
> Ex: Flight map, road map

# **terminogloy**:

+ <span style="color: orange;">Edges</span>:
  > <span style="color: pink;">Directed</span>: It has orientartion.
  >> ![directed graph](https://computersciencewiki.org/images/c/c6/Directed_graph.png)
  >
  > <span style="color: pink;">Undirected</span>: It's bidirectional.
  >> ![undirected graph](https://www.researchgate.net/profile/Hakan-Terelius/publication/265428782/figure/fig3/AS:669498856194058@1536632374537/An-undirected-graph-with-7-nodes-and-7-edges.png)
  >
  > <span style="color: pink;">Weighted</span>: Weight/cost is assigned to each edge.
  >> ![weighted graph](http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/11-Graph/FIGS/Dijkstra/weight01.gif)
  >
  > + Weighted directed
  > + Weighted undirected
  >
  > <span style="color: pink;">Incoming edges</sapn>
  >> ![incoming edges](https://www.researchgate.net/profile/Andrej-Gajduk/publication/262338460/figure/fig2/AS:614187415908367@1523445099831/Incoming-and-outgoing-edges-for-node-C.png)
  >
  > <span style="color: pink;">Outgoing edges</sapn>
  >> ![outgoing edges](https://iq.opengenus.org/content/images/2020/05/IMG_0022.jpg)

+ <span style="color: orange;">Source/Destination</sapn>:
  + Source: 1st end-point (from)
  + Destination: 2nd end-point (to)

+ <span style="color: orange;">Degree of vertex</sapn>: Number of incident edges of the vertex.

  > no of incoming edges + no of outgoing edges
  + Indegree: no of incomig edges
  + Outdegree: no of outgoing edges

+ <span style="color: orange;">Path</sapn>: Seq of edges starting at one vertex & ending at another vertex.
+ <span style="color: orange;">Cycle</sapn>: It's a path that start & end at the same vertex.
  > ![cycle](https://media.geeksforgeeks.org/wp-content/uploads/cycle-BFS.png) 
