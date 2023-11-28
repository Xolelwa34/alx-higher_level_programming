#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - Checks if a linked list contains a cycle
 * @list: Alinked list to check
 *
 * Return: 1 if there's a cycle, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *check, *write;

	if (list == NULL || list->next == NULL)
		return (0);

	check = list->next;
	write = list->next->next;

	while (check && write && write->next)
	{
		if (check == write)
			return (1);

		check = check->next;
		write = write->next->next;
	}

	return (0);
}
