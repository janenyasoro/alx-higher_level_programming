#include <stdlib.h>
#include <stdio.h>
#include "/usr/include/python3.4/Python.h"
#include "/usr/include/python3.4/listobject.h"
#include "/usr/include/python3.4/object.h"

/**
* print_python_list_info - prints some basic info about Python lists
* @p: Python Object
*
* Return: void
*/
void print_python_list_info(PyObject *p)
{
	int i = 0, list_len = 0;
	PyObject *item;
	PyListObject *clone = (PyListObject *) p;

	list_len = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", list_len);
	printf("[*] Allocated = %d\n", (int) clone->allocated);

	for (; i < list_len; ++i)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %d: %s\n", i, item->ob_type->tp_name);
	}
}
