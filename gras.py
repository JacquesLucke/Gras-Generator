import bpy
 
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
    
    ob1 = createMesh('Solid', origin, verts, [], faces)
    
    return

# generates 2 tupels, one with the verts and one with the indices for faces
def generate_polystrip(steps = 2, width = 0.7, height = 3, topScale = 0.3):
    verts = []
    faces = []
    
    heightPerStep = height / steps
    halfWidth = width / 2
    
    verts.append((halfWidth, 0, 0))
    verts.append((-halfWidth, 0, 0))
    
    for i in range(1, steps + 1):
        hWidth = linear_weight(halfWidth * topScale, halfWidth, i / steps)
        print(hWidth)
        verts.append((hWidth, 0, i * heightPerStep))
        verts.append((-hWidth, 0, i * heightPerStep))
        
        faces.append((2*i - 2, 2*i - 1, 2*i + 1, 2*i))
        
    return (verts, faces)

def linear_weight(val1, val2, weight):
    return val1 * weight + val2 * (1 - weight)
 
if __name__ == "__main__":
    run((0,0,0))