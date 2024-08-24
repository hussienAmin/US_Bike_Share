public class EngWord
{
public int Id{get;set;}
public string Word{get;set;}
}
public class ArWord
{
public int Id{get;set;}
public string Word{get;set;}
}
public class EngAr
{
public EnWord EnWord{get;set;}
public int ArId{get;set;}
public ArWord ArWord{get;set;}
public int EnId{get;set;}

}