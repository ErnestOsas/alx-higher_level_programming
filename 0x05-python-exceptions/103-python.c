#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <string.h>
/**
 * print_python_bytes - print python things
 * @p: pointer to PyObject p
 */
void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes = (PyBytesObject *)p;
    char *str = NULL;
    Py_ssize_t size = 0, i = 0;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }
    str = PyBytes_AsStringAndSize(p, &size);
    if (!str)
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }
    printf("  size: %ld\n  trying string: %s\n", size, str);
    size > 10 ? size = 10 : (void)size;
    printf("  first %ld bytes: ", size);
    for (i = 0; i < size; i++)
        printf("%02hhx ", str[i]);
    printf("\n");
}
/**
 * print_python_float - print python things
 * @p: pointer to PyObject p
 */
void print_python_float(PyObject *p)
{
    char *str;
    double f;

    setbuf(stdout, NULL);
    printf("[.] float object info\n");
    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }
    f = ((PyFloatObject *)(p))->ob_fval;
    str = PyOS_double_to_string(f, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
    printf("  value: %s\n", str);
    fflush(stdout);
    PyMem_Free(str);
}
/**
 * print_python_list - print python things
 * @p: pointer to PyObject p
 */
void print_python_list(PyObject *p)
{
	size_t i;
	PyObject *item;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n[*] Allocated = %ld\n",
 PyList_Size(p), ((PyListObject *)p)->allocated);
	for (i = 0; i < PyList_Size(p); i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
		if (strcmp(item->ob_type->tp_name, "bytes") == 0)
			print_python_bytes(item);
		if (strcmp(item->ob_type->tp_name, "float") == 0)
			print_python_float(item);
	}
}

