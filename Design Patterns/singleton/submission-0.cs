public class Singleton 
{

    private static volatile Singleton uniqueInstance = null;
    private String value = null;

    private Singleton() 
    {
      
    }

    public static Singleton getInstance() 
    {
        if (uniqueInstance == null)
        {
            uniqueInstance = new Singleton();
        }

        return uniqueInstance;
    }

    public string getValue() 
    {
        return this.value;
    }

    public void setValue(string value)
    {
        this.value = value;
    }
}
