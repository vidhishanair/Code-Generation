import java.util.Scanner;




public class ListMain {



    /**

     * @param args the command line arguments

     */

    public static void main(String[] args) 

    {

        List list = new List();
	System.out.println("-------List-------");

        Scanner in = new Scanner(System.in);

        int choice = 0;

        while(choice <= 3 && choice >= 0)

        {

            System.out.println("Enter \n 1. Insert \n  2. Count nodes \n 3.Display \n 4. Exit");

            choice = in.nextInt();

            switch(choice)

            {

                case 1:

                {

                    System.out.println("Inserting");

                    list.insert();

                    break;

                }


                case 2:

                {

                    System.out.println("The number of nodes are:");

                    list.no_node(list.head);

                    System.out.println(list.number);

                    list.number = 0;

                    break;

                }

		case 3:
		{
                        System.out.println("List contents \n");
			list.display();
			break;
		}

            }

        }

    }

}
