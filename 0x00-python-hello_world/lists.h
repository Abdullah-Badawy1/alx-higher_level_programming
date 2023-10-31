#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: The integer data of the node
 * @next: Pointer to the next node
 *
 * Description: Structure for a singly linked list node.
 */
typedef struct listint_s
{
	int n;             /* Integer data of the node */
	struct listint_s *next; /* Pointer to the next node */
} listint_t;

/**
 * print_listint - Prints the elements of a singly linked list.
 * @h: A pointer to the head of the list.
 *
 * Return: The number of nodes in the list.
 */
size_t print_listint(const listint_t *h);

/**
 * add_nodeint - Adds a new node to the beginning of a list.
 * @head: A pointer to the pointer to the head of the list.
 * @n: The integer data to be added to the new node.
 *
 * Return: A pointer to the newly added node, or NULL on failure.
 */
listint_t *add_nodeint(listint_t **head, const int n);

/**
 * free_listint - Frees a singly linked list.
 * @head: A pointer to the head of the list.
 */
void free_listint(listint_t *head);

/**
 * check_cycle - Checks if a singly linked list contains a cycle.
 * @list: A pointer to the head of the list.
 *
 * Return: (1) if there is a cycle, (0) if there is no cycle.
 */
int check_cycle(listint_t *list);

#endif /* LISTS_H */

