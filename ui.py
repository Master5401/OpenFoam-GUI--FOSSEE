import bpy


class OPENFOAM_PT_Sidebar(bpy.types.Panel):
    bl_label = "SimFlow Bridge"
    bl_idname = "OPENFOAM_PT_Sidebar"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'OpenFOAM'

    def draw(self, context):
        layout = self.layout
        props = context.scene.openfoam_props

        box = layout.box()
        box.label(text="Workflow: Setup", icon='PROPERTIES')
        box.prop(props, "case_dir")

        box = layout.box()
        box.label(text="Physics", icon='PHYSICS')
        box.prop(props, "solver")

        box = layout.box()
        box.label(text="Runtime", icon='TIME')
        box.prop(props, "end_time")
        box.prop(props, "delta_t")
        box.prop(props, "write_interval")

        layout.operator("openfoam.write_config", icon='FILE_TICK')