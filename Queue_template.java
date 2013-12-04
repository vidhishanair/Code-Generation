import java.util.Scanner;
public class Queue 
{
    QNode head;
    Scanner in;
    int number = 0;
    public Queue()
    {

        head = null;
	in = new Scanner(System.in);

    }

    public QNode create()
    {
        Scanner in = new Scanner(System.in);
	Scanner in1 = new Scanner(System.in);
        <attributes accept>
        QNode add = new QNode(<attribute list>);
        return add;
    }

    public void insert()
    {
         QNode add = create();
         if(head == null)
         {
             head = add;
         }
         else
         {
             QNode temp = head;
	         
	     while(temp.next!=null)
	     {
		//prev=temp;
		temp=temp.next;
	     }
	     temp.next=add;
        } 
	number++;
    }    

    public void delete()
    {
	if(number!=0)
	{
		QNode temp=head;
		head=head.next;
		temp.next=null;
	}
	else
		System.out.println("Empty queue");
    }
    public void no_node(QNode root)
    {
            if(root != null)
            {
                  no_node(root.next);
                  number++;

            }
    }

    public void display()
    {
	QNode temp = head;
        while(temp!=null)
        {
             <print statements>
	     temp = temp.next;	
        }
    }
}

