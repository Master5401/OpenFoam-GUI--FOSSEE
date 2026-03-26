import bpy

class OpenFoamProperties(bpy.types.PropertyGroup):
    case_dir: bpy.props.StringProperty(
        name="Case Path",
        subtype='DIR_PATH',
        description="Path to OpenFOAM case"
    )
    solver: bpy.props.EnumProperty(
        name="Solver",
        items=[('icoFoam', "icoFoam", "Incompressible"),
               ('simpleFoam', "simpleFoam", "Steady State")]
    )
    end_time: bpy.props.FloatProperty(name="End Time", default=10.0, min=0.1)
    delta_t: bpy.props.FloatProperty(name="Delta T", default=0.005, min=0.0001, precision=4)
    write_interval: bpy.props.IntProperty(name="Write Interval", default=20, min=1)
    
    mesh_res_x: bpy.props.IntProperty(name="X Cells", default=15, min=1, description="Grid resolution in X")
    mesh_res_y: bpy.props.IntProperty(name="Y Cells", default=15, min=1, description="Grid resolution in Y")
    mesh_res_z: bpy.props.IntProperty(name="Z Cells", default=15, min=1, description="Grid resolution in Z")
