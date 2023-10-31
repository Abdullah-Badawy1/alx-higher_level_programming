#include "lists.h"
/**
* check_cycle - Checks if a singly-linked list contains a cycle.
* @list: A singly-linked list.
*
* Return: (1) if there is a cycle, (0) if there is no cycle.
*/
int check_cycle(listint_t *list)
{
	listint_t *slow_ptr, *fast_ptr;

	if (list == NULL || list->next == NULL)
		return (0);

	slow_ptr = list->next;
	fast_ptr = list->next->next;

	for (; slow_ptr && fast_ptr && fast_ptr->next;)
	{
		if (slow_ptr == fast_ptr)
			return (1);

		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;
	}

	return (0);
}
