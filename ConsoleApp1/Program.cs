using System;
//תרגיל 1

class Program
{
    // ====== הגדרות ======

    class MyClass
    {
        public int Value;
    }

    struct MyStruct
    {
        public int Value;
    }

    // פונקציה שמקבלת class – תמיד by reference
    static void ChangeClass(MyClass obj)
    {
        obj.Value = 999;
    }

    // פונקציה שמקבלת struct – הוא מועבר by value (לא יצליח לשנות את המקורי)
    static void ChangeStruct(MyStruct s)
    {
        s.Value = 999;
    }

    // פונקציה שמקבלת struct כ־ref – תצליח לשנות את המקורי
    static void ChangeStructRef(ref MyStruct s)
    {
        s.Value = 555;
    }


    // ====== MAIN ======
    static void Main()
    {
        RunExercise1();//תרגיל1
        MemoryAllocationExperiment();//תרגיל6
    }
    static void RunExercise1()
    {
        Console.WriteLine("============== exc 1 =============");

        Console.WriteLine("=== הדגמה א: השמה בין משתנים ===");

        // --- CLASS (by reference)
        MyClass c1 = new MyClass { Value = 10 };
        MyClass c2 = c1;       // שניהם מצביעים לאותו אובייקט
        c2.Value = 20;

        Console.WriteLine("Class:");
        Console.WriteLine($"c1.Value = {c1.Value}");  // יציג 20
        Console.WriteLine($"c2.Value = {c2.Value}");  // יציג 20

        // --- STRUCT (by value)
        MyStruct s1 = new MyStruct { Value = 10 };
        MyStruct s2 = s1;      // העתקה מלאה
        s2.Value = 20;

        Console.WriteLine("\nStruct:");
        Console.WriteLine($"s1.Value = {s1.Value}");  // יציג 10
        Console.WriteLine($"s2.Value = {s2.Value}");  // יציג 20


        Console.WriteLine("\n=== הדגמה ב: העברה לפונקציה ===");

        // --- CLASS
        MyClass c3 = new MyClass { Value = 10 };
        ChangeClass(c3);
        Console.WriteLine($"After ChangeClass: c3.Value = {c3.Value}");  // יציג 999

        // --- STRUCT
        MyStruct s3 = new MyStruct { Value = 10 };
        ChangeStruct(s3);
        Console.WriteLine($"After ChangeStruct: s3.Value = {s3.Value}");  // עדיין 10 — לא השתנה

        // --- STRUCT ע"י ref (כן ישתנה!)
        MyStruct s4 = new MyStruct { Value = 10 };
        ChangeStructRef(ref s4);
        Console.WriteLine($"After ChangeStructRef: s4.Value = {s4.Value}");  // יציג 555
    }
    
//תרגיל 6

    public static void MemoryAllocationExperiment()
    {

        Console.WriteLine("============== exc 6 =============");

        Console.WriteLine("===== חלק א' – הקצאת מערכים בסיסיים =====");
        long baselineMemory = GC.GetAllocatedBytesForCurrentThread();

        // 1. Allocate an array of integers
        int[] intArray = new int[10000];
        long afterIntArray = GC.GetAllocatedBytesForCurrentThread();

        // 2. Allocate an array of doubles
        double[] doubleArray = new double[10000];
        long afterDoubleArray = GC.GetAllocatedBytesForCurrentThread();

        // 3. Allocate an array of strings
        string[] stringArray = new string[10000];
        long afterStringArray = GC.GetAllocatedBytesForCurrentThread();

        Console.WriteLine($"Baseline Memory: {baselineMemory} bytes");
        Console.WriteLine($"Int Array Allocation: {afterIntArray - baselineMemory} bytes");
        Console.WriteLine($"Double Array Allocation: {afterDoubleArray - afterIntArray} bytes");
        Console.WriteLine($"String Array Allocation: {afterStringArray - afterDoubleArray} bytes");


        Console.WriteLine("\n===== חלק ב' – מערכים של struct בגדלים שונים =====");

        long beforeStructs = GC.GetAllocatedBytesForCurrentThread();

        SmallStruct[] smallStructArr = new SmallStruct[10000];
        long afterSmallStruct = GC.GetAllocatedBytesForCurrentThread();

        MediumStruct[] mediumStructArr = new MediumStruct[10000];
        long afterMediumStruct = GC.GetAllocatedBytesForCurrentThread();

        LargeStruct[] largeStructArr = new LargeStruct[10000];
        long afterLargeStruct = GC.GetAllocatedBytesForCurrentThread();

        Console.WriteLine($"SmallStruct Array Allocation:  {afterSmallStruct - beforeStructs} bytes");
        Console.WriteLine($"MediumStruct Array Allocation: {afterMediumStruct - afterSmallStruct} bytes");
        Console.WriteLine($"LargeStruct Array Allocation:  {afterLargeStruct - afterMediumStruct} bytes");


        Console.WriteLine("\n===== חלק ג' – מערכים של class בגדלים שונים =====");

        long beforeClasses = GC.GetAllocatedBytesForCurrentThread();

        SmallClass[] smallClassArr = new SmallClass[10000];
        long afterSmallClass = GC.GetAllocatedBytesForCurrentThread();

        MediumClass[] mediumClassArr = new MediumClass[10000];
        long afterMediumClass = GC.GetAllocatedBytesForCurrentThread();

        LargeClass[] largeClassArr = new LargeClass[10000];
        long afterLargeClass = GC.GetAllocatedBytesForCurrentThread();

        Console.WriteLine($"SmallClass Array Allocation:  {afterSmallClass - beforeClasses} bytes");
        Console.WriteLine($"MediumClass Array Allocation: {afterMediumClass - afterSmallClass} bytes");
        Console.WriteLine($"LargeClass Array Allocation:  {afterLargeClass - afterMediumClass} bytes");

    }
}


// ===== Structs for part B =====
public struct SmallStruct
{
    public int A; // 4 bytes
}

public struct MediumStruct
{
    public int A, B, C, D; // 16 bytes
}

public struct LargeStruct
{
    public long A, B, C, D, E, F; // 48 bytes
}


// ===== Classes for part C =====
public class SmallClass
{
    public int A;
}

public class MediumClass
{
    public int A, B, C, D;
}

public class LargeClass
{
    public long A, B, C, D, E, F;
}

