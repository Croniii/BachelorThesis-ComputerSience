# -*- coding: utf-8 -*-
"""
Bachelor thesis "?"
Date: 6/2-26
@author: Veronica Persson

"""

# This is the algortihm/code to my bachelor thesis (VT26)

# How it works: 
#    1. Create two directed rooted trees with the class "TreeNode".
#    2. To make them isomorphic we need to use the class "EditNodes", so for each
#        pair of trees we want to make isomorphic by modifying them (with the 
#        collapse-operator), we need to create an object of this class. 
#    3. We then via the attribute "choose_victim_strategy" in "EditNodes" get
#       the option to choose between two different kind of strategies for
#       deciding which nodes should be deleted with the collapse operator: "MaxChildren_ChooseVictimStrategy"
#       or "SingleNode_ChooseVictimStrategy".
#    4. Lastly call the "make_isomorphic" method from the "EditNodes" class to
#       start the process of making the two trees isomorphic. 
    

# Assumptions: 
#    1. All graphs we work with are directed rooted trees. 
#    2. We assume that nodes of the two trees always have the same labels for simplicity, i.e
#       different labels on the nodes of two oterwhise identical trees does not matter, they are seen
#       as isomorphic. 
#    3. The collapse-operator is adapted and fitted to work with directed rootes trees
#       and my functions/methods in this code. 

        
# See the test file "tests.py" for examples and simulations of the algorithm. 



#------------------------------------------------------------------------------


# Node Structure for building a directed rooted tree
class TreeNode:
    def __init__(self, vertexid: str, parent = None, isomorphic_node = None):   
        self.id = vertexid       # Unique string to identify the nodeobject. 
        self.parent = parent     # Pointer to parent TreeNode object, if root node its None. 
        self.children = []       # List of child nodes/subtrees 
        self.isomorphic_node = isomorphic_node #identical node/subtree in eventual other tree.
        # to keep track of nodes that have already mapped togheter. 
        # Matches nodes across trees which should be isomorphic.
        
    def add_children(self, childrenList: list["TreeNode"]) -> None: 
        for child in childrenList: 
            self.children.append(child)  
            child.parent = self 
    
    def __str__(self):
        child_ids = [child.id for child in self.children] 
        parent = self.parent.id if self.parent else None 
        result = f"Node={self.id}, Parent={parent}, Children={child_ids}\n"
        for child in self.children:
            result += child.__str__() 
    
        return result 
        
    def delete_child(self, child: "TreeNode") -> None: 
        
        """ Deletes a single child of a given TreeNode object"""
        
        if not child in self.children:
            raise ValueError(f"'{child.id}' is not a child of the node '{self.id}'")
            
        self.children.remove(child) 
        child.parent = None
    
    
    def delete_all_children(self) -> None:
    
        """ Deletes all children of a given TreeNode object"""
        
        for child in self.children[:]:
            self.delete_child(child)  
            
 
    def collapse(self, node: "TreeNode") -> "TreeNode": 
        
        """ Input: Takes the parent of the node to be removed (self) and the 
            specific node we want to remove as input. """ 

        if not node in self.children:
            raise ValueError(f"'{node.id}' is not a child of the node '{self.id}'") 
        
        self.add_children(node.children)  
        self.delete_child(node) 
    
        
    def total_children(self) -> int:
        
        """ Returns the number of direct children of a node"""
        
        return len(self.children) 
                       
                         

