#!/usr/bin/python3
import sys

graph = []
import pprint
search = []

def get_position(graph, package):
    """"""
    for i in range(len(graph)):
        if graph[i][0] == package:
            return i
    return -1


def recursive_dfs(graph, initial_package, path=[]):
    '''recursive depth first search from initial_package'''
    pos = get_position(graph, initial_package)
    path = path + [initial_package]
    for i in range(len(graph[pos])-1):
        for node in graph[pos][i+1]:
            if not node in path:
                path = recursive_dfs(graph, node, path)
    return path
    


def checklen(graph,packagename,a,b,l):
    for i in range(len(graph)):
        for m in range(len(graph[i])):
    
            if graph[i][m] == graph[i][m]:
                for n in a:
                    if n == b[0]:
                        if len(l) > 1:
                            l.pop(0)
                        
                        put(graph,packagename,a,b,l)
                        
                        return
                    
                for n in b:
                    if n == a[0]:
                        if len(l) > 1:
                            l.pop(1)
                        put(graph,packagename,a,b,l)
                        
                        return                                                                                             
                                            
            
                index = 0
                count = 0
                
                for s in graph[i]:
        
                    for q in range(len(a)-1):
                       if [a[q+1]] == s:
                           index = index + 1
                    for p in range(len(b)-1):
                       if [b[p+1]] == s:
                            count = count + 1
                            
                if index > count and len(a)-index < len(b)-count:
                    if len(l) > 1:
                        l.pop(1)
                    put(graph,packagename,a,b,l)
                    
                elif index > count and len(a)-index > len(b)-count:
                    if len(l) > 1:
                        l.pop(0)
                    put(graph,packagename,a,b,l)
                    
                elif index < count and len(a)-index < len(b)-count:
                    if len(1) > 1:
                        l.pop(1)
                    put(graph,packagename,a,b,l)
                    
                elif index < count and len(a)-index > len(b)-count:
                    if len(l) > 1:
                        l.pop(0)
                    put(graph,packagename,a,b,l)
                    
                elif index == count and len(a)-index > len(b)-count:
                    if len(l) > 1:
                        l.pop(0)
                    put(graph,packagename,a,b,l)
                    
                elif index == count and len(a)-index < len(b)-count:
                    if len(l) > 1:
                        l.pop(1)
                    put(graph,packagename,a,b,l)
                    
                elif index > count and len(a)-index == len(b)-count:
                    if len(l) > 1:
                        l.pop(1)
                    put(graph,packagename,a,b,l)
                    
                    
                elif index < count and len(a)-index == len(b)-count:
                    if len(l) > 1:
                        l.pop(0)
                    put(graph,packagename,a,b,l)
                    
                elif index == count and len(a)-index == len(b)-count:
                    if len(l) > 1:
                        l.pop(1)
                    put(graph,packagename,a,b,l)
                    


def put(graph,packagename,a,b,l):
    if len(l) == 1:
        
        for i in range(len(graph)):
            for m in range(len(graph[i])):
                if graph[i][m] == packagename:
                    for r in range(len(graph[i])):
                        if type(graph[i][r]) is list:
                            if len(graph[i][r]) > 1:
                                
                                
                                if [l[0][0]] in graph[i]:
                                    graph[i].pop(r)
                                    return
                                else:
                                    graph[i].append([l[0][0]])
                                    graph[i][r],graph[i][-1] = graph[i][-1],graph[i][r]
                                    graph[i].pop(-1)
                                    return
    else:
        checklen(graph,packagename,l[0],l[1],l)

def SEARCH(package_name):
    for i in search:
        if i == package_name:
            graph = []
            return True
    return False

def dependencies(pack):
    result = []
    for e in graph:
        for f in e:
            if e[0] == pack:
                if type(f) is list:
                    for g in f:
                        result.append(g)
                    
    return result
            

f = open("packages_dependencies.txt")
for line in f:
    line = line.strip()
    names = line.split(":")[0]
    search.append(names)
    packages = line.split(":")[1:][0].split(",")

    required = []
    
    options2 = []
    for p in packages:
        options = []
        if len(p.split("|")) > 1:
            for x in p.split("|"):
                options.append(x.strip())
            options2.append(options)              
        else:
            for x in p.split("|"):
                required.append(x.strip())

    lister = [names]
    for req in required:
        lister.append([req])
    for q in options2:
        lister.append(q)
    graph.append(lister)
for r in graph:
    for b in range(len(r)):
        if r[b] == []:
            r.pop(b)
for fre in range(len(graph)):
    for fre2 in range(len(graph[fre])):
        if graph[fre][fre2] == ['']:
            graph[fre].pop(fre2)

for i in graph:
    for j in i:
        if type(j) is list and len(j) > 1:
            
            name = []
            for s in j:
                named = recursive_dfs(graph,s, path=[])
                name.append(named)
            checklen(graph,i[0],name[0],name[1],name)
                
        

