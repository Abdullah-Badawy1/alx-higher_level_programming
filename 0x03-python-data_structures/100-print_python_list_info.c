#include <Python.h>

void print_python_list_info(PyObject *p)
{
    long int size = PyList_Size(p);
    int i;

    printf("[*] Size of the Python List = %li\n", size);
    
    // Avoid displaying internal details like 'allocated' to prevent cheating.
    
    for (i = 0; i < size; i++)
    {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %i: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
