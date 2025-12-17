import java.util.Random;
import javax.crypto.spec.IvParameterSpec;

public class IvGenerator {

    public static IvParameterSpec generateIv() {
        Random random = new Random();
        byte[] iv = new byte[16];
        random.nextBytes(iv);
        IvParameterSpec ivSpec = new IvParameterSpec(iv);
        return ivSpec;
    }

    // Example usage
    public static void main(String[] args) {
        IvParameterSpec ivSpec = generateIv();
        System.out.println("IV length: " + ivSpec.getIV().length);
    }
}
