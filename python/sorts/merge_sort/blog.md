# Merge Sort

* We call merge sort on our un-ordered list, it splits the list in the middle and recursively sorts both halves
![screen shot](1.png)
* recursion is repeated until base case (length is less than or equal to 1) is met
![screen shot](2.png)
* merge is then used to zipper these sorted sub-lists together, maintaining order
![screen shot](3.png)
* and then repeated for the other half of the original sub-list
![screen shot](4.png)
* Once both sub lists are ordered they are zippered together by merge
![screen shot](5.png)
* and the final list is sorted
![screen shot](6.png)
