using System;
using System.ComponentModel;
public class HelloWorld
{
    public static void Main(string[] args)
    {
        Console.WriteLine ("Hello Mono World");
    }
}

 public class entity: INotifyPropertyChanged
 {public event PropertyChangedEventHandler PropertyChanged;
        protected void OnPropertyChanged(string name = null)
        {
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(name));
        }

 }
 public class procedural:entity 
 {
 
 }

public definitive:entity 
 {
 
 }
public definitive:entity 
 {
 
 }

public definitive:entity 
 {
 
 }