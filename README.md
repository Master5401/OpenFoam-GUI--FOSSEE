# OpenFOAM-Blender Bridge (FOSSEE Internship)

A modular Blender Add-on designed to automate OpenFOAM case setup, bridging the gap between 3D geometric modeling and CFD pre-processing.

## Current Status: M4 Geometric Extraction (Week 4)
The current build has advanced from basic Middleware to the **Mesh Generation Engine**. It successfully translates Blender's 3D bounding box data into OpenFOAM's strict 8-point Hex standard, generating the required background mesh dictionaries.

### Features
* **Geometric Translation:** Automatically calculates mesh bounding boxes and formats vertex arrays.
* **SimFlow-Style Interface:** Persistent N-Panel architecture mimicking standard CFD sequential pipelines (Workspace -> Physics -> Mesh -> Runtime).
* **Data Persistence:** Utilizes Blender's `PointerProperty` to securely bind simulation parameters to the `.blend` file metadata.
* **Automated Dictionary Generation:** Validates OS-level paths and automatically generates `system/controlDict` and `system/blockMeshDict`.

## Installation
1. Download this repository as a `.zip` file.
2. In Blender, navigate to `Edit > Preferences > Add-ons > Install...`
3. Select the `.zip` file and enable the "OpenFOAM Blender Bridge" add-on.

## Technical Architecture
This add-on is structured for scalability to allow future integration of Boundary Condition modules:
* `__init__.py`: Handles core Blender API registration.
* `properties.py`: The data layer; defines the OpenFoamProperties class.
* `ui.py`: The presentation layer; defines the `VIEW_3D` panel.
* `operators.py`: The logic layer; handles math translation, string parsing, and OS-level file I/O operations.
