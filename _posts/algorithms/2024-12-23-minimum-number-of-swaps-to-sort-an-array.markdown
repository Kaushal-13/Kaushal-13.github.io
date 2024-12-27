---
layout: post
title:  "Minimum no of swaps to sort an array."
categories: [Algorithms]
---

So I was solving the [leetcode Problem of the Day](https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/description/) and the bfs is strong with this one.(Bad reference) however something that amazed me was the algorithm required to find the minimum number of operations to sort an array and the solution was pretty nice. So I thought I would share it.(This is my first serious post and I hope many more are to come.)

# Solution.
Okay before everythin else , it is important to break down the array into two parts the elements that are already in place and those that aren't.
For example if Arr = [1,3,4,2,5] then (1,5) are in place whereas (3,4,2) are not.
This is an important bifurcation to make as we shall never touch those who are already in place.

Now, you may find the solution easily on other sites but I will try to mark the route as to how to reach such a solution.

Firstly let us define the sorted array as sorted_arr and our input as arr, now I define the delta of the array as the number of elements that are not in the correct position.

```python
def delta(arr, sorted_arr):
    delta_count = 0
    for a, b in zip(arr, sorted_arr):
        delta_count += (a != b)
    return delta_count
```
Note that the delta of the sorted array would be 0.


Now everytime we do such an operation the delta of the array is reduced by atleast 1.
 
So my solution is this, we pick up an index i if the element on arr[i] is in it's correctplace then no problem else we do this,
Swap the element on the ith index to its correct place and repeat.
These operations always reduce the delta by atleast one and hence we can argue that they are optimal.


So basically,
```python
i = 0
while i < len(arr):
    correct_index = # index where arr[i] should actually belong.
    if i != correct_index:
        arr[i], arr[correct_index] = arr[correct_index], arr[i] 
    else:
        i += 1
```

## Why does this work though.

Let us look at an element that is on position i, if we pick it up and put it in some other place we have created a blank at the position i now the next element has to either be at position i or somewhere else in the latter case the gap is still maintained which means that eventually one would have to place the element in the gap, which is the reason why the algorithm is correct.
And this understanding is important for the because now one can observe that if we keep on swapping at a position then eventually the element that is supposed to be at the position would be there.
A good way to understand this would be this video by Ted Ed.
<!--  Add link above.-->

Sorry for the dearth of Animations and stuff, I am still learning so would add them later down the road.

