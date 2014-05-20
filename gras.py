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
    verts = ((0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0),  (0, 2, 0), (1, 2, 0))
    faces = ((0, 1, 2, 3), (3, 2, 5, 4))
    ob1 = createMesh('Solid', origin, verts, [], faces)
    
    return
 
if __name__ == "__main__":
    run((0,0,0))