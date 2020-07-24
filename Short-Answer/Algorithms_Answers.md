#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(1)
the steps are the same no matter what the input is, it will always run the same equation

b) O(n log n)
the steps of the program decreases by half every time the loops runs, a function that does is falls under n log n.

c) O(n)
the equation scales linearly based on how big n grows. For each increment of n, the while loop inside grows proportionately with it.

## Exercise II

The building is essentially like an ordered list with no duplicates to which we know th max of. We need to find an unknown value within that list which sets the breaking point for the egg. If we drop an egg from each floor, starting from the lowest floor, we can find that magic number right when the egg breaks to which point we would have only broken one egg.

To do that we iterate the list from the beggining and see if the egg's break value is f, when it is f, we stop the iterations and return it to us.
