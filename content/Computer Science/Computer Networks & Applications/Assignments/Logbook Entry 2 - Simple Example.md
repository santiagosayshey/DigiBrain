
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
Logbook Entry 14 (4:43pm, May 22, 2024)
============================

`process_input` isn't going that well. I decided to scrap what I had. It was too confusing to continue. Going to approach each type of line one at a time now