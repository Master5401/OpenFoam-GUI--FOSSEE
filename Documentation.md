# OpenFOAM-Blender Bridge (FOSSEE Internship)

A modular Blender Add-on designed to automate OpenFOAM case setup, bridging the gap between 3D geometric modeling and CFD pre-processing. 

## Current Status: Middleware Automation (Week 3/4)
The current build focuses on the **Runtime Middleware**. It translates Blender scene data into OpenFOAM's native C++ ASCII dictionary format, mitigating human syntax errors during simulation setup.

### Features
* **SimFlow-Style Interface:** Persistent N-Panel architecture mimicking standard CFD sequential pipelines (Workspace -> Physics -> Runtime).
* **Data Persistence:** Utilizes Blender's `PointerProperty` to securely bind simulation parameters to the `.blend` file metadata.
* **Automated Dictionary Generation:** Validates OS-level paths and automatically generates the `system/controlDict` file.

## Screenshots

![UI Demo](ui_demo.png)
> **Fig 1:** The persistent SimFlow-style configuration panel within the Blender 3D Viewport.

![Output Demo](output_demo.png)
> **Fig 2:** Real-time data mapping from the Blender UI to the generated `controlDict` ASCII file.

## Installation
1. Download this repository as a `.zip` file.
2. In Blender, navigate to `Edit > Preferences > Add-ons > Install...`
3. Select the `.zip` file and enable the "OpenFOAM Blender Bridge" add-on.

## Technical Architecture
This add-on is structured for scalability to allow future integration of Mesh and Boundary Condition modules:
* `__init__.py`: Handles core Blender API registration.
* `properties.py`: The data layer; defines the OpenFoamProperties class.
* `ui.py`: The presentation layer; defines the `VIEW_3D` panel.
* `operators.py`: The logic layer; handles string parsing and OS-level file I/O operations.
