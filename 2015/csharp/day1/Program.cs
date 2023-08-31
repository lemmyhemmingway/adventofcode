// See https://aka.ms/new-console-template for more information
using System;
using System.IO;

using (var sr = new StreamReader("../../inputs/day1.txt"))
{
  var data = sr.ReadToEnd();
  var arr = data.ToCharArray();
  var floor = 0;
  var position = 0;
  foreach (var item in arr)
  {
     if (item == '(')
     {
       floor += 1;
     } else if (item == ')') {
       floor -= 1;
     }
  }
  Console.WriteLine(floor);
  floor = 0;
  foreach (var item in arr)
  {
    position += 1;
     if (item == '(')
     {
       floor += 1;
     } else if (item == ')') {
       floor -= 1;
     }
     if (floor == -1) {
       break;
     }
  }

  Console.WriteLine(position);
}
