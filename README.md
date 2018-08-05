# TicTacToe
TicTacToe game 2 player in python

## FAIL BRANCH- _in progress_
### changes:
1. added function winning_statement to reduce repeated code in winner function - succesful

2. added function (currently commented out lines 19 to 28 and moved as nested function inside func **winner**) **index_temp_score** to reduce repeated code - in progress-**not working-> see below:**
  ### challenges:
  * scope of variables Xscoret and Oscoret
  * not updating outside of function
  * **Index_temp_score** func is called in _while_ loop(s) in func **winner** so each time function is called, 
        non-updated variable is being used
  ### result: 
   * game intiates, runs, but will not determine winner, cat's game counter still works
  ### attempts to fix:
	1. tried to declare Global variables:  error SyntaxError: name 'Oscoret' is local and global python
	2. tried nonlocal declaration: error due to python version only avail in 3
	3. tried to wrap variable in mutable container as a list: no change
	4. tried to move function to a nested function: no change
