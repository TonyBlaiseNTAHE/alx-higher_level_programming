#include <python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	int i = 0;
	PyListObject *t;

	t = (PyListObject *)p;
	printf("[*] Size of Python List = %ld\n", Pylist_size(p));
	printf("[*] Allocated = %ld", t->allocated)
	while (i < Pylist_size(p))
	{
		printf("Element %d: %s\n", i, Py_TYPE(obj->ob_item[i]->tp_name));
		i++;
	}
}
