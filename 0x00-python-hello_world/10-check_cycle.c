#include "lists.h"
#include "stdio.h"

/**
 * check_cycle - function entry-point
 *
 * Description: prints all the elements of a list_t list
 * @head: pointer to singly linked list
 * Return: 1 if there is a cycle, 0 otherwise
 */

int check_cycle(listint_t *head)
{
	nodePtr temp1, temp2, temp3;

	if (head)
	{
		if (head == head->next)
			return (1);
		for (temp1 = head->next; temp1; temp1 = temp1->next->next)
		{
			if (temp1->next)
				temp3 = temp1->next;
			for (temp2 = head; temp2 != temp1; temp2 = temp2->next)
			{
				if (temp2 == temp1->next || temp2 == temp3->next)
					return (1);
			}
		}
	}
	return (0);
}
