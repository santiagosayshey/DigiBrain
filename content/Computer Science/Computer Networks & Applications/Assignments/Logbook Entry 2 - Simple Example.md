
# Input

```
A
B
C
LINKSTATE
A-B 2
B-C 3 B
UPDATE
A-C 1 A,C
END
```

# Explanation

![[Pasted image 20240522140023.png]]

![[Pasted image 20240522141326.png]]



Logbook Entry 2 - Simple Example

Since I wasn't quite grasping the explanation of the inputs and outputs from the assignment spec (im a very visual learner), I decided I should try to work through some examples. For each of the steps, I'll outline the expected output and draw the network topology. 

1. Input:
   ```
   A
   B
   C
   LINKSTATE
   A-B 2
   B-C 3 B
   UPDATE
   A-C 1 A,C
   END
   ```

2. Explanation:
   - The first three lines define the routers in the topology: A, B, and C.
   - The "LINKSTATE" section starts, and the first link is defined:
     - `A-B 2`: There is a link between router A and router B with a cost of 2.
   - The second link is defined:
     - `B-C 3 B`: There is a link between router B and router C with a cost of 3. The optional list "B" specifies that the Expected Output should be shown for router B after processing this link.
   - The "UPDATE" section starts, and an update is provided:
     - `A-C 1 A,C`: A new link is added between router A and router C with a cost of 1. The optional list "A,C" specifies that the Expected Output should be shown for routers A and C after processing this update.
   - The "END" keyword signals the end of the input.

3. Expected Output:
   ```
   B Neighbour Table:
   A|2
   C|3

   B LSDB:
   A|B|2
   B|C|3

   B Routing Table:
   A|A|2
   C|C|3

   A Neighbour Table:
   B|2
   C|1

   A LSDB:
   A|B|2
   A|C|1
   B|C|3

   A Routing Table:
   B|B|2
   C|C|1

   C Neighbour Table:
   A|1
   B|3

   C LSDB:
   A|B|2
   A|C|1
   B|C|3

   C Routing Table:
   A|A|1
   B|B|3
   ```

My drawings of the network topology have been included in the next entry!

Logbook Entry 2 - Simple Example (Continued)

Observations:
- This exercise seems perfect for applying object-oriented programming.
- We can start with a "Node" class, which defines functions for the following:
  - Constructor: Sets the name of the node.
  - `add_neighbor(self, neighbor, cost)`: Adds a neighbour to the node's neighbour table, along with the cost of the link.
  - `remove_neighbor(self, neighbor)`: Removes a neighbour from the node's neighbour table.
  - `update_lsdb(self, lsdb)`: Updates the node's LSDB with the given LSDB information.
  - `calculate_routing_table(self)`: Calculates the node's routing table based on the current LSDB using Dijkstra's algorithm.
  - `print_neighbor_table(self)`: Prints the node's neighbor table in the required format.
  - `print_lsdb(self)`: Prints the node's LSDB in the required format.
  - `print_routing_table(self)`: Prints the node's routing table in the required format.

- We can also create a "Network" class that represents the entire network topology and manages the interactions between nodes:
  - Constructor: Initializes an empty dictionary to store the nodes in the network.
  - `add_node(self, node_name)`: Adds a new node to the network with the given name.
  - `add_link(self, node1, node2, cost)`: Adds a link between two nodes with the given cost.
  - `remove_link(self, node1, node2)`: Removes the link between two nodes.
  - `update_lsdbs(self)`: Updates the LSDVs of all nodes in the network.
  - `process_input(self, input_lines)`: Processes the input lines and performs the necessary actions (adding nodes, links, updating LSDVs, etc.).
  - `print_output(self, node_names)`: Prints the Expected Output for the specified nodes.

[Insert a class diagram image here illustrating the "Node" and "Network" classes, their attributes, and methods.]

