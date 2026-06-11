public class Main {
    public static void main(String[] args) {

        int[] numbers = {10, 25, 5, 40, 15};

        int highest = numbers[0];
        int lowest = numbers[0];
        int sum = 0;

        for (int num : numbers) {
            if (num > highest) {
                highest = num;
            }

            if (num < lowest) {
                lowest = num;
            }

            sum += num;
        }

        double average = (double) sum / numbers.length;

        System.out.println("Highest: " + highest);
        System.out.println("Lowest: " + lowest);
        System.out.println("Average: " + average);
    }
}
