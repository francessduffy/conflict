# IntrastateConflict
Agent-Based Model of Militant and Civilian interactions during an intrastate conflict


To initiate the program, run output.py. To print results or change the displayed graphs, make changes to this file. It also produces an Excel spreadsheet in the "data" folder called "dataset."

It executes simulation.py, which runs the main program (main.py) a default of ten times and displays an average of the results.

In order to run one simulation, change the "import" statement in output.py "from simulation" to "from simulationonce". To run forty simulations, change the "import" statement in output.py "from simulation" to "from simulationforty". 

To change initial conditions of the environment, make changes to initconditions.py. 

To change initial characteristics of militants, make changes to militant.py, function "generateMilitants"

To add communities, make changes to community.py, function "generateCommunities" and update region.py,  "generateRegions". Changes may also be necessary to "wealths," "grievances," and "affiliations" matrices in initconditions.py.

The following files are used only to create/handle output variables within each simulation: variables.py, results.py

The following files are used only to create/handle output variables outside of the simulator: dfdata.py, militantdata.py
