import bpy
# -*- coding: utf-8 -*-

class GT_Weightnormalize(bpy.types.Operator):
    bl_idname = "gt_tool.gt_weightnormalize"
    bl_label = "GT_Weightnormalize"
    bl_description = "メッシュのボーンウェイトを1頂点あたり制限数4で正規化する。対象メッシュを1つ選択してからボタンを押す"

    def execute(self, context):
        bpy.ops.object.mode_set(mode='WEIGHT_PAINT')

        bpy.ops.object.vertex_group_limit_total(group_select_mode='ALL', limit=4)
        bpy.ops.object.vertex_group_normalize_all(group_select_mode='ALL', lock_active=False)
        bpy.ops.object.vertex_group_clean(group_select_mode='ALL', limit=0.001, keep_single=True)
        bpy.ops.object.vertex_group_normalize_all(group_select_mode='ALL', lock_active=False)

        bpy.ops.object.mode_set(mode='OBJECT')
        
        return {'FINISHED'}