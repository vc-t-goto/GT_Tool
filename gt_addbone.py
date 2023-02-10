import bpy
# -*- coding: utf-8 -*-

class GT_AddBone(bpy.types.Operator):
    bl_idname = "gt_tool.gt_addbone"
    bl_label = "GT_AddBone"
    bl_description = "ボーンの先端を選択し、実行で子ボーンを１つ接続無しで生成し、選択状態にする。"

    def execute(self, context):
        # add child bone without joint, select front end of bone and play,
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(1, -0, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        bpy.ops.armature.select_more()
        bpy.ops.armature.parent_clear(type='DISCONNECT')

        return {'FINISHED'}
