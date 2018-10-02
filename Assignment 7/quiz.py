''''
Given the following permutation of a,b,c,d,e,f,g,h,i,j, what is the next permutation in lexicographic (dictionary) order? Write your answer without any blank spaces between letters.
fjadbihgec
'''
from math import factorial
def print_permutations_lexicographic_order(s):
    seq = list(s)
    jk=list()
    for _ in range(factorial(len(seq))):
        jk.append(''.join(seq))
        #print(''.join(seq))
        p = len(seq) - 1
        while p > 0 and seq[p - 1] > seq[p]:
            p -= 1
        seq[p:] = reversed(seq[p:])
        if p > 0:
            q = p
            while seq[p - 1] > seq[q]:
                q += 1
            seq[p - 1], seq[q] = seq[q], seq[p - 1]
    print(jk[2138520])                                  #jk[2138519]='fjadbihgec'
s = input('Enter the string: ')                         #abcdefghij
print_permutations_lexicographic_order(s)   #fjadcbeghi

'''
We want to add a function length() to the class Node that implements user defined lists which will compute the length of a list. An incomplete implementation of length() given below. You have to provide an expression to put in place of *** on the last line.
'''
def length(self):
    if self.value == None:
        return(0)
    elif self.next == None:
        return(1)
    else:
        return(***)                                     #   return(1 + self.next.length())

'''Suppose we add this function foo() to the class Tree that implements search trees. For a name mytree with a value of type Tree, what would mytree.foo() compute?
'''
def foo(self):
    if self.isempty():
        return(0)
    elif self.isleaf():
        return(1)
    else:
        return(1 + max(self.left.foo(),self.right.foo()))
#The length of the longest path from root to leaf in mytree.

'''
Inorder traversal of a binary tree has been defined in the lectures. A preorder traversal lists the vertices of a binary tree (not necessarily a search tree) as follows:
Print the root.
Print the left subtree in preorder.
Print the right subtree in preorder. 
Suppose we have a binary tree with 10 nodes labelled a, b, c, d, e, f, g, h, i, j, with preorder traversal gbhecidajf and inorder traversal ehbicgjafd. What is the right child of the root node?
'''
#d
