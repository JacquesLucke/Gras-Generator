import bpy

class ToolsPanel(bpy.types.Panel):
    bl_label = "Make Gras"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
 
    def draw(self, context):
        layout = self.layout
        
        row = layout.row(align=True)
        row.operator("makegras.button")
        
class OBJECT_OT_Button(bpy.types.Operator):
    bl_idname = "makegras.button"
    bl_label = "Make Gras"
    number = bpy.props.IntProperty()
    row = bpy.props.IntProperty()
    loc = bpy.props.StringProperty()
 
    def execute(self, context):
        print("erfolgreich")
        return{'FINISHED'} 

bpy.utils.register_module(__name__)