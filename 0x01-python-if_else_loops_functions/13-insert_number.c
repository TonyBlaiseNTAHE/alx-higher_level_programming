#include "lists.h"

/**
 * inset_node - inserts a number into a sorted singly linked list.
 * @head: head pointer
 * @number: the data.
 * Return: the address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *ptr = NULL;
	listint_t *holder = NULL;

	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL || number <= (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	ptr = *head;
	while (ptr != NULL && ptr->n < number)
	{
		holder = ptr;
		ptr = ptr->next;
	}
	holder->next = new;
	new->next = ptr;
	return (new);
}