Implementation Plan:
1. Create the "Node" class with the specified methods.
2. Create the "Network" class with the specified methods.
3. Implement the `process_input` method in the "Network" class to handle the input lines and perform the necessary actions.
4. Implement the `print_output` method in the "Network" class to generate the Expected Output for the specified nodes.
5. In the main program:
   - Create a "Network" object.
   - Read the input lines from the standard input.
   - Call the `process_input` method with the input lines.
   - Call the `print_output` method with the specified node names.

[Insert a flowchart image here illustrating the main program flow, including reading input, processing input, and generating output.]

Logbook Entry 3 (2:32pm, May 22, 2024)

Thoughts / Observations:
- Working through some hand-written examples really helped my understanding of what the expected requirements are.
- This assignment seems perfect for an object-oriented programming approach.

Next steps:
- Outlining an extensive python implementation

Logbook Entry 4 (2:40pm, May 22, 2024)

Now that I have a pretty good understanding of what I need to do, I can actually start planning it.

This class implementation won't be perfect, but it's going to benefit me greatly to have planned this before diving into it. 

Code Outline:

1. Node Class:
   - Variables:
     - `name`: Stores the name of the node.
     - `neighbors`: A dictionary that stores the neighboring nodes and their associated link costs.
     - `routing_table`: A dictionary that stores the routing table entries.
   - Functions:
     - Constructor, `add_neighbor()`, `remove_neighbor()`, `calculate_routing_table()`, and printing functions for neighbor table, LSDB, and routing table.

2. Network Class:
   - Variables:
     - `nodes`: A dictionary that stores all the nodes in the network, with node names as keys and Node objects as values.
     - `lsdb`: A dictionary that represents the Link-State Database (LSDB) of the network.
   - Functions:
     - Constructor, `add_node()`, `add_link()`, `remove_link()`, `process_input()`, and `print_output()`.

Implementation Details:
- The `Node` class encapsulates the properties and behaviors of individual nodes in the network. It stores the node's name, neighbors, and routing table, and provides methods to update and retrieve this information.
- The `Network` class represents the entire network topology and manages the interactions between nodes. It stores all the nodes in the network and maintains the LSDB. It provides methods to add/remove nodes and links, process input commands, and generate the expected output.

By separating the responsibilities into two classes, we can achieve a modular and maintainable design. The `Node` class focuses on the individual node's perspective, while the `Network` class handles the overall network operations and coordination between nodes.

Next Steps:
- Setting up the SVN directory, initialising initial code files with proposed functions and comments.
	- Implement the `Node` class with the necessary variables and functions.
	- Implement the `Network` class with the necessary variables and functions.
	- Develop the `process_input()` method in the `Network` class to handle the input commands and update the network state accordingly.
	- Develop the `print_output()` method in the `Network` class to generate the expected output for the specified nodes.
	- Create a main program that utilizes the `Network` class to read input, process commands, and generate output.


============================
Logbook Entry 9 (3:48pm, May 22, 2024)
============================

I've completed the initialisation of the 'Network' class and included extensive docstrings (function explanations)

Here's the rundown:

- The `__init__` method is extensively commented to describe its purpose and attributes.
    - The `nodes` attribute is a dictionary that stores all the nodes in the network, with node names as keys and Node instances as values.
    - The `lsdb` attribute is a dictionary representing the link-state database (LSDB) of the network, where the keys are tuples of node names (representing links) and the values are the link costs.
- Each method has a docstring that describes its purpose and parameters (if any).
    - The `add_node` method adds a new node to the network.
    - The `add_link` method adds a new link between two nodes in the network.
    - The `remove_link` method removes the link between two nodes in the network.
    - The `process_input` method processes the input lines and performs the necessary actions based on the network topology and updates. This may be segmented into multiple functions in future. 
    - The `print_output` method prints the expected output for the specified nodes.

What's Next?
- Setting up the main `Dijkstra` file to instantiate a Network object and a function to take input


============================
Logbook Entry 10 (4:15pm, May 22, 2024)
============================

