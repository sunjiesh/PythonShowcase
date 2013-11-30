# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 22:07:29 2013

@author: tom
"""

def fromParamsCompare(paramTxt1,paramTxt2):
    """
        form普通表单形式的参数对比
    """
    #params to arr
    paramArr1=paramTxt1.split("&")
    paramArr2=paramTxt2.split("&")
    print paramArr1
    print paramArr2
    
    #存放到字典中，Value为List
    paramArrArr1={}
    paramArrArr2={}
    
    equalParams=[]
    notEqualParams=[]
    needlessParams=[]
    lostParams=[]

    for tempParam in paramArr1:
        if "=" in tempParam:
            tempParamArr=tempParam.split("=")
            tempParamName=''
            tempParamValue=''
            if(len(tempParamArr)==1):
                tempParamName=tempParamArr[0]
            elif(len(tempParamArr)==2):
                tempParamName=tempParamArr[0]
                tempParamValue=tempParamArr[1]
            else:
                tempParamName=tempParamArr[0]
                tempParamValue=tempParam.replace(tempParamName+"=")
            if paramArrArr1.has_key(tempParamName):
                paramArrValue=paramArrArr1[tempParamName]
                paramArrValue=paramArrValue.append(tempParamValue)
            else:
                paramArrArr1[tempParamName]=[tempParamValue];
    for tempParam in paramArr2:
        if "=" in tempParam:
            tempParamArr=tempParam.split("=")
            tempParamName=''
            tempParamValue=''
            if(len(tempParamArr)==1):
                tempParamName=tempParamArr[0]
            elif(len(tempParamArr)==2):
                tempParamName=tempParamArr[0]
                tempParamValue=tempParamArr[1]
            else:
                tempParamName=tempParamArr[0]
                tempParamValue=tempParam.replace(tempParamName+"=")
            if paramArrArr2.has_key(tempParamName):
                paramArrValue=paramArrArr2[tempParamName]
                paramArrValue=paramArrValue.append(tempParamValue)
            else:
                paramArrArr2[tempParamName]=[tempParamValue];
                
    print paramArrArr1
    print paramArrArr2
    
    
    
    
    
    #遍历数组，处理判断是否是却少的，以及不一情况
    for paramKey in paramArrArr1:
        if paramKey in paramArrArr2:            
            paramArrArrValue1=paramArrArr1[paramKey]
            paramArrArrValue2=paramArrArr2[paramKey]
            paramArrArrValue1=sorted(paramArrArrValue1)
            paramArrArrValue2=sorted(paramArrArrValue2)
            if paramArrArrValue1==paramArrArrValue2:
                equalParams.append(paramKey)
            else:
                notEqualParams.append(paramKey)
        else:
            lostParams.append(paramKey)
    
    #遍历数组，处理判断是否是多余的参数
    for paramKey in paramArrArr2:
        if paramKey in paramArrArr1:
            pass
        else:
            needlessParams.append(paramKey)
    
    print '结果如下'
    print '相等的参数是'
    print equalParams
    print '不想等的参数是'
    print notEqualParams
    print '多余的参数是'
    print needlessParams
    print '缺少的参数是'
    print lostParams
    
    return equalParams,notEqualParams,needlessParams,lostParams,paramArrArr1,paramArrArr2
