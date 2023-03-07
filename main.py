import bpy
import os
import sys
# 设置 FBX 文件夹路径和缩放比例
fbx_folder = r"C:\Users\DELL\Desktop\iso\FBX_new"
fbx__save_folder = r"C:\Users\DELL\Desktop\iso\FBX_out"
scale_factor = 0.01


for file in os.listdir(fbx_folder):
    if file.endswith(".fbx"):
        bpy.ops.import_scene.fbx(filepath=os.path.join(fbx_folder, file))
        del_name = []
        for name in bpy.data.objects.keys():
            obj = bpy.data.objects[name]
            if "Camera" in name or "Cube" in name or "Light" in name:
                bpy.data.objects.remove(obj)
            else:
                obj.scale = (0.01, 0.01, 0.01)
                del_name.append(name)
        bpy.ops.export_scene.fbx(filepath=os.path.join(fbx__save_folder, file))
        for del_n in del_name:
            bpy.data.objects.remove(bpy.data.objects[del_n])


