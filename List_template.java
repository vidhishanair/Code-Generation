import java.util.Scanner;
public class List 
{
    ListNode head;
    Scanner in;
    int number = 0;
    public List()
    {

        head = null;
	in = new Scanner(System.in);

    }

    public ListNode create()
    {
        Scanner in = new Scanner(System.in);
	Scanner in1 = new Scanner(System.in);
        <attributes accept>
        ListNode add = new ListNode(<attribute list>);
        return add;
    }

    public void insert()
    {
         ListNode add = create();
         if(head == null)
         {
             head = add;
         }
         else
         {
             ListNode temp = head;
	     System.out.println("Enter the position to insert:");
	     int pos = in.nextInt();
             ListNode prev=null;
	     int count=1;
	     if(pos==1)
	     {
               add.next=head;
               head=add;
             }
             else
             {
              while(count<=pos)
              {
               count++;
               prev=temp;
               temp=temp.next;
              }
              if(count==pos)
	      {
               add.next=add;
               add.next=temp;
              }
              else
              {
               System.out.println("Position out of bounds");
              }
             }
        }
    }    

    public void no_node(ListNode root)
    {
            if(root != null)
            {
                  no_node(root.next);
                  number++;

            }
    }

    public void display()
    {
	ListNode temp = head;
        while(temp!=null)
        {
             <print statements>
	     temp = temp.next;	
        }
    }
}
