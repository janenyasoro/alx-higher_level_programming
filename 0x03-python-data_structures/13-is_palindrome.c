#include "lists.h"

/**
 * is_palindrome - Checks to see if linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if not a palindrome, 1 if a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head, *new_current = *head;
	unsigned int count = 0, cycle = 0, i = 0, len = 0;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);

	while (current != NULL)
	{
		count++;
		current = current->next;
	}

	current = *head;
	cycle = count * 2;
	len = cycle - 2;

	for (i = 0; i < cycle; i = i + 2)
	{
		if (current[i].n != new_current[len].n)
			return (0);
		len = len - 2;
	}

	return (1);
}
