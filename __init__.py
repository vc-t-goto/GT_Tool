bl_info = {
    "name": "GT Tool",
    "author": "raikohGT",
    "version": (1, 0),
    "blender": (2, 90, 0),
    "location": "location",
    "description": "GT Toolです。自分用の便利ツールまとめです。",
    "warning": "使用は自己責任です。at your own risk",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "https://twitter.com/kurohune",
    "category": "Object"
}


if "bpy" in locals():
    import imp
    #項目に応じて追記--pyファイル名--------------------------------
    imp.reload(gt_bone_merge)
    imp.reload(gt_weightnormalize)
    imp.reload(gt_addbone)
else:
    #項目に応じて追記--pyファイル名---------------------------------
    from . import gt_bone_merge
    from . import gt_weightnormalize
    from . import gt_addbone

import bpy

#Main Panel
class GT_Panel(bpy.types.Panel):
    bl_label = "GT Tool"
    bl_idname = "gt_tool.gt_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "GT Tool"

    def draw(self, context):
        layout = self.layout
        #項目に応じて追記--pyファイル名---------------------------------
        layout.operator("gt_tool.gt_bone_merge")
        layout.operator("gt_tool.gt_weightnormalize")
        layout.operator("gt_tool.gt_addbone")


# Blenderに登録するクラス
#項目に応じて追記--pyファイル名,関数名---------------------------------
classes = [
    GT_Panel,
    gt_bone_merge.GT_BoneMerge,
    gt_weightnormalize.GT_Weightnormalize,
    gt_addbone.GT_AddBone,
]


# アドオン有効化時の処理
def register():
    for c in classes:
        bpy.utils.register_class(c)
    print("有効化されました。")


# アドオン無効化時の処理
def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    print("無効化されました。")


if __name__ == "__main__":
    register()