I've initialized all the necessary files and functions, and now it's time to start implementing everything!

I'll start by tackling the input processing first. Here's my plan:

- Implement the `read_input` function in `Dijkstra` to read input lines from the standard input (stdin) until "END" is encountered.
	- Return the list of input lines.

- Implement the `process_input` method in the `Network` class to handle different types of input lines and update the network accordingly.
	- Keep track of the current input section ("INIT", "LINKSTATE", or "UPDATE") using a variable.
	- Iterate over each input line and process it based on the current section.
	- For "INIT" lines, add new nodes to the network.
	- For "LINKSTATE" and "UPDATE" lines:
		- Extract the node names, cost, and optional list of chosen routers.
		- Add or remove links between nodes based on the cost.
		- Update the network topology and print the output for chosen routers, if any.


============================
Logbook Entry 11 (4:09pm, May 22, 2024)
============================

I've implemented the `read_input` function. Seems to be working pretty well!

```
A
B
C
LINKSTATE
A-B 2
B-C 3 B
UPDATE
A-C 1 A,C
END
::input lines:: ['A', 'B', 'C', 'LINKSTATE', 'A-B 2', 'B-C 3 B', 'UPDATE', 'A-C 1 A,C', 'END']
```

Now on to implementing the `process_input` function!


============================
Logbook Entry 12 (4:18pm, May 22, 2024)
============================

I have implemented the `process_input` function in the `Network` class to handle the input processing for the network simulation. Here's a summary of what the function does:

- It takes a list of input lines as a parameter.
- It iterates over each line and determines the current section based on the keywords "LINKSTATE", "UPDATE", and "END".
- For each line in the "LINKSTATE" or "UPDATE" section:
  - It splits the line into parts and extracts the node names and cost.
  - If the nodes are not already present in the network, it adds them by calling the `add_node` function.
  - If the cost is -1, it removes the link between the nodes by calling the `remove_link` function.
  - Otherwise, it adds the link between the nodes with the given cost by calling the `add_link` function.
  - If there are additional parts in the line, it splits them by comma and passes them to the `print_output` function to print the output for the specified nodes.
- For lines outside the "LINKSTATE" or "UPDATE" section, it adds the node to the network by calling the `add_node` function.

Running the our initial example: 

```
A
B
C
LINKSTATE
A-B 2
B-C 3 B
UPDATE
A-C 1 A,C
END
add_node function called with argument: A
add_node function called with argument: B
add_node function called with argument: C
add_node function called with argument: B
add_node function called with argument: C
add_link function called with arguments: B, C, 3
add_node function called with argument: A
add_node function called with argument: C
add_link function called with arguments: A, C, 1
```

That doesn't seem right.... Seems we forgot a major function in our Network implementation - `update_links`. We also need to call the printing functions within the linkstate and update functions. 


============================
Logbook Entry 15 (5:09pm, May 22, 2024)
============================

Process input seems to be working properly now!!

Observations:
This `process_input` function may be the hardest part of the assignment... Here are a list of issues I've found when parsing the line.
- We need to define an instruction type for each type of line
- If the line *is* the instruction type, then it needs to be skipped over...
- LINKSTATE and UPDATE instructions are variable, so splitting lines is not trivial
- Nodes need to be split using `-` as a delimiter
- Printed nodes need to be split using `,` as a delimiter, sorted alphabetically and stored in an array

But, it seems to be working properly now!

```
A
B
C
LINKSTATE
A-B 2
B-C 3 B,A,C
UPDATE
A-C 1 A,C
END
Added node: A
Added node: B
Added node: C
add_link function called with arguments: A, B, 2
No nodes chosen for printing output.
add_link function called with arguments: B, C, 3
Chosen routers: A, B, C
update_link function called with arguments: A, C, 1
Chosen routers: A, C
End of input.
```

I will need to revisit this function as I implement the other functions. New lines are still not working properly, but I think I can implement within the lower level functions.

