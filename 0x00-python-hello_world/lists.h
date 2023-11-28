#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

typedef struct listint_s
{
	int n;
	struct lint_s *next;
}listint_t;

void free_listint(listint_t *head);
size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_ **head, const int n);
int check_cycle(listint_t *list);

#endif /* LITS_H */
