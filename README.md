# GT_Tool
Blenderの自分用便利アドオンまとめ My Blender very very nice addon
GT_tool

v1.0.0  2022/12/04
v1.1.0  2023/02/10 GT_AddBone追加
v1.2.0  2023/02/10 GT_DelVertexGroup追加



自分用のBlender便利ツールまとめです。
使用は自己責任でお願いします。

■GT_BoneMerge
ボーンをたくさん選択してそれらのボーンが持つウェイトを全て１つのボーンに転送する機能です。

対象メッシュ、アーマチュアの順に選択してエディットモードに入る。ボーンを複数選択する。このときまとめる先のボーンを最後に選択する。ボタンを押す。

■GT_Weightnormalize
頂点の持つウェイトをきれいにする機能です。
頂点１つあたりのボーンの制限数４で、ウェイトの合計1.0になるように正規化します。

■GT_AddBone
いちいち子ボーンの接続を切るのが面倒だったので作成した。
編集メニューで使用。　ボーンの先端を選択し、実行で子ボーンを１つ接続無しで生成し、選択状態にする。

■GT_DelVertexGroup
オブジェクトを選択して実行。未使用の頂点グループを削除する。




・インストール
zipをBlenderアドオンのインストールから導入してください
横のバーに追加されます。隠れてたら「N」キーで枠が出てきます。


![image](https://user-images.githubusercontent.com/43428951/205498092-70a17412-3396-49a1-930b-05451c26af00.png)


・アンインストール
アドオンの一覧からGT_Toolを削除してください





連絡はGitHubかtwitterにお願いします
https://github.com/vc-t-goto/GT_Tool


-----------------------------------------------
Copyright (c) 2022 raikohGT
Released under the MIT license
https://opensource.org/licenses/mit-license.php
