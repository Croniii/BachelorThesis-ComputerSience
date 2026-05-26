# -*- coding: utf-8 -*-
"""
Created on Wed May 13 16:29:14 2026

@author: Veronica Persson
"""

# These are simulations and test examples of directed rooted trees for the file CodeThesis.py 

# Choose which strategy you want to use on all the simulations, either MaxChildren_ChooseVictimStrategy
# or SingleNode_ChooseVictimStrategy. Default is set to MaxChildren_ChooseVictimStrategy. 

from CodeThesis_Draft1 import TreeNode, EditNodes
from CodeThesis_Draft1 import MaxChildren_ChooseVictimStrategy
from CodeThesis_Draft1 import SingleNode_ChooseVictimStrategy

strategy = MaxChildren_ChooseVictimStrategy()
#strategy = SingleNode_ChooseVictimStrategy()

# -----------------------------------------------------------------------------
# Simulation 1 - Two non-isomorphic trees 

print("Simulation1: Two non-isomorphic trees \n")

# Tree1  -  3 leaves
root1 = TreeNode("root1") 
n1 = TreeNode("n1")
n2 = TreeNode("n2") 
n3 = TreeNode("n3")
n4 = TreeNode("n4")

root1.add_children([n1,n2]) 
n1.add_children([n3])
n1.add_children([n4])

# Tree2  -  4 leaves
root2=TreeNode("root2") 
x1 = TreeNode("x1") 
x2 = TreeNode("x2")
x3 = TreeNode("x3")
x4 = TreeNode("x4")
x5 = TreeNode("x5")

root2.add_children([x1,x2,x3])
x1.add_children([x4,x5]) 

print("The trees before algorithm is applied:")
print("\nTree1:")
print(root1)
print("\nTree2:") 
print(root2)


simulation1 = EditNodes() 
simulation1.choose_victim_strategy = strategy

solution1=simulation1.make_isomorphic(root1,root2) 

print("\nOutput from Algortihm:")
print(simulation1) 

print("Tree1:")
print(root1)
print("\nTree2:") 
print(root2)

print("--------------------------------------------------------------------")

# -----------------------------------------------------------------------------

# Simulation 2 - Two non-isomorphic trees
# Both tree3 and tree4 have the same number of leaves

print("\nSimulation2: Two non-isomorphic trees \n")
 

# Tree3  -  4 leaves
root3=TreeNode("root3") 
y1 = TreeNode("y1") 
y2 = TreeNode("y2")
y3 = TreeNode("y3")
y4 = TreeNode("y4")
y5 = TreeNode("y5")
y6 = TreeNode("y6")

root3.add_children([y1,y2])
y1.add_children([y3,y4])
y3.add_children([y5,y6])

# Tree4  -  4 leaves
root4=TreeNode("root4") 
z1 = TreeNode("z1") 
z2 = TreeNode("z2")
z3 = TreeNode("z3")
z4 = TreeNode("z4")
z5 = TreeNode("z5")
z6 = TreeNode("z6")

root4.add_children([z1,z2])
z1.add_children([z3,z4,z5])
z2.add_children([z6]) 

print("The trees before algorithm is applied:") 
print("\nTree3")
print(root3)
print("\nTree4")
print(root4)

simulation2 = EditNodes() 
simulation2.choose_victim_strategy = strategy 

solution2=simulation2.make_isomorphic(root3,root4)   

print("Output from Algortihm:\n")
print(solution2)
print(simulation2)
 
print("Tree3:")
print(root3)
print("\nTree4:") 
print(root4)


print("--------------------------------------------------------------------")


# -----------------------------------------------------------------------------

# Simulation 3 - Two non-isomorphic trees

print("\nSimulation3: Two non-isomorphic trees \n") 


# Tree5  -  12 leaves
root5=TreeNode("root5") 
a1 = TreeNode("a1") 
a2 = TreeNode("a2")
a3 = TreeNode("a3")
a4 = TreeNode("a4")
a5 = TreeNode("a5")
a6 = TreeNode("a6")
a7 = TreeNode("a7")
a8 = TreeNode("a8")
a9 = TreeNode("a9")
a10 = TreeNode("a10")
a11 = TreeNode("a11")
a12 = TreeNode("a12")
a13 = TreeNode("a13")
a14 = TreeNode("a14")
a15 = TreeNode("a15")
a16 = TreeNode("a16")
a17 = TreeNode("a17")
a18 = TreeNode("a18")
a19 = TreeNode("a19")
a20 = TreeNode("a20")
a21 = TreeNode("a21")

root5.add_children([a1,a2,a3,a4,a5])
a1.add_children([a6,a7,a8])
a6.add_children([a9])
a9.add_children([a10])
a7.add_children([a11,a12])
a3.add_children([a13,a14])
a14.add_children([a15,a16,a17])
a4.add_children([a18])
a5.add_children([a19])
a19.add_children([a20,a21])


