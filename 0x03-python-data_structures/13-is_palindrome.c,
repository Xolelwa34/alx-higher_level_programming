#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - Reverses the elements of the list
 * @head: A pointer to the first node of the list
 *
 * Return: A pointer to head of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome -Verify if a singly linked list is a palindrome.
 * @head:head of the linked list
 *
 * Reurn: -1 if the linked list is palindrome, -0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *val, *num;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		size++;
		temp = temp->next;
	}

	temp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		temp = temp->next;

	if ((size % 2) == 0 && temp->n != temp->next->n)
		return (0);

	temp = temp->next->next;
	val = reverse_listint(&temp);
	num = val;

	temp = *head;
	while (val)
	{
		if (temp->n != val->n)
			return (0);
		temp = temp->next;
		val = val->next;
	}
	reverse_listint(&num);

	return (1);
}
