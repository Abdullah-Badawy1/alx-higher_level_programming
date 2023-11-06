#include <Python.h>

void print_python_list_info(PyObject *p)
{
    long int size = PyList_Size(p);
    int i;

    printf("[*] Size of the Python List = %li\n", size);
    
    // 'allocated' field is an implementation detail; consider avoiding it
    // printf("[*] Allocated = %li\n", obj->allocated);
    
    for (i = 0; i < size; i++)
    {
        // Use Py_TYPE to get the type of the Python object
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %i: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
