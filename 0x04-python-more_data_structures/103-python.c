#include <Python.h>

void display_python_list_info(PyObject *list);
void display_python_bytes_info(PyObject *bytes);

/**
 * display_python_list_info - Displays information about Python lists.
 * @list: a PyObject list object.
 */
void display_python_list_info(PyObject *list)
{
	int size, allocation, index;
	const char *element_type;
	PyListObject *py_list = (PyListObject *)list;
	PyVarObject *var = (PyVarObject *)list;

	size = var->ob_size;
	allocation = py_list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocation);

	index = 0;
	while (index < size)
	{
		element_type = py_list->ob_item[index]->ob_type->tp_name;
		printf("Element %d: %s\n", index, element_type);
		if (strcmp(element_type, "bytes") == 0)
			display_python_bytes_info(py_list->ob_item[index]);

		index++;
	}
}

/**
 * display_python_bytes_info - Displays information about Python byte objects.
 * @bytes: A PyObject byte object.
 */
void display_python_bytes_info(PyObject *bytes)
{
	unsigned char i, size;
	PyBytesObject *byte_data = (PyBytesObject *)bytes;

	printf("[.] bytes object info\n");
	if (strcmp(bytes->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)bytes)->ob_size);
	printf("  trying string: %s\n", byte_data->ob_sval);

	if (((PyVarObject *)bytes)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)bytes)->ob_size + 1;

	printf("  first %d bytes: ", size);
	i = 0;
	while (i < size)
	{
		printf("%02hhx", byte_data->ob_sval[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
		
		i++;
	}
}
