from avl_node import AVLNode
from bst import BST
from bst_node import Node


class AVL(BST):
    def __init__(self):
        super().__init__()

    def add(self, value):
        self.root = self._add_recursive(self.root, value)  # Note that self.root is updated here

    def _add_recursive(self, current_node, value):
        # If the current node is None, return a new AVLNode containing the value
        if current_node is None:
            return AVLNode(value)
        # Check if current_node is of the base class Node and cast it to AVLNode if necessary
        # This is necessary to not change the add() in the BST class.
        # When the first node is added, the type of the root is Node, so we need to cast it
        if isinstance(current_node, Node) and not isinstance(current_node, AVLNode):
            current_node = AVLNode(current_node.value)
            current_node.left_child = self.root.left_child
            current_node.right_child = self.root.right_child
            self.root = current_node

        # Determine whether the value should be inserted to the left or right subtree
        if value <= current_node.value:
            current_node.left_child = self._add_recursive(current_node.left_child, value)
        else:
            current_node.right_child = self._add_recursive(current_node.right_child, value)

        # Update the height and imbalance factor for the current node
        current_node.calculate_height_and_imbalance()

        # Check if tree balancing is needed and balance if necessary
        if abs(current_node.imbalance) == 2:
            return self._balance(current_node)

        return current_node

    def get_height(self):
        if self.root is None:
            return 0
        return self.root.height

    def _rotate_left(self, node):
        # Store the pivot (the root of the right subtree of 'node')
        pivot = node.right_child

        # Update the right child of 'node' to be the left child of the pivot
        node.right_child = pivot.left_child

        # Set the left child of the pivot to be the node
        pivot.left_child = node

        # Recalculate the height and imbalance factor for the rotated node
        node.calculate_height_and_imbalance()

        # Recalculate the height and imbalance factor for the pivot
        pivot.calculate_height_and_imbalance()

        # Return the pivot as the new root of this subtree
        return pivot

    def _rotate_right(self, node):
        # Store the pivot (the root of the left subtree of 'node')
        pivot = node.left_child

        # Update the left child of 'node' to be the right child of the pivot
        node.left_child = pivot.right_child

        # Set the right child of the pivot to be the node
        pivot.right_child = node

        # Recalculate the height and imbalance factor for the rotated node
        node.calculate_height_and_imbalance()

        # Recalculate the height and imbalance factor for the pivot
        pivot.calculate_height_and_imbalance()

        # Return the pivot as the new root of this subtree
        return pivot

    def _balance(self, node):
        # Case 1: Left subtree is higher than right subtree
        if node.imbalance == 2:
            pivot = node.left_child

            # Single right rotation
            if pivot.imbalance == 1:
                return self._rotate_right(node)
            # Double rotation: Left-Right
            else:
                node.left_child = self._rotate_left(pivot)
                return self._rotate_right(node)
        # Case 2: Right subtree is higher than left subtree
        else:
            pivot = node.right_child
            # Single left rotation
            if pivot.imbalance == -1:
                return self._rotate_left(node)
            # Double rotation: Right-Left
            else:
                node.right_child = self._rotate_right(pivot)
                return self._rotate_left(node)
