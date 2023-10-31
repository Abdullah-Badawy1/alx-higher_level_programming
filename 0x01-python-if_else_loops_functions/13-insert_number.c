#include "lists.h"

/**
 * insert_node - Inserts a node with a number in a sorted singly linked list
 * @head: Pointer to a pointer to the head of the linked list
 * @number: Number to insert
 * Return: Address of the new node or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current_node;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	if ((*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	current_node = *head;
	while (current_node->next != NULL)
	{
		if (current_node->next->n > number)
		{
			new_node->next = current_node->next;
			current_node->next = new_node;
			return (new_node);
		}
		current_node = current_node->next;
	}

	current_node->next = new_node;
	return (new_node);
}
