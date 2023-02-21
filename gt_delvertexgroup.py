import bpy
# -*- coding: utf-8 -*-
#reference:::::https://scrapbox.io/keroxp/Blender%E3%81%A7%E3%82%A6%E3%82%A7%E3%82%A4%E3%83%88%E3%81%AE%E3%81%AA%E3%81%84%E9%A0%82%E7%82%B9%E3%82%B0%E3%83%AB%E3%83%BC%E3%83%97%E3%82%92%E3%81%99%E3%81%B9%E3%81%A6%E5%89%8A%E9%99%A4%E3%81%99%E3%82%8B

class GT_DelVertexGroup(bpy.types.Operator):
    bl_idname = "gt_tool.gt_delvertexgroup"
    bl_label = "GT_DelVertexGroup"
    bl_description = "オブジェクトを選択して実行。未使用の頂点グループを削除"

    def execute(self, context):   
        def survey(obj):
            maxWeight = {}
            nameByIndex = {}
            indexByName = {}
            for vg in obj.vertex_groups:
                maxWeight[vg.index] = 0
                nameByIndex[vg.index] = vg.name;
                indexByName[vg.name] = vg.index;
            for v in obj.data.vertices:
                for g in v.groups:
                    gn = g.group
                    w = obj.vertex_groups[g.group].weight(v.index)
                    if (maxWeight.get(gn) is None or w > maxWeight[gn]):
                        maxWeight[gn] = w
            return maxWeight, nameByIndex, indexByName
        # bone_name.(l|L) <-> bone_name.(r|R)
        mirroredNameMap = {"L": "R", "R":"L", "l": "r", "r": "l"}
        def getMirroredName(name):
            prefix = mirroredNameMap.get(name[-1])
            return name[0:-1]+prefix if prefix is not None else name

        def __main__():
            obj = bpy.context.active_object
            maxWeight, nameByIndex, indexByName = survey(obj)
            print(indexByName)
            ka = []
            ka.extend(maxWeight.keys())
            ka.sort(key=lambda gn: -gn)
            removalFlags = {}
            for gn in ka:
                if removalFlags.get(gn) is not None:
                    continue
                removalFlags[gn] = maxWeight[gn] <= 0
                group_name = nameByIndex[gn]
                mirror = getMirroredName(group_name)
                mirror_index = indexByName.get(mirror)
                if mirror_index is not None:
                    if removalFlags.get(mirror_index) is None:
                        removalFlags[gn] = maxWeight[gn] <= 0
                    if maxWeight[gn] > 0 or maxWeight[mirror_index] > 0:
                        removalFlags[gn] = removalFlags[mirror_index] = False
                else:
                    removalFlags[gn] = maxWeight[gn] <= 0
            for gn in ka:
                if removalFlags[gn]:
                    obj.vertex_groups.remove(obj.vertex_groups[gn])
                    print ("deleted: "+nameByIndex[gn])
        __main__()
        return {'FINISHED'}
