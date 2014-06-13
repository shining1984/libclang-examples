#!/usr/bin/env python
 
#sample come from the network:
#http://www.seethroughskin.com/blog/?p=2172
#
import os
import sys
from pprint import pprint
import clang.cindex

def get_info(node, depth=0):
	return { 'kind' : node.kind,
             'usr' : node.get_usr(),
             'spelling' : node.spelling,
             'location' : node.location,
             'extent.start' : node.extent.start,
             'extent.end' : node.extent.end,
             'is_definition' : node.is_definition()}
 
def output_cursor_and_children(cursor, level=0):
 
	#LINKAGE_SPEC (http://clang.llvm.org/doxygen/classclang_1_1LinkageSpecDecl.html)
	#Represents code of the type:  extern "C" void foo()
#	if cursor.kind == clang.cindex.CursorKind.LINKAGE_SPEC:
#		pprint(('nodes', get_info(cursor)))
	pprint(('nodes', get_info(cursor)))

	# Recurse for children of this cursor
	has_children = False;
	for c in cursor.get_children():
		if not has_children:
			has_children = True
		output_cursor_and_children(c, level+1)
 
def main():
	from clang.cindex import Index
	from pprint import pprint
 
	from optparse import OptionParser, OptionGroup
 
	global opts
 
	parser = OptionParser("usage: %prog {filename} [clang-args*]")
	parser.disable_interspersed_args()
	(opts, args) = parser.parse_args()
 
	if len(args) == 0:
		print 'invalid number arguments'
 
	index = Index.create()
	tu = index.parse(None, args)
 
	if not tu:
		print "unable to load input"
 
	output_cursor_and_children(tu.cursor)
 
if __name__ == '__main__':
    main()
