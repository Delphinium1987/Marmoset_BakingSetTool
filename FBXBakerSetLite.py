# -*- coding: utf-8 -*-
import mset
import re
import os

def bakerSetBetweenHighAndLow():
    selection = mset.getSelectedObject()    
    if selection == None:
        mset.err("Please select your model!!")
        return

    if "Bake Project" in selection.name:
        mset.err("You are selecting the bake project!!")
        return
      
    #移除旧的烘焙对象。
    oldBakeProject = mset.findObject("Bake Project 1")
    if oldBakeProject != None:
        oldBakeProject.destroy()
        
     #创建新的烘焙对象。
    newBakeProject = mset.BakerObject()
    newBakeProject.name = "Bake Project 1"
    outputMapSet()

    lowModel = mset.SceneObject.duplicate(selection)
    lowModel.name = selection.name + "_Low"
    
    objlist_High = selection.getChildren()
    for i in range(len(objlist_High)-1,-1,-1):
        if "_Low" in objlist_High[i].name:
            objlist_High[i].destroy()
    objlist_Low = lowModel.getChildren()
    for i in range(len(objlist_Low)-1,-1,-1):
        if "_High" in objlist_Low[i].name:
            objlist_Low[i].destroy()

    #重新 GetChildren 从而清除上一步删除造成的空元素。    
    objlist_High = selection.getChildren()
    objlist_Low = lowModel.getChildren()

    #获取材质名称列表，用于接下来的判定。
    materialListName = []
    materialList = mset.getAllMaterials()
    for i in range(0,len(materialList),1):
        materialListName.append(materialList[i].name)

    for i in range(len(objlist_Low)-1,-1,-1):
        if "Bake_High" in materialListName and "Bake_Low" in materialListName:
            mset.findMaterial("Bake_High").assign(objlist_High[i])
            mset.findMaterial("Bake_Low").assign(objlist_Low[i])


    #根据 Mesh 数量创建烘焙组。此处要递减进行，以适应场景中排序。   
    for i in range(len(objlist_Low)-1,-1,-1):
        group = newBakeProject.addGroup("Bake_Group_" + str(i))
        high = group.findInChildren("High")
        low = group.findInChildren("Low")  
        #设置父级
         #设置High
        objlist_High[i].parent = high
        #根据命名匹配一个 Low 对象
        for j in range(0,len(objlist_Low),1):
            lowname = re.sub(r'_Low$', '', objlist_Low[j].name)
            highname = re.sub(r'_High$', '', objlist_High[i].name)

            if lowname == highname:
                 objlist_Low[j].parent = low



    #最后销毁 lowModel，因为 lowModel 中的物体都已经移动至烘焙组。
    lowModel.destroy() 

def setBakerHigh():
    selection = mset.getSelectedObject()    
    if selection == None:
        mset.err("Please select your model!!")
        return

    if "Bake Project" in selection.name:
        mset.err("You are selecting the bake project!!")
        return
      
    #移除旧的烘焙对象。
    oldBakeProject = mset.findObject("Bake Project 1")
    if oldBakeProject != None:
        oldBakeProject.destroy()
    objlist_High = selection.getChildren()

     #创建新的烘焙对象。
    newBakeProject = mset.BakerObject()
    newBakeProject.name = "Bake Project 1"
    outputMapSet()

    #根据 Mesh 数量创建烘焙组。此处要递减进行，以适应场景中排序。   
    for i in range(len(objlist_High)-1,-1,-1):
        group = newBakeProject.addGroup("Bake_Group_" + str(i))
        high = group.findInChildren("High")
        #设置父级
         #设置High
        objlist_High[i].parent = high    

def setBakerLow():
    selection = mset.getSelectedObject()    
    if selection == None:
        mset.err("Please select your model!!")
        return

    if "Bake Project" in selection.name:
        mset.err("You are selecting the bake project!!")
        return
      
    #搜索是否存在烘焙对象。
    bakeProject = mset.findObject("Bake Project 1")
    if bakeProject == None:
        mset.err("No Bake Project Exists!!")
        return
    
    objlist_Low = selection.getChildren()
    count = len(objlist_Low)
    for i in range(0,count,1):
        group = mset.findObject("Bake_Group_" + str(i))
        for j in range(len(objlist_Low)-1,-1,-1):    
            high = group.findInChildren("High")
            low = group.findInChildren("Low")
            highObject = high.getChildren()
            highname = re.sub(r'_High$', '', highObject[0].name)
            lowname = re.sub(r'_Low$', '', objlist_Low[j].name)
            if highname == lowname:
                objlist_Low[j].parent = low

def outputMapSet():
    newBakeProject = mset.findObject("Bake Project 1")
    newBakeProject.outputSamples = 32
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    newBakeProject.outputPath = os.path.join(desktop_path, outputName.value + ".tga")

def showHideModel(name, visible):
    bakeGroup = mset.findObject("Bake Project 1")
    bakeList = bakeGroup.getChildren()
    #两层 for 循环，用来确认 Low 和 High 组。这是 BakeGroup 的结构导致的。
    for obj in bakeList:
        groupList = obj.getChildren()
        for target in groupList:
            if target.name == name:
                target.visible = visible


def showHighModel():
    showHideModel(name ="High", visible =True)
    showHideModel(name ="Low", visible =False)
def showLowModel():
    showHideModel(name ="High", visible =False)
    showHideModel(name ="Low", visible =True)
    
    
def bakeModel():
    for obj in mset.getAllObjects():
        if isinstance(obj, mset.BakerObject):
            newBakeProject = obj
    if newBakeProject != None:
        newBakeProject.bake()
        #mat_Low = mset.findMaterial("Bake_Low")
        #desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        #mat_Low.getSubroutine("surface").setField("Normal Map", "")        
        #normalmap = mset.Texture(path = os.path.join(desktop_path, outputName.value + "_normal.tga"))
        #mat_Low.getSubroutine("surface").setField("Normal Map", normalmap)
        
    

window = mset.UIWindow( "BakeSetTool_Lite" )
window.width = 110

window.addElement( mset.UILabel("------Set FBX------") )
window.addReturn()

window.addElement( mset.UILabel("TextureName") )
window.addReturn()
outputName = mset.UITextField()
outputName.value = "bake"
window.addElement(outputName)
window.addReturn()

window.addElement( mset.UILabel("SetBaker") )
window.addReturn()

btn = mset.UIButton(" Set Bake HtoL ")
btn.onClick = bakerSetBetweenHighAndLow
window.addElement(btn)
window.addReturn()
btn = mset.UIButton(" High")
btn.onClick = setBakerHigh
window.addElement(btn)
btn = mset.UIButton(" Low ")
btn.onClick = setBakerLow
window.addElement(btn)
window.addReturn()

window.addElement( mset.UILabel("ShowModel") )
window.addReturn()

btn = mset.UIButton(" High")
btn.onClick = showHighModel
window.addElement(btn)
btn = mset.UIButton(" Low ")
btn.onClick = showLowModel
window.addElement(btn)
window.addReturn()

window.addElement( mset.UILabel("Bake") )
window.addReturn()
btn = mset.UIButton("        Bake!!!       ")
btn.onClick = bakeModel
window.addElement(btn)