What's next?
Implementing the `add_node` function inside `Network`.

============================
Logbook Entry 15 (6:00pm, May 22, 2024)
============================

Reflection:
Implemented the `add_node` function in the `Network` class. This function now allows for the addition of new nodes to the network by checking if the node already exists and adding it if not. 

Here's a brief overview of what the function does:
- It takes the node name as a parameter.
- Checks if the node already exists in the network's nodes dictionary.
- If not, it creates a new `Node` instance, adds it to the dictionary, and prints a confirmation message.
- If the node already exists, it prints a message indicating this.

What's next?
Implementing add, update and remove links. As well as print output functions. I am leaving out implementing the routing table calculations so that I can focus on that last. 

22 May 2024 21:30:00
Kind: Text, by: a1799298, from: 118_211_67_70

============================
Logbook Entry 18 (5:52pm, May 22, 2024)
============================

Reflection:
Since my last entry, I've made significant progress on implementing key functionalities in the Network class, specifically focusing on adding, updating, and managing links between nodes. Here's a detailed summary of the work done:

1. **add_node Function:**
   - Implemented the `add_node` function to add new nodes to the network. This function checks if the node already exists before adding it, ensuring no duplicates. If the node exists, it prints a message indicating so.

2. **add_neighbor Function:**
   - Updated the `add_neighbor` function in the `Node` class to add neighboring nodes with specified link costs. This ensures that each node maintains an accurate dictionary of its neighbors and their respective link costs.

3. **add_link Function:**
   - Implemented the `add_link` function in the `Network` class to create links between nodes with specified costs. This function adds the link to both nodes' neighbor dictionaries and updates the link-state database (LSDB) with the new link.

4. **remove_neighbor Function:**
   - Implemented the `remove_neighbor` function in the `Node` class to remove a neighbor node from the neighbors dictionary. This function checks if the neighbor exists before deleting it, ensuring the neighbors list is always up-to-date.

5. **update_link Function:**
   - Implemented the `update_link` function to handle updating the cost of an existing link or adding a new link if it does not already exist. This function removes the existing neighbors, re-adds them with the new cost, and updates the LSDB accordingly. If the link does not exist, it calls the `add_link` function to create it.

What's next?
- Implementing the `remove_link` function.


============================
Logbook Entry 19 (5:58pm, May 22, 2024)
============================

Reflection:
Without much hassle, I've implemented the following:

1. **remove_link Function:**
   - Implemented the `remove_link` function to remove an existing link between two nodes and update the link-state database (LSDB). This function checks if the link exists before attempting to remove it, ensuring accurate network topology.

2. **process_input Function Update:**
   - Updated the `process_input` function to handle cases where the cost is -1, indicating a link removal. This ensures that the network can dynamically handle the removal of links based on input.

Observations:
- I have functionality for removing a link inside 'add link'. This might not be necessary, but it's good to be rigorous. 
- I'm really really glad I planned this all out beforehand. It's paying dividends

What's next?
- Implementing print output functions.

22 May 2024 23:45:00
Kind: Text, by: a1799298, from: 118_211_67_70

22 May 2024 23:45:00
Kind: Text, by: a1799298, from: 118_211_67_70

============================
Logbook Entry 20 (6:20pm, May 22, 2024)
============================

Reflection:
I've implemented the `process_input` and `print_output` functions in the `Network` class, as well as `print_neighbour`. However, I've encountered an issue where the `print_lsdb` function within the `Node` class does not have access to the `lsdb` attribute, which is part of the `Network` class.

I did touch on this in one of the first few entries, and I mistakenly said that the Node has access to the lsdb. This is wrong.

This oversight means that individual nodes cannot directly print the link-state database (LSDB) as they lack access to the global `lsdb` information stored in the `Network` class. As a result, the current implementation of the `print_lsdb` function in the `Node` class is not feasible.

