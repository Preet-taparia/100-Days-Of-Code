import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean shouldContinue = true;

        System.out.println("Welcome to Password Generator and Checker.");
        while (shouldContinue) {
            System.out.println("If you want to generate a password, press 1.");
            System.out.println("If you want to check password strength, press 2.");
            System.out.println("To stop the program, press 0.");

            int input = sc.nextInt();

            switch (input) {
                case 1:
                    System.out.println("Enter the desired length of the password:");
                    int size = sc.nextInt();
                    String newPassword = Generator.generate_password(size);
                    System.out.println(newPassword);
                    break;
                case 2:
                    System.out.println("Enter the password to check its strength:");
                    String password = sc.next();
                    Password obj_check = new Password(password);
                    System.out.println("Password strength score: " + obj_check.calculateScore());
                    break;
                case 0:
                    shouldContinue = false;
                    break;
                default:
                    System.out.println("Invalid input. Please provide correct information.");
                    break;
            }
        }

        sc.close();
    }
}
