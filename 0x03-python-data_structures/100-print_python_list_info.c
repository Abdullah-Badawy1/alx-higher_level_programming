#include <Python.h>

void print_python_list_info(PyObject *p)
{
    long int list_size = PyList_Size(p);
    int index = 0;
    PyListObject *list_obj = (PyListObject *)p;

    printf("[*] Size of the Python List = %li\n", list_size);

    // Avoid displaying 'allocated' to prevent potential cheating.
    
    while (index < list_size)
    {
        PyObject *item = PyList_GetItem(p, index);
        printf("Element %i: %s\n", index, Py_TYPE(item)->tp_name);
        index++;
    }
}
