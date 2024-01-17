#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *next;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	next = current->next;

	while (next != NULL && next->n < number)
	{
		current = next;
		next = current->next;
	}
	current->next = new;
	new->next = next;
	return (new);
}
