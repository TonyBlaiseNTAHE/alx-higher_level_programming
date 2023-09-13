#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	int i = 0;
	PyListObject *t;
	long int size = PyList_Size(p);
	
	t = (PyListObject *)p;
	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", t->allocated);
	for (;i < size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(t->ob_item[i])->tp_name);
}
