# -*- coding: utf-8 -*-
"""
Bachelor thesis "Tree-Editing via the collaspe-operator"
Date: 6/2-26
@author: Veronica Persson

"""

# This is the code to my bachelor thesis (VT26)
# See the test file "Tests.py" for examples and simulations of this program. 

# This program is an approximate solution to the problem of finding the minimum
# number of vertices that must be removed from two rooted directed trees using 
# the collapse operator, in order to make the trees isomorphic. 

# How it works: 
#    1. Create two directed rooted trees with the class "TreeNode".
#    2. To make them isomorphic we need to use the class "EditNodes", so for each
#        pair of trees we want to make isomorphic by modifying them (with the 
#        collapse-operator), we need to create an object of this class. 
#    3. We then via the attribute "choose_victim_strategy" in "EditNodes" get
#       the option to choose between two different kind of strategies for
#       deciding which nodes should be deleted with the collapse operator: 
#       "MaxChildren_ChooseVictimStrategy" or "SingleNode_ChooseVictimStrategy".
#    4. Lastly call the "isomorphic_process" method from the "EditNodes" class to
#       start the process of making the two trees isomorphic. 
#    5. To get the desired information print the "EditNodes" object you created
#       and the attribute "isSuccesfull". 
    

# Assumptions and details: 
#    1. All graphs we work with are directed rooted trees.  
#    2. The collapse-operator is adapted and fitted to work with directed rootes 
#       trees and my functions/methods in this code. 
#    3. Two trees transformed by the program, may be printed with different 
#       child/subtree ordering despite being structurally isomorphic. This is only
#       a representation issue and does not affect the correctness of the algorithm. 
#    4. The order of which the children are presented in the "TreeNode" objects, 
#       will influence the solution. So two simulations with exactly the same 
#       trees, but with different implemented order of their children/subtrees, 
#       may result in different isomorphic trees. 



# At the bottom of this file I have created alternative functions for the 
# collapse operator for directed rootes trees.  


#------------------------------------------------------------------------------


# Class for building and implementing a directed rooted tree 
class TreeNode:
    def __init__(self, vertexid: str, parent = None, isomorphic_node = None):   
        self.id = vertexid       # Unique string to identify the nodeobject. 
        self.parent = parent     # Pointer to parent object. If root node its None. 
        self.children = []       # List of child nodes/subtrees 
        
        # Matches/Maps nodes across different trees. This attribute exists to keep 
        # track of nodes that have been mapped togheter and nodes that have not. 
        self.isomorphic_node = isomorphic_node

        
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
        
        """ Deletes a single child of a given TreeNode object """
        
        if not child in self.children:
            raise ValueError(f"'{child.id}' is not a child of the node '{self.id}'")
            
        self.children.remove(child) 
        child.parent = None
    
    
    # Only used if the commented codeblock in "make_isomorphic" is used. 
    def delete_all_children(self) -> None:
    
        """ Deletes all children of a given TreeNode object """
        
        for child in self.children[:]:
            self.delete_child(child)  
            
            
    # In this collapse method we assume the root of a tree can never be removed, since 
    # we aren't intresed in that case and it would destroy our directed rooted 
    # tree --> forest. Therefore that case has not been considerd in this method.
    def collapse(self, node: "TreeNode") -> None: 
        
        """ Input: Takes the parent of the node to be removed (self) and the 
            specific node we want to remove as input. 
            
            Output: Returns nothing """ 

        if not node in self.children:
            raise ValueError(f"'{node.id}' is not a child of the node '{self.id}'") 
        
        self.add_children(node.children)  
        self.delete_child(node) 
    
        
    def total_children(self) -> int:
        
        """ Returns the number of children of a node """
        
        return len(self.children) 
                       
                         

