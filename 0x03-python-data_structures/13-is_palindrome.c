#include "lists.h"

/**
 * reverse_listint - Reverses a linked list.
 * @head: Pointer to the first node in the list.
 *
 * Return: Pointer to the first node in the new list.
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	for (; current; current = next)
	{
		next = current->next;
		current->next = prev;
		prev = current;
	}

	*head = prev;
}

/**
 * is_palindrome - Checks if a linked list is a palindrome.
 * @head: Double pointer to the linked list.
 *
 * Return: 1 if it is a palindrome, 0 if not.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dup = slow->next;
			break;
		}
		if (!fast->next)
		{
			dup = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	reverse_listint(&dup);

	for (; dup && temp; dup = dup->next, temp = temp->next)
	{
		if (temp->n != dup->n)
			return (0);
	}

	if (!dup)
		return (1);

	return (0);
}
