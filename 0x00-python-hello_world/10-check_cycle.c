#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has
 * a cycle in it
 * @list: list
 * Return: 0 if there is no cycle,
 * 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *ptr;
	listint_t *previous;

	ptr = list;
	previous = list;
	while (list && ptr && ptr->next)
	{
		list = list->next;
		ptr = ptr->next->next;

		if (list == ptr)
		{
			list = previous;
			previous =  ptr;
			while (1)
			{
				ptr = previous;
				while (ptr->next != list && ptr->next != previous)
				{
					ptr = ptr->next;
				}
				if (ptr->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
