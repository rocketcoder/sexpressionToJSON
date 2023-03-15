import re
import json

def processOrderData(results):
  orderSet = []
  print(results)
  for result in results:
    keys = getKeys(result[0])
    values = getValues(result[0])    
    orderItem = {}
    for i in range(0, len(keys)): 
      if i < len(values) and not isinstance(values[i], list):
        orderItem[keys[i]] = values[i]
      
    orderSet.append(orderItem)
  
  return orderSet;  


def getOrderSet(sexpression):
    print(sexpression)
    orderGroups = getGroups(sexpression)
    print(orderGroups)
    orderData = walkOrderData(orderGroups)
    order_dict = processOrderData(orderData)        
    filtered_order_dict = []
    for item in order_dict:
        if len(item) > 0:
            filtered_order_dict.append(item)

    return filtered_order_dict

def getGroups(data_str):
    stack = []
    root = {"children":[], "parent": None, "result": ""}
    currentNode = root
    start = False

    for i in range(0, len(data_str)):
        if data_str[i] == '(':
            stack.append('(')
            node = {"result" : "", "children":[]}
            if currentNode["parent"] is not None:
                node["parent"] = root
                root["children"].append(node)
            else:
                node["parent"] = currentNode
                currentNode["children"].append(node)
            
            currentNode = node             
            if start == False:
                start = True                
            
            node["result"] = data_str[i]
            
        elif data_str[i] == ')':
            if stack[len(stack) - 1] == '(': 
                stack.pop()
                if len(stack) == 0:
                    start = False
                
                currentNode["result"] += data_str[i]
                
                if currentNode["parent"] is not None:
                    currentNode = currentNode["parent"]
            else:
                print("not balanced!")            
            
        else:
            if start == True :
                currentNode["result"] += data_str[i]
    return root


def walkOrderData(node): 
  orderData = []
  if node["result"] is not None:
    orderData.append(node["result"])
  
  if len(node["children"]) > 0:
    for i in range(0, len(node["children"])):
      orderData.append(walkOrderData(node["children"][i]))
  
  return orderData


def getKeys(text):
    regex = "(?<=:)[\w+.-]+"
    matches =  re.findall(regex, text)
    return matches
  
def getValues(text):
    regex = "'(.*?)'"
    matches = re.findall(regex, text)
    matched_values = []
    for match in matches:
        matched_values.append(match)
    return matched_values


