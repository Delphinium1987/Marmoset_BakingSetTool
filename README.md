# 使用说明
本工具用于为 Marmoset 设置烘焙组。能够自动将模型高低模物体对应分配到不同的烘焙组中。
> 该工具通过 _High/Low 后缀识别高模低模，且需要高模/低模名称能够对应。

## 高模低模分别导入
对于分别导入的模型，选中 **High 模型 FBX**，点击 **High** 按钮建立 BakeProject，并将高模分别分配到烘焙组中。
此时选中 **Low 模型 FBX**，点击 **Low** 按钮，低模会对应移动到相应烘焙组中。

![GIF](https://github.com/user-attachments/assets/706a7cc9-6f55-49c1-adb6-1fcad36633c5)

## 高模低模合并导入
如果 FBX 中同时包含 High 和 Low 模型物体。点击** Set Bake HtoL **按钮，建立 BakeProject，并自动将模型一一对应分配到烘焙组中。

![GIF2](https://github.com/user-attachments/assets/3c0b93da-b3e1-407d-8486-62e2bb7ddee1)
