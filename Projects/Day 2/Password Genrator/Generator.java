import java.util.Random;

public class Generator {


    static String generate_password(int size) {
        // Define character sets
        String upper_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String lower_chars = "abcdefghijklmnopqrstuvwxyz";
        String number_chars = "1234567890";
        String special_chars = "!@#$%^&*()_+-/.,<>?;':\"[]{}\\|`~";

        // Combine all character sets
        String chars = "";
        chars += upper_chars;
        chars += lower_chars;
        chars += number_chars;
        chars += special_chars;

        // Initialize the password with one character from each set
        String password = "";
        password += upper_chars.charAt((int) (Math.random() * upper_chars.length()));
        password += lower_chars.charAt((int) (Math.random() * lower_chars.length()));
        password += number_chars.charAt((int) (Math.random() * number_chars.length()));
        password += special_chars.charAt((int) (Math.random() * special_chars.length()));

        Random rnd = new Random();
        // Generate remaining characters for the password
        while (password.length() < size) {
            int index = (int) (rnd.nextFloat() * chars.length());
            password += chars.charAt(index);
        }

        // Shuffle the password
        String shuffled = "";
        while (password.length() > 0) {
            int index = (int) (rnd.nextFloat() * password.length());
            shuffled += password.charAt(index);
            password = password.substring(0, index) + password.substring(index + 1);
        }

        return shuffled;
    }
}
