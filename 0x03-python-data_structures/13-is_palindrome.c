#include "lists.h"

/**
 * reverse_listint - reverse a linked list
 * @head: head pointer
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *temp = *head;
	listint_t *next = NULL;

	while (temp)
	{
		next = temp->next;
		temp->next = prev;
		prev = temp;
		temp = next;
	}
	*head = prev;
}
/**
 * is_palindrome - checks if a linked list is a palindrome.
 * @head: head pointer.
 * Return: 1 is its otherwise 0.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *temp = *head;
	listint_t *ptr = NULL;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	while (1)
	{
		fast = fast->next->next;
		if (fast == NULL)
		{
			ptr = slow->next;
			break;
		}
		if (!fast->next)
		{
			ptr = slow->next->next;
			break;
		}
		slow = slow->next;
	}
	reverse_listint(&ptr);
	while (ptr  && temp)
	{
		if (temp->n == ptr->n)
		{
			ptr = ptr->next;
			temp = temp->next;
		}
		else
			return (0);
	}
	if (!ptr)
		return (1);
	return (0);
}
