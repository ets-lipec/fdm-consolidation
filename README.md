# 3D Printing Problem

The problem is studied in 1D.

A filament of polymer (ABS) is extruded of a nozzle and deposited at a time 0 on a heated platform whose temperature is defined in ["Experimental Conditions"] ["Bed Temperature"]. This temperature is considered constant during all the experience, not affected by the deposition of the polymer.

Then, other filaments are deposited at regular intervals on top of each other. Their thickness, the time between 2 filament depositions and the number of filaments are defined by the user in ["Experimental Conditions"] ["Layer Thickness"], ["Simulation"] ["Time per layer"] and ["Experimental Conditions"] ["Number of Layers"], respectively. They are deposited at a temperature defined by the experimenter in ["Experimental Conditions"] ["Extrusion Temperature"].

Once the layers have been deposited, the platform stays at high temperature during a time defined by the user in ["Simulation"] ["Time before cooling"]. Then, it cools linearly at a speed defined in ["Simulation"] ["Vcooling"] until it reaches the room temperature also defined by the user in ["Experimental Conditions"] ["RoomTemperature"].

By using the finite differences for the heat transfer equation, the user determines the temperature for every space element, defined in ["Simulation"] ["Number of intervals per layer"], at every time step, fixed in the code to respect the stability criterion.

```yaml
Materials:
  Mechanical:
    Coefficient of Thermal Expansion: 0.000041
    Density: 1250
  Thermal:
    Heat Transfer Coefficient: 100
    Thermal Conductivity: 0.13
    Heat Capacity: 1800

Experimental Conditions:
  Extrusion Temperature: 453
  Bed Temperature: 338
  Room Temperature: 295
  Layer Thickness: 0.0008
  Number of Layers: 3

Simulation:
  Number of intervals per layer: 4
  Time per layer: 20
  Vcooling: 0.5
  Time before cooling: 60
  Time after cooling: 60
```

# Operation

### Matrix Generation

A class named "Matrix Generation" creates a matrix to solve the heat transfer equation. Its length depends on the number of filaments deposited. It also defines the boundary conditions and the initial conditions of temperature.

### Resolution

A class named "Temperature" solves the heat transfer equation by finite differences for every element at every time step. A class named "flow" calculates the convection and conduction flows at the contact between the polymer and the air or the platform. A class named "healing" calculates the evolution of the healing between the layers.

### Plot

A class named "Graph" creates graphs representing the evolution of the temperature for every element, the conductive and convective flows and the healing between every filament at every time step. A class named "Animation" generates a 2D figure of the temperature at regular intervals and then creates a GIF of those figures. A class named "Stability" also generates a graph of time stability for different values of time steps.

# Usage

```linux
git clone https://github.com/ets-lipec/consolidation-works.git
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
python main.py
```