# Class for transforming two non-isomorphic trees into two isomorphic trees by removing
# nodes in one or both trees with help of the collapse operator. 
class EditNodes:
    def __init__(self):
        self.solution_tree1 = None 
        self.solution_tree2 = None 
        self.isSuccessful = False
        
        # Strategy/method for deleting nodes from trees with help of the collapse operator
        self.choose_victim_strategy = None 
        # List of all the deleted nodes in both trees
        self.removed_nodes = [] 
    
    
    def number_of_removed_nodes(self):
        return len(self.removed_nodes)
    
    def __str__(self):
        return f"Removed {self.number_of_removed_nodes()} nodes. \nThe removed nodes are {self.removed_nodes}"
        #return f"{self.solution_tree1}\n{self.solution_tree2}"
    
    def collect_removed_descendants(self, node: TreeNode) -> None:
        
        """ 
        Recursively collects all descendants of a node and adds them to 
        the list 'removed nodes'. """
        
        for child in node.children:
            self.removed_nodes.append(child.id)
            self.collect_removed_descendants(child)
    
        return
    
    # The main function we call upon for making two non-isomorphic trees isomorphic.
    # This algorithm mapes nodes across trees and then calls upon other methods
    # for eventual deletion of nodes or traversing through trees. 
    def make_isomorphic(self, node1: TreeNode, node2: TreeNode) -> TreeNode:
 
        # Connecting the given nodes/subtrees 
        node1.isomorphic_node = node2 
        node2.isomorphic_node = node1
                
        # If one of the nodes don't have any children we can directly
        # remove all children and descendants of the other node. 
        # if node1.total_children() == 0:
        #     self.collect_removed_descendants(node2)
        #     node2.delete_all_children() 
        #     print("child1")
            
        # if node2.total_children() == 0: 
        #     self.collect_removed_descendants(node1)
        #     node1.delete_all_children() 
        #     print("child2")

        
        while node1.total_children() != node2.total_children(): 
            self.choose_victim(node1,node2) 
        
        
        # When getting here the two given nodes have the same number of children,
        # due to the while loop.
        if node1.total_children() != 0:
            self.mapping_children(node1,node2) 

        return 
         
       # return f"hej2\n{self.solution_tree1}\n{self.solution_tree2}" 
       

    
    # Dives into trees/subtrees and traverses through them and decides which nodes
    # should be mapped across the trees. 
    def mapping_children(self, node1: TreeNode, node2: TreeNode) -> None:   #mapping_strategy         
        
        """ Dives into trees/subtrees and """

        # Comparing each node on the same level across the two trees.
        for childNode1 in node1.children[:]:
            
            # Checking if there exist nodes with the same amount of grandchildren
            # and gathering ev. such grandchildren in a list.
            grandchildren_list = list(filter(lambda x: x.isomorphic_node == None and 
                                             x.total_children() == childNode1.total_children(), node2.children))
            
            # If we have nodes with same number of grandchildren we want to map them
            # against each other and diver further into the subtrees of these nodes. 
            # Thus we call make_isomorphic
            if grandchildren_list != []:
                
                childNode2 = grandchildren_list[0] 
                self.make_isomorphic(childNode1,childNode2) 
            else:
                childNode2 = None
        
        # If we don't find any children of the child nodes of the given nodes
        # we will have to do the next best.
        
        # Sorting the children of node1 which not yet have been matched in descending order
        childrenlist1 = list(filter(lambda x: x.isomorphic_node == None, node1.children))
        childrenlist1.sort(key=lambda x: x.total_children(),reverse=True) 
        
        # Sorting the children of node2 which not yet have been matched in descending order
        childrenlist2 = list(filter(lambda x: x.isomorphic_node == None, node2.children))
        childrenlist2.sort(key=lambda x: x.total_children(),reverse=True)
        
        # Mapping the children of the given nodes against eachother which are
        # closest in number of its own children. 
        if len(childrenlist1) > 0:         
            for i in range(len(childrenlist1)): 
                self.make_isomorphic(childrenlist1[i], childrenlist2[i]) 
            
        return        

        

    def choose_victim(self, node1: TreeNode, node2: TreeNode) -> None:
        
        """ Chooses which node we want to remove, i.e the victim and
           then changes the tree using collapse to remove the victim. """
           
         # When we want to remove a node, we use our attribute "choose_victim_strategy" which has been set by the user
         # for which strategy we want to apply for choosing which node is the most optimal to remove. 
        victim = self.choose_victim_strategy.action(node1,node2)   
        self.removed_nodes.append(victim.id)
        victim.parent.collapse(victim) 

        return


# I have created two strategies/classes for choosing a victim, i.e choosing which 
# node we want to remove in two trees to eventually make them identical. 
# So these classes chooses which node we want to apply collapse on. 

# This class chooses a victim based on which tree and node has the most children
class MaxChildren_ChooseVictimStrategy:
   
    def action(self, node1: TreeNode, node2: TreeNode) -> TreeNode:
        victim = None        # Node to be deleted
        parentVictim = None  # Parent of node to be deleted
        
        # Choosing which tree we want to remove a vertice from
        if node1.total_children() > node2.total_children():
            parentVictim = node1  
                    
        else:
            parentVictim = node2  
            
        # Chooses which node in the choosen tree we want to remove. 
        # This is based on which node has the fewest childnodes. 
        for child in parentVictim.children: 
            if victim == None:
                victim = child 
                         
            if child.total_children() < victim.total_children():  
                victim = child 
            
        return victim

# This class chooses a victim based on number of grandcildren and also
# uses the class MaxChildren_ChooseVictimStrategy as deafult.  
class SingleNode_ChooseVictimStrategy:
    def __init__(self):
        # setting a default strategy if the strategy in this class cannot find
        # a vinctim satisfying the given conditions in the action method. 
        self.default_strategy = MaxChildren_ChooseVictimStrategy()
    
    def action(self, node1: TreeNode, node2: TreeNode) -> TreeNode:
        victim = None        # Node to be deleted
        parentVictim = None  # Parent of node to be deleted

        # Choosing which tree we want to remove a vertice from
        if node1.total_children() < node2.total_children():
            parentVictim = node1  
                    
        else:
            parentVictim = node2  
        
        # We need to find a node (grandchild) further down in parentVictim
        # matching this difference.
        child_difference = abs(node1.total_children()-node2.total_children()) 
        
        # Here we search for ev. grandchildren to be removed upwards
        for child in parentVictim.children: 
            
            if child.total_children() == child_difference + 1:  
                victim = child 
            
            if victim != None:
                return victim 
            
        # If we dont find a grandchild matching the differnce, we change strategy
        return self.default_strategy.action(node1, node2)




