#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * insert_node -Inserts a number into a singly linked list_t
 * @head: pointer to head
 * @number: value
 *
 * Return: the address of the new node,0 if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *prev;
	unsigned int index = 0, i = 0;
	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (index == 0)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	prev = *head;
	while (i != index - 1 && prev != NULL)
	{
		prev = prev->next;
		i++;
	}

	if (i == index - 1 && prev != NULL)
	{
		new->next = prev->next;
		prev->next = new;
		return (new);
	}
	return (NULL);
}
