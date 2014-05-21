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
    for i in range(1, 2):
        newOrigin = add_vectors(origin, [random.uniform(-2, 2), random.uniform(-2, 2), 0])
        verts, edges = generate_polystrip()
        ob = createMesh('g', newOrigin, verts, edges, [])    
        ob.show_name = False
    return

# generates 2 tupels, one with the verts and one with the indices for edges
def generate_polystrip(steps = 5, height = 0.2):
    verts = generate_points(steps = 7, height = 1)
    edges = []
    
    for i in range(1, len(verts)):
        edges.append((i - 1, i))     
        
    return (verts, edges)

# generate point list
def generate_points(steps = 4, height = 1):
    verts = []
    
    lastPosition = [0, 0, 0]
    verts.append(lastPosition)
    
    size = height / steps
    changeVector = [random.uniform(-size / 4, size / 4), random.uniform(-size / 4, size / 4), size]
    
    for i in range(1, steps):   
        changeAmount = linear_interpolation(size * 2, size / 10, i / steps)
        directionChangeVector = [random.uniform(-changeAmount, changeAmount), random.uniform(-changeAmount, changeAmount), random.uniform(-changeAmount / 1.5, changeAmount * 1.3)]
        changeVector = add_vectors(changeVector, directionChangeVector)
        multiply_vector(changeVector, 0.9)
        newPosition = add_vectors(lastPosition, changeVector)
        verts.append(newPosition)
        
        lastPosition = newPosition
        
    return verts

def normalize_vector(v):
    lenght = math.sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2])
    v[0] /= lenght
    v[1] /= lenght
    v[2] /= lenght

def multiply_vector(v, value):
    v[0] *= value
    v[1] *= value
    v[2] *= value
    
def set_length(vector, length):
    normalize_vector(vector)
    multiply_vector(vector, length)

def add_vectors(v1, v2):
    return [v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2]]

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
