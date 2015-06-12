
/**
 * Write a description of class Student here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Student
{
// the student’s full name
private String name;
// the student ID
private String id;
// the amount of credits for study taken so far
private int credits;


/**
 * Create a new student with a given name and ID number.
 */
public Student(String fullName, String studentID)
{
    name = fullName;
    id = studentID;
    credits = 0;
}
/**
 * Return the full name of this student.
 */
public String getName()
{
    return name;
}
/**
 * Set a new name for this student.
 */
public void changeName(String newName)
{
    name = newName;
}
/**
 * Return the student ID of this student.
 */
public String getStudentID()
{
return id; }
/**
 * Add some credit points to the student’s
 * accumulated credits.
 */
public void addCredits(int newCreditPoints)
{
    credits += newCreditPoints;
}
}
