#include "lists.h"

/**
 * reverse - reverses the 2nd half of a list
 *
 * @h_r: head of the 2nd half
 * Return: nothing
 */

void reverse(listint_t **h_r)
{
	listint_t *prev;
	listint_t *current;
	listint_t *nxt;

	prev = NULL;
	current = *h_r;

	while (current != NULL)
	{
		nxt = current->next;
		current->next = prev;
		prev = current;
		current = nxt;
	}

	*h_r = prev;
}

/**
 * compare - compares integers of the list
 *
 * @h1: head of the first half
 * @h2: head of the second half
 * Return: 1 if are equals, 0 if not equal
 */

int compare(listint_t *h1, listint_t *h2)
{
	listint_t *temp1;
	listint_t *temp2;

	temp1 = h1;
	temp2 = h2;

	while (temp1 != NULL && temp2 != NULL)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
		{
			return (0);
		}
	}

	if (temp1 == NULL && temp2 == NULL)
	{
		return (1);
	}

	return (0);
}

/**
 * is_palindrome - checks if a singly linked list
 * is a palindrome
 * @head: head of list
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palndrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow;
	listint_t *second_half, *middle;
	int isp;

	slow = fast = prev_slow = *head;
	middle = NULL;
	isp = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}

		if (fast != NULL)
		{
			middle = slow;
			slow = slow->next;
		}

		second_half = slow;
		prev_slow->next = NULL;
		reverse(&second_half);
		isp = compare(*head, second_half);

		if (middle != NULL)
		{
			prev_slow->next = middle;
			middle->next = second_half;
		}
		else
		{
			prev_slow->next = second_half;
		}
	}

	return (isp);
}
