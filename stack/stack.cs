var stack = new Stack<string>();

stack.Push("one");
stack.Push("two");
stack.Push("three");

stack.Peek(); // three  

stack.Pop(); // three   
stack.Pop(); // two
stack.Pop(); // one
stack.Pop(); // InvalidOperationException