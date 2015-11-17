from rit_object import *

class Tree(rit_object):
	__slots__ = ('head', 'size')
	_types      = ('TreeNode', int)

class TreeNode:
	__slots__ = ('data', 'left', 'right')
	_types      = (object, 'TreeNode', 'TreeNode')

def mkTree(head, size):
	return Tree(head,size)

def mkTreeNode(data, left, right):
	return TreeNode(data,left,right)

def is_in_tree(head, element):
	if head == None:
		return False
	elif head.data == element:
		return True
	elif head.data < element:
		return is_in_tree(head.right, element)
	elif head.data > element:
		return is_in_tree(head.left, element)
