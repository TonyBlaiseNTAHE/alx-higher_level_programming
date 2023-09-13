#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	PyListObject *t;
	int i = 0;
	long int size = PyList_Size(p);

	t = (PyListObject *)p;
	printf("[*] Size of Python List = %ld\n", size);
	printf("[*] Allocated = %ld", t->allocated)
	while (i < size))
	{
		printf("Element %d: %s\n", i, Py_TYPE(obj->ob_item[i]->tp_name));
		i++;
	}
}
