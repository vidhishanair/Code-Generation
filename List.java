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
        System.out.println("Enter the USN:");
	int USN = in.nextInt();
	System.out.println("Enter the name:");
	String name = in1.nextLine();
	
        ListNode add = new ListNode(USN,name);
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
             System.out.println("USN: "+temp.USN);
	System.out.println("name: "+temp.name);
	
	     temp = temp.next;	
        }
    }
}



