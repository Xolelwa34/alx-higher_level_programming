#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - A function that checks if a singly-linked list contains a cycle.
 * @list: Singly- linked list
 *
 * Return: -1 if theres a cycle, -0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *teen, *finder;

	if (list == NULL || list->next == NULL)
		return (0);

	teen = list->next;
	finder = list->next->next;

	while (teen && finder && finder->next)
	{
		if (teen == finder)
			return (1);

		teen = teen->next;
		finder = finder->next->next;
	}

	return (0);
}
