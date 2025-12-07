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

## 模型显示和烘焙
ShowModel 页签下的按钮用于快速切换高模/低模显示，**Bake **按钮可用于贴图烘焙，和官方面板按钮功能相同。


## Tips
本工具本来是用于我自己的工作流的，一部分功能和 Blender 插件配合工作，应群友要求开源，部分不通用的功能做了删除处理（比如 LowtoLow 工作流）。
现在 AI 编程流行，我自己是不太擅长 Python 的，部分功能参考了 AI 的教学和指导。在此感谢 Deepseek 老师。
