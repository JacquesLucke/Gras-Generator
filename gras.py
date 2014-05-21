import bpy
import random
import math

random.seed(); 
 
def createMesh(name, origin, verts, edges, faces):
    # Create mesh and object
    me = bpy.data.meshes.new(name+'Mesh')
    ob = bpy.data.objects.new(name, me)
    ob.location = origin
    ob.show_name = True
    # Link object to scene
    bpy.context.scene.objects.link(ob)
 
    # Create mesh from given verts, edges, faces. Either edges or
    # faces should be [], or you ask for problems
    me.from_pydata(verts, edges, faces)
 
    # Update mesh with new data
    me.update(calc_edges=True)
    return ob
 
def run(origin):
    verts, faces = generate_polystrip()
    
    ob = createMesh('Solid', origin, verts, [], faces)    
    return

# generates 2 tupels, one with the verts and one with the indices for faces
def generate_polystrip(steps = 10, width = 0.4, height = 3, topScale = 0.2):
    verts = []
    faces = []
    
    halfWidth = width / 2
    
    direction = [0, 0, 1]
    growSpeed = height / steps
    
    
    verts.append([halfWidth, 0, 0])
    verts.append([-halfWidth, 0, 0])
    
    for i in range(1, steps + 1):
        hWidth = linear_interpolation(halfWidth * topScale, halfWidth, i / steps)
        
        vert1 = [hWidth, 0, i * growSpeed]
        vert2 = [-hWidth, 0, i * growSpeed]
        verts.append(vert1)
        verts.append(vert2)
        
        faces.append((2*i - 2, 2*i - 1, 2*i + 1, 2*i))
        
    return (verts, faces)

def normalize_vector(v):
    lenght = math.sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2])
    v[0] /= lenght
    v[1] /= lenght
    v[2] /= lenght
    return v

def multiply_vector(v, value):
    v[0] *= value
    v[1] *= value
    v[2] *= value
    return v

def add_vectors(v1, v2):
    v1[0] += v2[0]
    v1[1] += v2[1]
    v1[2] += v2[2]
    return v1

def linear_interpolation(val1, val2, weight):
    return val1 * weight + val2 * (1 - weight)

def gradient_interpolation(gradient, value):
    index = (len(gradient) - 1) * value
    if round(index) == index:
        return gradient[int(index)]
    indexDown = math.trunc(index)
    indexUp = math.ceil(index)
    val = linear_interpolation(gradient[indexDown], gradient[indexUp], (value - 1 / len(gradient) * indexDown) * len(gradient))
    print(val)
    return val
    
    
    
# Interface ----------------------------------------------   
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
        run((0,0,0))
        return{'FINISHED'} 

bpy.utils.register_module(__name__)
