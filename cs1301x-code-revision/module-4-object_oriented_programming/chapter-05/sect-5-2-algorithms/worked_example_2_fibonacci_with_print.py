#As before, our core function below hasn't changed. What
#has changed is that we've added print statements so we can
#see a bit about how the program is running.

def fib(n):
    if n == 1 or n == 2:
        print("Found fib(", n, "): returning 1!", sep = "")
        return 1
    
    #As with the factorial function, we want to print every
    #time we're about to create a new call to Fibonacci,
    #and every time such a call is completed.
    
    else:
        print("Finding fib(", n, "): fib(", n - 1, ") + fib(", n-2, ")", sep = "")
        result =  fib(n - 1) + fib(n - 2)
        print("Found fib(", n, "): ", result, sep = "")
        return result

#Now if we run this, we'll see a lot more output. Feel free
#to change this line to visualize different Fibonacci
#numbers.
print("fib(5) is", fib(5))

#The output here is more complex; you may want to copy it
#into another window to read it.
#
#When fib(5) is first called, it wants to calculate fib(4)
#and fib(3). So, it calls fib(4) first, which demands fib(3)
#and fib(2). So, it calls fib(3), which demands fib(2) and
#fib(1). Those are both the base case, so both return 1.
#So, in the execution order, we see fib(5), then fib(4),
#then fib(3), then fib(2), then fib(1).
#
#Once fib(2) and fib(1) have run, then fib(3) can finish,
#and so the next statement printed is the result of fib(3).
#Once fib(3) is finished, then we can finish fib(4) by
#finding fib(2). fib(2) is again 1, so the next line is
#fib(2).
#1)
#Once fib(3) and fib(2) have finished, we can finish
#fib(4), so the next statement printed is the result of
#fib(4).
#
#Now that fib(4) is finished, we're all the way back to the
#first call, which wanted fib(4) + fib(3). Now, the rest of
#the execution is evaluating fib(3), which immediately
#demands fib(2) and fib(1). So, the next two lines are the
#results of fib(2) and fib(. Once those are done, fib(3)
#is finished again.
#
#Now fib(4) and fib(3) are both finished, so the very first
#line can end: fib(4) + fib(3) = 3 + 2 = 5.
# The output is below:
# Finding fib(5): fib(4) + fib(3)
# Finding fib(4): fib(3) + fib(2)
# Finding fib(3): fib(2) + fib(1)
# Found fib(2): returning 1!
# Found fib(1): returning 1!
# Found fib(3): 2
# Found fib(2): returning 1!
# Found fib(4): 3
# Finding fib(3): fib(2) + fib(1)
# Found fib(2): returning 1!
# Found fib(1): returning 1!
# Found fib(3): 2
# Found fib(5): 5
# fib(5) is 5

################## detailed note below #######################
#     Finding fib( 5 ): fib( 4 ) + fib( 3 )

#         Code: This comes from the else block in fib(5). The code is about to calculate fib(4) + fib(3).

#         Sequence: This is the very first call, fib(5). It needs to compute fib(4) and fib(3).

#     Finding fib( 4 ): fib( 3 ) + fib( 2 )

#         Code: Inside the call to fib(4) (which was initiated by fib(5)), the else block is executed. It needs fib(3) and fib(2).

#         Sequence: fib(5) has called fib(4) first, and now fib(4) is calling fib(3) and fib(2).

#     Finding fib( 3 ): fib( 2 ) + fib( 1 )

#         Code: Inside the call to fib(3) (initiated by fib(4)), the else block executes, needing fib(2) and fib(1).

#         Sequence: We're going deeper: fib(5) -> fib(4) -> fib(3).

#     Found fib( 2 ): returning 1!

#         Code: fib(2) hits the if n == 1 or n == 2 condition (base case), so it prints this message and returns 1.

#         Sequence: fib(3) called fib(2), which is a base case.

#     Found fib( 1 ): returning 1!

#         Code: fib(1) also hits the base case and returns 1.

#         Sequence: fib(3) had also called fib(1), another base case.

#     Found fib( 3 ): 2

#         Code: Now that fib(2) and fib(1) have returned, fib(3) can complete its calculation: 1 + 1 = 2. It prints this and returns 2.

#         Sequence: fib(3) is now finished, returning its result to fib(4).

#     Found fib( 2 ): returning 1!

#         Code: fib(4) now needs fib(2), which hits the base case again.

#         Sequence: fib(4) called fib(2) after getting the result of fib(3).

#     Found fib( 4 ): 3

#         Code: fib(4) has received fib(3) (which was 2) and fib(2) (which was 1). It calculates 2 + 1 = 3, prints this, and returns 3.

#         Sequence: fib(4) is done and returns its result back to the initial fib(5) call.

#     Finding fib( 3 ): fib( 2 ) + fib( 1 )

#         Code: Back in the original fib(5) call, it now needs fib(3). It goes into the else block and will need fib(2) and fib(1).

#         Sequence: fib(5) had already gotten fib(4). Now it's calculating the needed fib(3). Notice that fib(3) is being calculated again—this is the inefficiency of the simple recursive approach.

#     Found fib( 2 ): returning 1!

#         Code: fib(2) is a base case.

#         Sequence: Same as before when fib(3) was calculated for the first time.

#     Found fib( 1 ): returning 1!

#         Code: fib(1) is a base case.

#         Sequence: Same as before.

#     Found fib( 3 ): 2

#         Code: fib(3) calculates 1 + 1 = 2 again.

#         Sequence: fib(3) is finished (again), returning to fib(5).

#     Found fib( 5 ): 5

#         Code: fib(5) has received fib(4) (which was 3) and fib(3) (which was 2). It calculates 3 + 2 = 5, prints this, and returns 5.

#         Sequence: The initial fib(5) call is complete.

#     fib(5) is 5

#         Code: This comes from the final print("fib(5) is", fib(5)) statement outside the function.

#         Sequence: The program has finished calculating fib(5).


# The output shows the order in which the fib() function is called and the results returned at each step. 
# You can see how the recursive calls branch out and how the base cases are crucial for eventually
# returning values back up the call chain. The sequence also highlights the redundant calculations that occur in this simple recursive solution.