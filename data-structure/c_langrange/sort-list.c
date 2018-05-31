#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct List
{
	int  data;
	struct List  *next;

}NODE;


NODE *  init_node(int n)
{
	NODE *list, *p1,*p2;
	int a;
	int i;
	list =NULL;
	printf("enter %d number:\n", n);
	for(i = 0; i < n; i ++)
	{
		scanf("%d",&a);
		p1 = (NODE *)malloc(sizeof(NODE));
		p1->data = a;
		p1->next = NULL;
		if(NULL == list)
		{
			list = p1;
		}
		else
		{
			p2->next = p1;
		}
		p2 = p1;
	}	
	p2->next = NULL;
	return list;
}

NODE * sort (NODE *list)
{
	NODE *p,*q;
	int t;
	for(p = list; p != NULL; p = p->next)
	{
		for(q= p->next; q != NULL; q = q->next)
		{		
			if(p->data > q->data)
			{
				t = p->data;
				p->data = q->data;
				q->data = t;


			}
		}
	}
	return list;


}


void printnode(NODE * list)
{
	int i;
	NODE *lp = list;
	while(lp != NULL && NULL !=lp->next)
	{
		printf("node = %d\n",lp->data);
		lp = lp->next;
	}
}
int main()
{
	int n;
	NODE * head;
	printf("enter num:\n");
	scanf("%d",&n);
	head = init_node(n);
	head = sort(head);
	printnode(head);
	printf("\n");
	free(head);
	return 0;

}
