# Network Graph Task

This small program allows a user to set-up and input their own configuration file for a network, and receive an output file that provides a description of the network, including all links between nodes, the weights of those links, and the weights of the nodes themselves. A sample configuration file are provided as "config.txt" and "graph_output.txt" respectively.

#### A configuration file requires the following format:

Line 1: Number of Nodes Requested  <br />
Line 2: Topology of Network (Linear, Full, Star, or Random)  
Line 3: Alpha Number (Enter 0 if not using Random topology)  
Line 4: Minimum Node Weight  
Line 5: Maximum Node Weight  
Line 6: Minimum Link Weight  
Line 7: Maximum Link Weight

NOTE: Please enter these numbers and topology selection without any additional labeling.

#### The output file you receive should have the following format:

Line 1: "First node" "Second node" Link weight <br />
Line 2: "First node" "Second node" Link weight <br />
. <br />
. <br /> 
. <br />
Line N-1: "First node" "Second node" Link weight <br />
Line N: "Node0 weight" "Node1 weight" . . . "NodeN Weight"

Compile the file using g++ or a C++ compiler of your choice. You will be asked to enter a configuration file name upon running the executable.

Email conlonej@slu.edu with any additional questions.

