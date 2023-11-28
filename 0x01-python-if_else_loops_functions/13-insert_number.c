#include "lists.h"

/**
 * insert_node - inserts a number into a
 * sorted singly linked list
 *
 * @head: head
 * @number: index
 * Return: the address of the new node, or NULL if it
 * failed.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_n;
	listint_t *h;
	listint_t *prev_h;

	h = *head;
	new_n = malloc(sizeof(listint_t));

	if (new_n == NULL)
		return (NULL);

	while (h != NULL)
	{
		if (h->n > number)
			break;
		prev_h = h;
		h = h->next;
	}

	new_n->n = number;

	if (*head == NULL)
	{
		new_n->next = NULL;
		*head = new_n;
	}
	else
	{
		new_n->next = h;
		if (h == *head)
			*head = new_n;
		else
			prev_h->next = new_n;
	}

	return (new_n);
}
