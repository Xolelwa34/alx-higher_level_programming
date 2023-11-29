#include "lists.h"

/**
 * insert_node - Insert number into the list
 * @head: list pointer
 * @number: number to be added
 * Return: added node address, else NULL.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *older, *current;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	older = NULL;
	current = *head;

	for (; current != NULL && current->n < number;)
	{
		older = current;
		current = current->next;
	}

	new->next = current;

	if (older != NULL)
		older->next = new;
	else
		*head = new;

	return (new);
}