# Class for transforming two non-isomorphic trees into two isomorphic trees by 
# removing nodes in one or both trees with the collapse operator. 
class EditNodes:
    def __init__(self):
        self.solution_tree1 = None 
        self.solution_tree2 = None 
        
        # False if trees we are working with are non-isomorphic, True if they are isomorphic
        self.isSuccessfull = False 
    
        # Strategy/method for determine which nodes should be deleted with collapse operator
        self.choose_victim_strategy = None 
        
        # List of all the deleted nodes in both trees
        self.removed_nodes = [] 
    
    
    def number_of_removed_nodes(self) -> int:
        return len(self.removed_nodes)
    
    def __str__(self):
        return f"Removed {self.number_of_removed_nodes()} nodes \nThe removed nodes are {self.removed_nodes}"
    
    def collect_removed_descendants(self, node: TreeNode) -> None:
        
        """ 
        Recursively collects all descendants of a node and adds them to 
        the list 'removed nodes'. """
        
        for child in node.children:
            self.removed_nodes.append(child.id)
            self.collect_removed_descendants(child)
    
        return
    
    def AHU_algorithm(self, node: TreeNode) -> str:
        
        """
            Input: A single "TreeNode" object.
            Output: An unique encoding of a tree made up of a unique string that 
                    represents a tree. """

        # Leaf nodes are assigned with () 
        if node.total_children() == 0:
            return "()"

        # Recursively encode all children.
        child_encodings = [] 
        for child in node.children:
            child_encodings.append(self.AHU_algorithm(child))
    
        # Sorts lexicographically to make encoding independent of child order.
        child_encodings.sort()
    
        return "(" +"".join(child_encodings)+ ")"
    
    
    def isomorphic_check(self, root1: TreeNode, root2: TreeNode) -> bool: 
        
        """ Uses the 'AHU_algorithm' to check whether two trees are isomorphic.
            Returns True if the trees are isomorphic, False otherwise. """
            
        return self.AHU_algorithm(root1) == self.AHU_algorithm(root2)
    
    
    def isomorphic_process(self, node1: TreeNode, node2: TreeNode):
        """
        The main function we call upon for making two trees isomorphic. This function
        initalizes the process of making two trees isomorphic. """
        
        self.isSuccessfull = self.isomorphic_check(node1,node2) 
        if self.isSuccessfull:
            print (f"The two given trees, {node1.id} and {node2.id}, already are isomorphic!")
        
        else:
            self.make_isomorphic(node1,node2)
            self.isSuccessfull = self.isomorphic_check(node1,node2)
            
        return
    

    def make_isomorphic(self, node1: TreeNode, node2: TreeNode) -> None:
        
        """ Maps nodes across trees and calls upon other methods for ev. deletion 
            of nodes and traversing through trees. """
            
        # Connecting the given nodes/subtrees 
        node1.isomorphic_node = node2 
        node2.isomorphic_node = node1
        
        # We can uncomment the codeblock below if we want a faster algorithm, 
        # but if we strictly want to use the collapse operator this should stay commented. 
        
        # If one of the nodes don't have any children we can directly
        # remove all children and descendants of the other node. 
        # if node1.total_children() == 0:
        #     self.collect_removed_descendants(node2)
        #     node2.delete_all_children() 
            
        # if node2.total_children() == 0: 
        #     self.collect_removed_descendants(node1)
        #     node1.delete_all_children() 


        # If the two input nodes, which are now mapped against each other, don't
        # have the same number of children we have to delete one or more of their
        # children or descendants. 
        while node1.total_children() != node2.total_children(): 
            self.choose_victim(node1,node2) 
        
        
        # When getting here the two input nodes have the same number of children,
        # so we continue diving further down into the tree to continue making the 
        # tree isomorphic. 
        if node1.total_children() != 0: 
            self.mapping_children(node1,node2) 
        
        # Arriving here, the given trees or subtrees should now be isomorphic.
        return 
                
     
    
    # In this method we first check if there exists nodes which have the same 
    # amount of grandchildren. Then remaining nodes are mapped.
    
    def mapping_children(self, node1: TreeNode, node2: TreeNode) -> None:   
        
        """ Dives into trees/subtrees and traverses through them and decides
            which nodes should be mapped across trees. 
            
            The input nodes need to have the same number of children. """

        # Comparing each node on the same depth across the two trees.
        for childNode1 in node1.children[:]:
            
            grandchildren_list = list(filter(lambda x: x.isomorphic_node == None and 
                                             x.total_children() == childNode1.total_children(), node2.children))
            

            # Mapping children of the input nodes to each other if the 
            # "grandchildren_list" is non-empty.
            if grandchildren_list != []:
                childNode2 = grandchildren_list[0] 
                self.make_isomorphic(childNode1,childNode2) 
            else:
                childNode2 = None
        
        # Sorting the children of node1 which not yet have been matched in descending order
        childrenlist1 = list(filter(lambda x: x.isomorphic_node == None, node1.children))
        childrenlist1.sort(key=lambda x: x.total_children(),reverse=True) 
        
        # Sorting the children of node2 which not yet have been matched in descending order
        childrenlist2 = list(filter(lambda x: x.isomorphic_node == None, node2.children))
        childrenlist2.sort(key=lambda x: x.total_children(),reverse=True)
        
        # Mapping remaining nodes based on closest in number of children 
        if len(childrenlist1) > 0:         
            for i in range(len(childrenlist1)): 
                self.make_isomorphic(childrenlist1[i], childrenlist2[i]) 
            
        return        

        
    def choose_victim(self, node1: TreeNode, node2: TreeNode) -> None:
        
        """ Chooses one node to be removed in a tree, i.e the victim and
           then modifies the tree using collapse to remove the victim. """
           
        victim = self.choose_victim_strategy.action(node1,node2)   
        self.removed_nodes.append(victim.id)
        victim.parent.collapse(victim) 
        return


