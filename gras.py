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
def generate_polystrip():
    verts = []
    faces = []
    
    verts.append((0.5, 0, 0))
    verts.append((-0.5, 0, 0))
    
    for i in range(1, 5):
        verts.append((0.5, 0, i))
        verts.append((-0.5, 0, i))
        
        faces.append((2*i - 2, 2*i - 1, 2*i + 1, 2*i))
        print(faces[i - 1])
        
    return (verts, faces)
 
if __name__ == "__main__":
    run((0,0,0))