What's the Fix?
- I've decided to move the `print_lsdb` function to the `Network` class and update the `print_output` function accordingly. This approach ensures that the LSDB is printed correctly using the information available in the `Network` class.

What's next?
- Move `print_lsdb` to the `Network` class and update `print_output` accordingly.
- Test the updated implementation to ensure correct functionality.

22 May 2024 23:55:00
Kind: Text, by: a1799298, from: 118_211_67_70

============================
Logbook Entry 21 (6:31pm, May 22, 2024)
============================

LSDB has now been implemented properly (sort of)

Observations
- For some reason, the example outputs in the assignment spec seem to have LSDBs instantiated on a node by node basis. My implementation works (and is more space efficient!!!), but ill have to fix this up later.

What's next?
- Implement Dijkstra in the routing table calculations  
- Implement the function to print the routing table for each node.


============================
Logbook Entry 22 (6:44pm, May 22, 2024)
============================

Reflection:
I've successfully implemented the basic version of Dijkstra's algorithm in the `Node` class to calculate routing tables.

To ensure that the routing tables are recalculated whenever the network topology changes, I updated the `add_link`, `remove_link`, and `update_link` functions in the `Network` class. These functions now call a new function, `calculate_routing_tables`, which recalculates the routing tables for all nodes in the network.

Changes made:
1. **Implemented Dijkstra's Algorithm:**
   - Added the `calculate_routing_table` method to the `Node` class to compute the shortest paths and populate the routing table.

2. **Updated Link Functions:**
   - Modified `add_link`, `remove_link`, and `update_link` in the `Network` class to call `calculate_routing_tables` after making changes to the network topology.

3. **New `calculate_routing_tables` Function:**
   - Created a new method `calculate_routing_tables` in the `Network` class to iterate over all nodes and recalculate their routing tables.

4. **Updated `print_output` Function:**
   - Ensured that the `print_output` function in the `Network` class correctly prints the routing tables for the specified nodes.

5. **Implemented `print_routing_table` Function:**
   - Added the `print_routing_table` method to the `Node` class to print the routing table in the required format.

It's working beautifully!

```
X
Y
Z
LINKSTATE
X-Z 1 X,Y
X-Y 5 
Y-Z 3 X,Z
UPDATE
X-Z -1 X,Y
Y-Z 9 Y,Z
END
X Neighbour Table:
Z|1

X LSDB:
X|Z|1

X Routing Table:
Z|Z|1

Y Neighbour Table:

Y LSDB:
X|Z|1

Y Routing Table:

X Neighbour Table:
Y|5
Z|1

X LSDB:
X|Y|5
X|Z|1
Y|Z|3

X Routing Table:
Y|Z|4
Z|Z|1

Z Neighbour Table:
X|1
Y|3

Z LSDB:
X|Y|5
X|Z|1
Y|Z|3

Z Routing Table:
X|X|1
Y|Y|3

X Neighbour Table:
Y|5

X LSDB:
X|Y|5
Y|Z|3

X Routing Table:
Y|Y|5
Z|Y|8

Y Neighbour Table:
X|5
Z|3

Y LSDB:
X|Y|5
Y|Z|3

Y Routing Table:
X|X|5
Z|Z|3

Y Neighbour Table:
X|5
Z|9

Y LSDB:
X|Y|5
Y|Z|9

Y Routing Table:
X|X|5
Z|Z|9

Z Neighbour Table:
Y|9

Z LSDB:
X|Y|5
Y|Z|9

Z Routing Table:
X|Y|14
Y|Y|9
```


What's next?
- Fix up LSDB to be instantiated within nodes, not the network itself.
- Lots and lots and lots of testing


============================
Logbook Entry 23 (12:15am, May 23, 2024)
============================

Plan for implementing LSDB Instantiation within Nodes

**Objective:**
Move the instantiation of the Link-State Database (LSDB) from the `Network` class to individual `Node` instances. This will allow each node to maintain its own LSDB, reflecting its view of the network topology.

