from rit_lib import *

class TreeNode( struct ):
	_slots = ((object,'data'),
              (('TreeNode',NoneType),'left'),
              (('TreeNode',NoneType),'right') )

class Tree( struct ):
	_slots = ( (int,'size'), (TreeNode,'head') )

def is_in_tree(head, element):
	if head == None:
		return False
	elif head.data == element:
		return True
	elif head.data < element:
		return is_in_tree(head.right, element)
	elif head.data > element:
		return is_in_tree(head.left, element)
