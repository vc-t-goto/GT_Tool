import bpy
# -*- coding: utf-8 -*-

class GT_BoneMerge(bpy.types.Operator):
    bl_idname = "gt_tool.gt_bone_merge"
    bl_label = "GT_Bone_Merge"
    bl_description = "---使い方--- 対象メッシュ、アーマチュアの順に選択してエディットモードに入る。ボーンを複数選択する。このときまとめる先のボーンを最後に選択する。ボタンを押す。"

    def execute(self, context):         
        ##Blender2.9 running
        ##オブジェクト（ウェイト対象）アーマチュアの順で選択、そのままEditに入り対象ボーンのみ選択、
        ##その状態のまま再生ボタンを押す

        #ウェイト結合してボーンを消してくれる
        #editmodeはポーズではなく編集になるように

        #メッシュ、アーマチュアの順で複数選択
        #その後編集モードに入りボーンを複数選択
        objs= bpy.context.selected_objects

        merge_root=None#string名称指定無しのとき、最後に選択したボーンを親にする
        if merge_root == None:
            merge_root = bpy.context.active_bone.name

        #名前指定しない場合 None は、編集モードで複数選択しているボーンが指定される
        merge_branch=None


        #選択順によりたまにローカルで順番が変わるため修正判定
        if objs[0].type == "ARMATURE":
            obj = objs[1]#2.9で修正 #はじめに選択するObject(weight having object)
            arma = objs[0]#2.9で修正 #次に選択するObject(armature object)
        else:
            obj = objs[0]#2.9で修正 #はじめに選択するObject(weight having object)
            arma = objs[1]#2.9で修正 #次に選択するObject(armature object)


        #頂点グループ結合後ボーンを消すかどうか
        is_bonedelete = True


        def weight_merge(merge_root,merge_branch,arma,is_bonedelete,obj):
            bpy.context.view_layer.objects.active=obj
            bpy.ops.object.mode_set(mode='EDIT')

            bpy.ops.object.modifier_add(type='VERTEX_WEIGHT_MIX')
            bpy.context.object.modifiers["VertexWeightMix"].vertex_group_a = merge_root
            bpy.context.object.modifiers["VertexWeightMix"].vertex_group_b = merge_branch
            bpy.context.object.modifiers["VertexWeightMix"].mix_mode = 'ADD'
            bpy.context.object.modifiers["VertexWeightMix"].mix_set = 'ALL'
            bpy.ops.object.modifier_move_up(modifier="VertexWeightMix")
            bpy.ops.object.modifier_move_up(modifier="VertexWeightMix")
            bpy.ops.object.modifier_move_up(modifier="VertexWeightMix")
            bpy.ops.object.modifier_move_up(modifier="VertexWeightMix")
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.modifier_apply(modifier="VertexWeightMix")#2.9で修正


            vg=bpy.context.object.vertex_groups.get(merge_branch)


            if vg is not None:
                bpy.ops.object.vertex_group_set_active(group=merge_branch)
                bpy.ops.object.vertex_group_remove(all=False, all_unlocked=False)
            obj.select_set(False)
            #bpy.data.objects[arma].select_set(True)#2.8で修正
            #bpy.context.view_layer.objects.active=bpy.data.objects[arma] #active
            bpy.context.view_layer.objects.active=arma
            bpy.ops.object.mode_set(mode='EDIT')

            if is_bonedelete == True:
                bone =bpy.context.object.data.edit_bones.get(merge_branch)#2.8で修正
                bpy.context.object.data.edit_bones.remove(bone)


            bpy.ops.object.mode_set(mode='OBJECT')
            return
        
        #kansuu
        #名前指定しない場合 None は、編集モードで複数選択しているボーンが指定される
        if merge_branch == None:
            selected_bones = bpy.context.selected_editable_bones
            bo_name=[]
            if selected_bones != None:
                for bo in selected_bones:
                    bo_name.append(bo.name)
                
                for merge_branch in bo_name:
                    #結合先親と今参照してるボーンの名称が同じときは無視する
                    if merge_branch != merge_root:
                        bpy.context.view_layer.objects.active=obj
                        weight_merge(merge_root,merge_branch,arma,is_bonedelete,obj)
        else:
            bpy.context.view_layer.objects.active=obj
            weight_merge(merge_root,merge_branch,arma,is_bonedelete,obj)
        return {'FINISHED'}
