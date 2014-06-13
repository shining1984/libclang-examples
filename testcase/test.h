//
//This testcase come from the blog:
//http://www.seethroughskin.com/blog/?p=2172
//
#ifndef TEST_H
#define TEST_H
 
class Foo 
{
	int data_;
public:
	Foo(){}
 
	void bar(int data){data_ = data;}
};
 
extern "C" __declspec( dllexport )void test1(){}
 
#endif
