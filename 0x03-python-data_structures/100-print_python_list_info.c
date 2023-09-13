#include <stdio.h>
#include "Python.h"

/**
 * print_python_list_info - prints some basic info
 * about Python list
 * @p: pointer of type PyObectj.
 * Return: nothing.
*/
void print_python_list_info(PyObject *p)
{
	int i = 0;
	PyListObject *t;

	t = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", t->ob_base.ob_size);
	printf("[*] Allocated  = %ld\n", t->allocated);
	while (i < t->ob_base.ob_size)
	{
		printf("Element %d: %s\n", i, t->ob_item[i]->ob_type->tp_name);
		i++;
	}
}
