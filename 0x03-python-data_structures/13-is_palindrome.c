#include "lists.h"

/**
 * is_palindrome - Checks if a string is palindrome or not
 * @head: ptr
 * Return: 0 if not palindrome else -1 if it is
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (current_pali(head, *head));
}

/**
 * current_pali Checks if a string is palindrome or not
 * @head: ptr at the in the list
 * @last: ptr at the end of list
 * Return: 0 if not palindrom else- 1 or not
 */
int current_pali(listint_t **head, listint_t *last)
{
	if (last == NULL)
		return (1);
	if (current_pali(head, last->next) && (*head)->n == last->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