# Tree6  -  6 leaves
root6=TreeNode("root6") 
b1 = TreeNode("b1") 
b2 = TreeNode("b2")
b3 = TreeNode("b3")
b4 = TreeNode("b4")
b5 = TreeNode("b5")
b6 = TreeNode("b6")
b7 = TreeNode("b7")
b8 = TreeNode("b8")
b9 = TreeNode("b9")
b10 = TreeNode("b10")

root6.add_children([b1,b2,b3,b4])
b1.add_children([b5,b6])
b5.add_children([b7]) 
b4.add_children([b8]) 
b8.add_children([b9,b10]) 

print("The trees before algorithm is applied:")
print("\nTree5")
print(root5)
print("Tree6")
print(root6)


simulation3 = EditNodes() 
simulation3.choose_victim_strategy = strategy  

solution3 = simulation3.make_isomorphic(root5,root6)   

print("Output from algorithm:\n") 
print(solution3) # unnecessary if make isomorphic returns nothing
print(simulation3) # Makes sense that the EditNodes() returns which nodes were removes and # nodes 

print("\nTree5")
print(root5)
print("\nTree6")
print(root6) 

print("--------------------------------------------------------------------")

# -----------------------------------------------------------------------------


# Simulation 4 - Two non-isomorphic trees
# Only difference to simulation3 is switched order of the nodes/subtrees a1 and a5.

print("\nSimulation4: Two non-isomorphic trees \n") 


# Tree7  -  12 leaves
root7=TreeNode("root5") 
c1 = TreeNode("c1") 
c2 = TreeNode("c2")
c3 = TreeNode("c3")
c4 = TreeNode("c4")
c5 = TreeNode("c5")
c6 = TreeNode("c6")
c7 = TreeNode("c7")
c8 = TreeNode("c8")
c9 = TreeNode("c9")
c10 = TreeNode("c10")
c11 = TreeNode("c11")
c12 = TreeNode("c12")
c13 = TreeNode("c13")
c14 = TreeNode("c14")
c15 = TreeNode("c15")
c16 = TreeNode("c16")
c17 = TreeNode("c17")
c18 = TreeNode("c18")
c19 = TreeNode("c19")
c20 = TreeNode("c20")
c21 = TreeNode("c21")


root7.add_children([c5,c2,c3,c4,c1])
c1.add_children([c6,c7,c8])
c6.add_children([c9])
c9.add_children([c10])
c7.add_children([c11,c12])
c3.add_children([c13,c14])
c14.add_children([c15,c16,c17])
c4.add_children([c18])
c5.add_children([c19])
c19.add_children([c20,c21])


# Tree8  -  6 leaves
root8=TreeNode("root6") 
d1 = TreeNode("d1") 
d2 = TreeNode("d2")
d3 = TreeNode("d3")
d4 = TreeNode("d4")
d5 = TreeNode("d5")
d6 = TreeNode("d6")
d7 = TreeNode("d7")
d8 = TreeNode("d8")
d9 = TreeNode("d9")
d10 = TreeNode("d10")

root8.add_children([d1,d2,d3,d4])
d1.add_children([d5,d6])
d5.add_children([d7]) 
d4.add_children([d8]) 
d8.add_children([d9,d10]) 

print("The trees before algorithm is applied:")
print("\nTree7")
print(root7)
print("Tree8")
print(root8)


simulation4 = EditNodes()
simulation4.choose_victim_strategy = strategy  

solution4 = simulation4.make_isomorphic(root7,root8)   

print("Output from algorithm:")
print(solution4)
print(simulation4)

print("\nTree7")
print(root7)
print("Tree8")
print(root8) 


print("--------------------------------------------------------------------")

# -----------------------------------------------------------------------------

# Simulation 5 - Two isomorphic trees

print("\nSimulation5: Two isomorphic trees \n") 

# Tree9  -  4 leaves
root9=TreeNode("root9") 
f1 = TreeNode("f1") 
f2 = TreeNode("f2")
f3 = TreeNode("f3")
f4 = TreeNode("f4")
f5 = TreeNode("f5")
f6 = TreeNode("f6")

root9.add_children([f1,f2])
f1.add_children([f3,f4])
f3.add_children([f5,f6])

# Tree10  -  4 leaves
root10=TreeNode("root10") 
g1 = TreeNode("g1") 
g2 = TreeNode("g2")
g3 = TreeNode("g3")
g4 = TreeNode("g4")
g5 = TreeNode("g5")
g6 = TreeNode("g6")

root10.add_children([g1,g2])
g1.add_children([g3,g4])
g3.add_children([g5,g6])

print("The trees before algorithm is applied:")
print("\nTree9")
print(root9)
print("Tree10")
print(root10)


simulation5 = EditNodes()
simulation5.choose_victim_strategy = strategy  

solution5 = simulation5.make_isomorphic(root9,root10)  


print("Output from algorithm:")
print(simulation5)
print(solution5)

print("\nTree9")
print(root9)
print("\nTree10")
print(root10) 

print("--------------------------------------------------------------------")

# -----------------------------------------------------------------------------

# Simulation 6 - Two non-isomorphic trees

# En till där strategy två är bättre