**Steps to Implement:**

1. **Modify Node Class:**
   - Add an `lsdb` attribute to the `Node` class.
   - Initialize the `lsdb` attribute as a dictionary in the `Node` constructor.

2. **Update Network Class:**
   - Remove the `lsdb` attribute from the `Network` class.
   - Update the `add_link`, `remove_link`, and `update_link` methods to update the `lsdb` of each affected node.

3. **Adjust Link-State Database Functions:**
   - Ensure that the `print_lsdb` function in the `Node` class correctly prints the node's own LSDB.

4. **Recalculate Routing Tables:**
   - Ensure that routing tables are recalculated based on the updated LSDB information in each node.

============================
Logbook Entry 24 (8:22 PM, May 23, 2024)
============================


After implementing the routing table calculations using Dijkstra's algorithm, the next challenge was printing the Link-State Database (LSDB) for each node. Despite a comprehensive plan, this task proved more difficult than anticipated.

Initial Implementation:
- LSDB was instantiated within the Network class, representing the global network topology.
- The expected output suggested that the LSDB should be maintained and printed for individual nodes.

Refactoring:
- Moved LSDB instantiation to the Node class.
- Modified add_link, remove_link, and update_link methods in Network to update the LSDB of affected nodes.
- Updated print_lsdb method to retrieve LSDB from each node instance.

Persistent Issue:
- Output still didn't match the expected format.
- Realized that the LSDB for a node should only include links directly connected to that node, not the entire network topology.

Final Solution:
- Implemented a breadth-first search (BFS) algorithm in print_lsdb to find all reachable links from the specified node.
- This approach ensured that the LSDB output contained only the relevant links for each node.

Next Steps:
- Conduct extensive testing with various network topologies and edge cases.

============================
Logbook Entry 25 (8:00 PM, May 23, 2024)
============================

Final Reflections: Code Implementation and Development Process

As I reflect on the code implementation and development process for this assignment, there are several aspects that stand out, both in terms of what went as expected and what presented unexpected challenges.

Planning and Design:
The initial planning and design phase (Entry 4) proved to be invaluable. Breaking down the problem into smaller components, such as the Node and Network classes, and outlining their respective responsibilities and methods, provided a solid foundation for the implementation. This approach allowed me to tackle the problem in a modular and organized manner, which paid dividends as the development progressed.

Node Class Implementation:
The implementation of the Node class (Entry 7) went relatively smoothly. The concepts of object-oriented programming were fresh in my mind, and I was able to encapsulate the necessary attributes and methods effectively. The docstrings and comments helped maintain a clear understanding of the code's purpose and functionality.

Network Class Implementation:
The Network class implementation (Entry 9) presented some challenges. While the overall structure was well-planned, the intricate details of handling input processing, link updates, and output formatting required more attention than anticipated. The `process_input` method, in particular, underwent multiple iterations and refinements (Entries 12, 13, 15) to handle the various input scenarios correctly.

Dijkstra's Algorithm Implementation:
Implementing Dijkstra's algorithm (Entry 22) for calculating routing tables was a relatively straightforward process, surpisingly!

LSDB Implementation:
The implementation of the Link-State Database (LSDB) proved to be one of the most challenging aspects of this assignment. Initially, I had implemented the LSDB within the Network class (Entry 21), but later realized that it should be maintained and printed for each individual node based on the expected output format (Entry 23). 

The breakthrough moment came when I implemented the Breadth-First Search (BFS) algorithm in the `print_lsdb` method to find all reachable links from a specified node (Entry 24). This approach ensured that the LSDB output contained only the relevant links for each node, as per the requirements.

Testing and Debugging:
The program has been tested quite minimally (only with the given example), so I still have lots more to do. I will be submitting for the first time now, and seeing how I go! 

Overall, the code implementation and development process for this assignment presented a mix of expected and unexpected challenges. While some aspects went as planned, others required more effort and iterative refinement than initially anticipated. 