# I have created two strategies/classes for choosing a victim, i.e choosing which 
# node we want to remove in two trees to eventually make them identical. 
# So these classes chooses which node we want to apply collapse on. 

# This class chooses a victim based on which tree and node has the most children.
class MaxChildren_ChooseVictimStrategy:
   
    def action(self, node1: TreeNode, node2: TreeNode) -> TreeNode:
        victim = None        # Node to be deleted
        parentVictim = None  # Parent of node to be deleted
        
        # Choosing in which tree we want to remove a node. 
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


# This class chooses a victim based on number of grandchildren and also
# uses the class MaxChildren_ChooseVictimStrategy as deafult.  
class SingleNode_ChooseVictimStrategy:
    def __init__(self):
        # Setting a default strategy if the strategy in this class cannot find
        # a vinctim satisfying the given conditions in the action method. 
        self.default_strategy = MaxChildren_ChooseVictimStrategy()
    
    def action(self, node1: TreeNode, node2: TreeNode) -> TreeNode:
        victim = None        # Node to be deleted
        parentVictim = None  # Parent of node to be deleted

        # Choosing which tree we want to remove a vertice from.
        if node1.total_children() < node2.total_children():
            parentVictim = node1  
                    
        else:
            parentVictim = node2  
        
        # We need to find a grandchild in parentVictim matching this difference.
        child_difference = abs(node1.total_children()-node2.total_children()) 
        
        # Here we search for ev. grandchildren to be removed upwards.
        # Does it exist grandchildren to parentVictim which fulfills "child_difference"?
        for child in parentVictim.children: 
            
            if child.total_children() == child_difference + 1:  
                victim = child 
            
            if victim != None:
                return victim 
            
        # If we don't find a grandchild matching the "child_difference", we change strategy.
        return self.default_strategy.action(node1, node2)




#------------------------------------------------------------------------------
# Collapse Operator Section

# Another version of the collapse operator, which returns the whole tree after 
# removing a specific vertex.
def collapse(tree: TreeNode, node: TreeNode) -> TreeNode:
    """ 
        Input: The node to be removed and the tree this node belongs to. 
        Output: The modified tree with the given node removed. """
    
    node.parent.add_children(node.children)
    node.parent.delete_child(node)
    
    return tree


# Another addtional version of collapse operator which also can remove multiple 
# vertices at once. 
def collapse_multi(tree: TreeNode, nodelist: list[TreeNode]) -> TreeNode:
    """ 
        Input: A list of nodes to be removed and the tree these nodes belongs to. 
        Output: The modified tree with the given node removed. """
        
    for node in nodelist:
        node.parent.add_children(node.children)
        node.parent.delete_child(node)
    
    return tree


# Tree1
# root = TreeNode("root")
# n1 = TreeNode("n1")
# n2 = TreeNode("n2") 
# n3 = TreeNode("n3")
# n4 = TreeNode("n4")
# n5 = TreeNode("n5")

# root.add_children([n1,n2]) 
# n1.add_children([n3])
# n3.add_children([n4,n5])

# print("Tree1 before collapse is applied:\n")
# print(root)
# print("\nTree1 after collapse is applied:\n")
# print(collapse(root, n4))
# print("\nTree1 after collapse_multi is applied:\n")
# print(collapse_multi(root, [n1,n2]))


