import java.util.Scanner;




public class QueueMain {



    /**

     * @param args the command line arguments

     */

    public static void main(String[] args) 

    {

        Queue queue = new Queue();
        System.out.println("-------Queue------");
        Scanner in = new Scanner(System.in);

        int choice = 0;

        while(choice <= 4 && choice >= 0)

        {

            System.out.println("Enter \n 1. Insert \n 2. Delete \n 3. Count nodes \n 4.Display \n 5. Exit");

            choice = in.nextInt();

            switch(choice)

            {

                case 1:

                {

                    System.out.println("Inserting");

                    queue.insert();

                    break;

                }

                case 2:

                {

                    System.out.println("Deletion");

                     queue.delete();

                     break;

                }

                case 3:

                {

                    System.out.println("The number of nodes are:");

                    queue.no_node(queue.head);

                    System.out.println(queue.number);

                    queue.number = 0;

                    break;

                }

		case 4:
		{
                        System.out.println("Queue holds \n");
			queue.display();
			break;
		}

            }

        }

    }

}
