#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * insert_node -Inserts a number into a singly linked list_t
 * @h: pointer to head
 * @num: value 
 *
 * Return: the address of the new node,0 if failed
 */

listint_t *insert_node(listint_t **head, int num)
{
	listint_t *new, *traverse;
	unsigned int index = 0, i = 0;
	if (h == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = num;
	if (index == 0)
	{
		new->next = *h;
		*h = new;
		return (new);
	}
	traverse = *h;
	while (i != index - 1 && traverse != NULL)
	{
		traverse = traverse->next;
		i++;
	}

	if (i == index - 1 && traverse != NULL)
	{
		new->next = traverse->next;
		traverse->next = new;
		return (new);
	}
	return (NULL);
}
