Algorithm

Import Libraries:
Import required modules from the kanren library: Relation, facts, run, var, and conde.

Define Relations:
Define relations such as doctor and treats.

Insert Facts into the Knowledge Base:
Use facts() to define who is a doctor and which patients they treat.

Define Rule:
Create a rule is_skilled(p) such that:

A person p is a doctor, and

The doctor p treats at least one patient.

Accept User Query:
Take user input (e.g., “Who is skilled?” or “Is dr_lee skilled?”).

Perform Reasoning:

Use run() with the defined rule to retrieve all skilled doctors.

If the query starts with "who", list all skilled doctors.

If the query starts with "is", check whether the specified doctor is in the skilled list.

Otherwise, mark the query as invalid.

Display Result:

Print the list of skilled doctors if the query is “who”.

Print Yes/No if the query is “is”.

Print an error message for invalid queries.

----------------------------------------------------------------------------------------------------------------------------

Algorithm: A* Search

Start the program.

Initialize data structures:

Create a priority queue open_list and insert the start node with
f(start) = g(start) + h(start) where g(start) = 0.

Create an empty set visited to track explored nodes.

Repeat until open_list is empty:
a. Remove the node with the lowest f(n) from open_list.
b. If this node is the goal node, return the path and exit.
c. If the node is not visited yet:

Mark it as visited.

For each neighbor of the node:
i. Compute g(neighbor) = g(current) + edge_cost.
ii. Compute f(neighbor) = g(neighbor) + h(neighbor).
iii. Add neighbor, updated path, and cost to open_list.

If the queue becomes empty without finding the goal, output “No path found.”

End the program.