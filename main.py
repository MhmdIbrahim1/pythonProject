# # for i in range(10):
# #     print(i)
#
#
# # n = int(input("Enter a number: "))  # Complexity: O(1)
# # for i in range(0, n):  # Complexity: O(n)
# #     i = i / 2  # Complexity: O(log n)
# #     print(i)
#
#
# # n = int(input("Enter a number: "))  # Complexity: O(1)
# # for i in range(0,n): # Complexity: O(n)
# #     print(i)
# # # Complexity: O(n)
#
# # n = int(input("Enter a number: "))  # Complexity: O(1)
# # for i in range(0, n):  # Complexity: O(n)
# #     for j in range(0, n):  # Complexity: O(log n)
# #         j = j / 2
# #         print(j)
# # # Complexity: O(n log n)
#
# # n = int(input("Enter a number: "))  # Complexity: O(1)
# # for i in range(0, n):  # Complexity: O(n)
# #     for j in range(0, n):  # Complexity: O(n)
# #         print(i*j)
# # # Complexity: O(n^2)
#
# # more examples
#
# # n = int(input("Enter a number: "))  # Complexity: O(1)
# # for i in range(0, n):  # Complexity: O(n)
# #     for j in range(0, n):  # Complexity: O(n)
# #         for k in range(0, n):
# #             print(i*j*k)
# # # Complexity: O(n^3)
#
# # n = int(input("Enter a number: "))  # Complexity: O(1)
# # for i in range(0, n):  # Complexity: O(n)
# #     for j in range(0, n):  # Complexity: O(n)
# #         for k in range(0, n):
# #             for l in range(0, n):
# #                 print(i*j*k*l)
#
# # # Complexity example of O(nlogn)
# # n = int(input("Enter a number: ")) # C
# # for i in range(0, n):  n
# #     for j in range(0, n): log n
# #         j = j / 2
# #         print(j)
# # # Complexity: O(n log n)
#
# # c + n + n * log n  = O(n log n)
#
# # c + n + n * log n  = O(n log n)
#
#
# """
# O(1) - Constant
# O(log n) - Logarithmic
# O(n) - Linear
# O(n log n) - Log Linear
# O(n^2) - Quadratic
# O(2^n) - Exponential
# """
#
# # Create X|O game with tkinter GUI to play with computer
#
import heapq
import tkinter as tk
from tkinter import messagebox
import random


# Create window
# window = tk.Tk()
# window.title("X|O")
# window.geometry("300x300")
#
# # Create buttons
# button1 = tk.Button(window, text=" ", font=("Arial", 20), height=3, width=6, command=lambda: button_click(button1))
# button2 = tk.Button(window, text=" ", font=("Arial", 20), height=3, width=6, command=lambda: button_click(button2))
# button3 = tk.Button(window, text=" ", font=("Arial", 20), height=3, width=6, command=lambda: button_click(button3))
# button4 = tk.Button(window, text=" ", font=("Arial", 20), height=3, width=6, command=lambda: button_click(button4))
# button5 = tk.Button(window, text=" ", font=("Arial", 20), height=3, width=6, command=lambda: button_click(button5))
# button6 = tk.Button(window, text=" ", font=("Arial", 20), height=3, width=6, command=lambda: button_click(button6))
# button7 = tk.Button(window, text=" ", font=("Arial", 20), height=3, width=6, command=lambda: button_click(button7))
# button8 = tk.Button(window, text=" ", font=("Arial", 20), height=3, width=6, command=lambda: button_click(button8))
# button9 = tk.Button(window, text=" ", font=("Arial", 20), height=3, width=6, command=lambda: button_click(button9))
#
# # Create grid
# button1.grid(row=0, column=0)
# button2.grid(row=0, column=1)
# button3.grid(row=0, column=2)
# button4.grid(row=1, column=0)
# button5.grid(row=1, column=1)
# button6.grid(row=1, column=2)
# button7.grid(row=2, column=0)
# button8.grid(row=2, column=1)
# button9.grid(row=2, column=2)
#
# # Create list of buttons
# buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]
#
# # Create list of possible winning combinations
# winning_combinations = [[button1, button2, button3], [button4, button5, button6], [button7, button8, button9],
#                         [button1, button4, button7], [button2, button5, button8], [button3, button6, button9],
#                         [button1, button5, button9], [button3, button5, button7]]
#
# # Create list of possible winning combinations
# winning_combinations = [[button1, button2, button3], [button4, button5, button6], [button7, button8, button9],
#                         [button1, button4, button7], [button2, button5, button8], [button3, button6, button9],
#                         [button1, button5, button9], [button3, button5, button7]]
#
#
# # Create function to check if there is a winner
# def check_winner():
#     for combination in winning_combinations:
#         if combination[0]["text"] == combination[1]["text"] == combination[2]["text"] == "X":
#             messagebox.showinfo("Winner", "X wins!")
#             window.destroy()
#         elif combination[0]["text"] == combination[1]["text"] == combination[2]["text"] == "O":
#             messagebox.showinfo("Winner", "O wins!")
#             window.destroy()
#
#
# # Create function to check if there is a tie
# def check_tie():
#     if button1["text"] != " " and button2["text"] != " " and button3["text"] != " " and button4["text"] != " " and \
#             button5["text"] != " " and button6["text"] != " " and button7["text"] != " " and button8["text"] != " " and \
#             button9["text"] != " ":
#         messagebox.showinfo("Tie", "It's a tie!")
#         window.destroy()
#
#

# # Create function to check if there is a winner or a tie
# def check_winner_or_tie():
#     check_winner()
#     check_tie()


# # Create function to check if button is empty
# def check_button_empty(button):
#     if button["text"] == " ":
#         return True
#     else:
#         return False
#
#
# def computer_move():
#     # Check for any winning moves for the computer
#     for combination in winning_combinations:
#         if combination[0]["text"] == combination[1]["text"] == "O" and check_button_empty(combination[2]):
#             combination[2]["text"] = "O"
#             check_winner_or_tie()
#             return
#
#         elif combination[1]["text"] == combination[2]["text"] == "O" and check_button_empty(combination[0]):
#             combination[0]["text"] = "O"
#             check_winner_or_tie()
#             return
#
#         elif combination[0]["text"] == combination[2]["text"] == "O" and check_button_empty(combination[1]):
#             combination[1]["text"] = "O"
#             check_winner_or_tie()
#             return
#
#     # Check for any blocking moves for the computer
#     for combination in winning_combinations:
#         if combination[0]["text"] == combination[1]["text"] == "X" and check_button_empty(combination[2]):
#             combination[2]["text"] = "O"
#             check_winner_or_tie()
#             return
#
#         elif combination[1]["text"] == combination[2]["text"] == "X" and check_button_empty(combination[0]):
#             combination[0]["text"] = "O"
#             check_winner_or_tie()
#             return
#
#         elif combination[0]["text"] == combination[2]["text"] == "X" and check_button_empty(combination[1]):
#             combination[1]["text"] = "O"
#             check_winner_or_tie()
#             return
#
#     # Play in a random empty square
#     empty_buttons = [button for button in buttons if check_button_empty(button)]
#     if empty_buttons:
#         button = random.choice(empty_buttons)
#         button["text"] = "O"
#         check_winner_or_tie()
#     else:
#         messagebox.showinfo("Tie", "It's a tie!")
#         window.destroy()
#
#
# # test
# def button_click(button):
#     if check_button_empty(button):
#         button["text"] = "X"
#         check_winner_or_tie()
#         computer_move()
#     else:
#         messagebox.showinfo("Error", "Button is not empty!")
#
#
# window.mainloop()
# -----------------------------------------------------------


# b) Design a more efficient algorithm to do the same task with less complexity
#
# def descending_order(arr):
#     n = len(arr)
#     result = [0] * n
#     for i in range(n):
#         count = 0
#         for j in range(n):
#             if arr[i] < arr[j]:
#                 count += 1
#         result[i] = count + 1
#     return result

#
# def descending_order(arr):
#     # Step 1
#     res = [0] * len(arr)
#     # Step 2
#     for i, val in enumerate(arr):
#         c = 1
#         for other in arr:
#             if other > val:
#                 c += 1
#         res[i] = c
#     # Step 3
#     return res
#
#
# def descending_order_efficient(arr):
#     # Get the length of the input array
#     n = len(arr)
#     # Create a dictionary that maps each unique value in the array to its rank (position when sorted in
#     # descending order) The rank of the largest value in the array is 1, the rank of the second-largest value is 2,
#     # and so on.
#     rank = {val: i + 1 for i, val in enumerate(sorted(arr, reverse=True))}
#     # Iterate through each element in the input array
#     for i in range(n):
#         # Replace each element in the input array with its rank (as determined by the rank dictionary)
#         arr[i] = rank[arr[i]]
#     # if equal values in the array, the rank of the first occurrence of the value will be used
#     if len(set(arr)) != n:
#         print("There are equal values in the array")
#     # Return the changed input array
#     return arr


# Test case 1
# arr1 = [10, 12, 17, 14, 8, 3, 22]
# print("First input array: ", arr1)
# print("Output", descending_order(arr1))
# print("\n")
#
# # Test case 2
# arr2 = [1, 2, 3, 4, 5]
# expected2 = [5, 4, 3, 2, 1]
# assert descending_order(arr2) == expected2
# print("Second input array: ", arr2)
# print("Output", descending_order(arr2))
# print("\n")
#
# # Test case 3
# arr3 = [5, 4, 3, 2, 1]
# expected3 = [1, 2, 3, 4, 5]
# assert descending_order(arr3) == expected3
# print("Third input array: ", arr3)
# print("Output", descending_order(arr3))

#
# def descending_order(arr):
#     # Initialize an empty array to store the result
#     res = [0] * len(arr)
#
#     # Loop through each element in arr
#     for i, val in enumerate(arr):
#         # Initialize a counter to keep track of the order
#         c = 1
#
#         # Loop through each element in arr
#         for other in arr:
#             # If other is greater than val, increment the counter
#             if other > val:
#                 c += 1
#
#         # Set the ith element in the result array to the order
#         res[i] = c
#
#     # Return the result array
#     return res


# ---------------------------

# def find_triplet(arr):
#     n = len(arr)
#     triplets = []
#     for i in range(n - 2):
#         for j in range(i + 1, n - 1):
#             if arr[i] > arr[j]:
#                 for k in range(j + 1, n):
#                     if arr[j] > arr[k]:
#                         triplets.append((arr[i], arr[j], arr[k]))
#     if len(triplets) == 0:
#         return None
#     else:
#         return max(triplets)
#
#
#

# #

# def find_triplet(arr):
#     n = len(arr)
#     triplet = []
#     for i in range(n-2):
#         for j in range(i+1, n-1):
#             for k in range(j+1, n):
#                 if arr[i] > arr[j] > arr[k]:
#                     if not triplet or sum(triplet) < arr[i] + arr[j] + arr[k]:
#                         triplet = [arr[i], arr[j], arr[k]]
#     return triplet

# def find_triplet(arr):
#     n = len(arr)
#     if n < 3:  # Check if the input array has less than three elements
#         return []  # If so, return an empty list
#     max_k = [0] * n  # Create an auxiliary array to store the index of the largest element to the right of each element
#     max_k[n - 1] = n - 1  # Initialize the last element of max_k as n-1
#     # Iterate through the elements of arr from right to left
#     for i in range(n - 2, -1, -1):
#         # If the current element is larger than the largest element to its right, set its index as the largest
#         if arr[i] > arr[max_k[i + 1]]:
#             max_k[i] = i
#         else:  # Otherwise, the index of the largest element to the right remains the same
#             max_k[i] = max_k[i + 1]
#     # Iterate through the elements of arr from left to right, up to the second-to-last element
#     for i in range(n - 2):
#         # Check if the current element is larger than the largest element to its right
#         if arr[i] > arr[max_k[i + 1]]:
#             # Iterate through the elements of arr to the right of the current element
#             for j in range(i + 1, n - 1):
#                 # Check if the current element and the current element to its right are larger than the largest
#                 # element to the right of the second element
#                 if arr[max_k[j + 1]] < arr[j] < arr[i]:
#                     # If so, return the triplet consisting of the current element, the second element,
#                     # and the largest element to the right of the second element
#                     return [arr[i], arr[j], arr[max_k[j + 1]]]
#     # If no triplet is found, return an empty list
#     return []

#
# def find_triplet(A):
#     # get the length of the array
#     n = len(A)
#     # Initialize an array to store the maximum values from A[0..i]
#     left_max = [0] * n
#     # Initialize an array to store the minimum values from A[i..n-1]
#     right_min = [0] * n
#
#     # Set the first element of left_max to the first element of A
#     left_max[0] = A[0]
#     # Loop through the second element of A to the last element
#     for i in range(1, n):
#         # Set the ith element of left_max to the maximum of value of between left_max[i-1] and A[i]
#         left_max[i] = max(left_max[i-1], A[i])
#
#     # Set the last element of right_min to the last element of A
#     right_min[n-1] = A[n-1]
#     # Loop through the second-to-last element of A to the first element
#     for i in range(n-2, -1, -1):
#         # Set the ith element of right_min to the minimum of value of between right_min[i+1] and A[i]
#         right_min[i] = min(right_min[i+1], A[i])
#
#     # Loop through the elements of A
#     for j in range(n):
#         # Check if left_max[j], A[j], and right_min[j] form a valid triplet
#         if left_max[j] > A[j] > right_min[j]:
#             # If so, return the triplet
#             print(left_max[j], A[j], right_min[j])
#             #return left_max[j], A[j], right_min[j]
#
#     return None
#
#
# arr = [9, 1, 6, 7, 3, 4, 5]
# print("First Input: ", arr)
# print(find_triplet(arr))
# #
# arr = [1, 2, 3, 3, 2, 1]
# print("Second Input: ", arr)
# print(find_triplet(arr))
#
# arr = [5, 4, 3, 2, 1]
# print("Third Input: ", arr)
# print(find_triplet(arr))


#
# def find_triplet(arr):
#     n = len(arr)
#     triplet = []
#     for i in range(n - 2):
#         a = arr[i]
#         for j in range(i + 1, n - 1):
#             b = arr[j]
#             for k in range(j + 1, n):
#                 c = arr[k]
#                 if a > b > c:
#                     if not triplet or sum([a, b, c]) > sum(triplet):
#                         triplet = [a, b, c]
#     return triplet
# triplet
#
# A = [9, 1, 6, 7, 3, 4, 5]
# print("First test case for input: ", A)
# print("output: ", find_triplet(A))
#
# A = [1, 2, 3, 3, 2, 1]
# print("Second test case for input: ", A)
# print("output: ", find_triplet(A))
#
# A = [5, 4, 3, 2, 1]
# print("Third test case for input: ", A)
# print("output: ", find_triplet(A))

# ---------------------------
#
# def longest_consecutive_subsequence(arr):
#     # Sort the array in ascending order
#     arr.sort()
#
#     # Initialize variables
#     max_length = 1
#     curr_length = 1
#
#     # Loop through the array
#     for i in range(len(arr) - 1):
#         # Check if the difference between the current and previous element is 1
#         if arr[i + 1] - arr[i] == 1:
#             curr_length += 1
#         else:
#             # Update max_length if curr_length is greater
#             max_length = max(max_length, curr_length)
#             # Reset curr_length to 1
#             curr_length = 1
#
#     # Update max_length if curr_length is greater
#     max_length = max(max_length, curr_length)
#
#     return max_length
#
#
# def longest_consecutive_subsequence_efficient(arr):
#     # Create an empty set to store the numbers in arr
#     num_set = set()
#
#     # Add all the numbers in arr to the set
#     for num in arr:
#         num_set.add(num)
#
#     # Initialize max_len to 0
#     max_len = 0
#
#     # Loop through each number in num_set
#     for num in num_set:
#         # If num-1 is not in num_set, then num is the start of a consecutive subsequence
#         if num - 1 not in num_set:
#             # Initialize curr_num and curr_len to num and 1, respectively
#             curr_num = num
#             curr_len = 1
#
#             # Increment curr_num and curr_len until curr_num+1 is not in num_set
#             while curr_num + 1 in num_set:
#                 curr_num += 1
#                 curr_len += 1
#
#             # Update max_len to be the maximum of max_len and curr_len
#             max_len = max(max_len, curr_len)
#
#     # Return the length of the longest consecutive subsequence
#     return max_len

# def longest_consecutive_subsequence_efficient(nums):
#     res = 0
#     nums = set(nums)
#     for num in nums:
#         if num - 1 not in nums:  # then num is the left most of the consecutive sequence
#             left = num
#             right = num
#             while right + 1 in nums:  # scan to find the right most of the consecutive sequence
#                 right += 1
#             res = max(res, right - left + 1)
#     return res

# def longestConsecutiveSequence(arr):
#     n = len(arr)
#     longestLength = 0
#     for i in range(n):
#         currElement = arr[i]
#         currLength = 1
#         while True:
#             found = False
#             for j in range(n):
#                 if arr[j] == currElement + 1:
#                     found = True
#                     break
#             if found:
#                 currElement += 1
#                 currLength += 1
#             else:
#                 break
#         longestLength = max(longestLength, currLength)
#     return longestLength


# A = [1, 3, 5, 9, 11]
# print(longestConsecutiveSequence(A))  # Output: 1
# # # Test case 1
# A = [2, 0, 6, 1, 5, 3, 7]
# print(longestConsecutiveSequence(A))
# # Test case 2
# A = [2, 4, 6, 3, 7, 4, 8, 1]
# print(longestConsecutiveSequence(A))
# # Test case 3
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(longestConsecutiveSequence(A))
# # Test case 4
# A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(longestConsecutiveSequence(A))
#
# # Test case 5
# A = [1, 3, 5, 7, 9]
# expected = 1
# assert longestConsecutiveSequence(A) == expected
#
# # Test case 6
# A = [5,2,3,1,4]
# print("input: ", A)
# print(longest_consecutive_subsequence(A))

# def descending_order_efficient(arr):
#     # Get the length of the input array
#     n = len(arr)
#     # Find the maximum value in the input array
#     max_val = max(arr)
#     # Initialize a list of counts, where the i-th element stores the number of occurrences of the value i in the input
#     # array
#     counts = [0] * (max_val + 1)
#     for val in arr:
#         counts[val] += 1
#     # Compute the prefix sums of the counts to get the rank of each value in the input array
#     rank = [0] * (max_val + 1)
#     rank[max_val] = 1
#     for i in range(max_val - 1, -1, -1):
#         rank[i] = rank[i+1] + counts[i+1]
#     # Iterate through each element in the input array and replace it with its rank
#     for i in range(n):
#         arr[i] = rank[arr[i]]
#     # Return the changed input array
#     return arr


#

# import time
#
# start_time = time.perf_counter()


# our code goes here

# def longest_consecutive_subsequence_efficient(arr):
#     # Create an empty set to store the numbers in arr
#     num_set = set()
#
#     # Add all the numbers in arr to the set
#     for num in arr:
#         num_set.add(num)
#
#     # Initialize max_len to 0
#     max_len = 0
#
#     # Loop through each number in num_set
#     for num in num_set:
#         # If num-1 is not in num_set, then num is the start of a consecutive subsequence
#         if num - 1 not in num_set:
#             # Initialize curr_num and curr_len to num and 1, respectively
#             curr_num = num
#             curr_len = 1
#
#             # Increment curr_num and curr_len until curr_num+1 is not in num_set
#             while curr_num + 1 in num_set:
#                 curr_num += 1
#                 curr_len += 1
#
#             # Update max_len to be the maximum of max_len and curr_len
#             max_len = max(max_len, curr_len)
#
#     # Return the length of the longest consecutive subsequenc
#     return max_len
#
# def LCS_Efficient(arr):
#     # Initialize map and maxCount
#     map = {}
#     maxCount = 1
#     for i in arr:
#         # Skip if i is already in map
#         if i in map:
#             continue
#         # Add i to map
#         map[i] = 1
#         # Check if i-1 is in map and update maxCount
#         if i - 1 in map:
#             maxCount = max(maxCount, merge(map, i - 1, i))
#         # Check if i+1 is in map and update maxCount
#         if i + 1 in map:
#             maxCount = max(maxCount, merge(map, i, i + 1))
#     return maxCount
#
# def merge(map, left, right):
#     # Find upper and lower bounds of sequence
#     upper = right + map[right] - 1
#     lower = left - map[left] + 1
#     # Calculate length of sequence
#     length = upper - lower + 1
#     # Update map with new length
#     map[upper] = length
#     map[lower] = length
#     return length
#
# def longestConsecutiveSequence(arr):
#     n = len(arr)
#     longestLength = 0
#     for i in range(n):
#         currElement = arr[i]
#         currLength = 1
#         while True:
#             found = False
#             for j in range(n):
#                 if arr[j] == currElement + 1:
#                     found = True
#                     break
#             if found:
#                 currElement += 1
#                 currLength += 1
#             else:
#                 break
#         longestLength = max(longestLength, currLength)
#     return longestLength


# A = [1, 3, 5, 9, 11]
# print(LCS(A))  # Output: 1
# # # Test case 1
# A = [2, 0, 6, 1, 5, 3, 7]
# print(LCS(A))
# # Test case 2
# A = [2, 4, 6, 3, 7, 4, 8, 1]
# print(LCS(A))
# # Test case 3
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(LCS(A))
# # Test case 4
# A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(LCS(A))


# A = [5070, 3683, 3296, 6849, 7073, 1612, 4346, 3017, 1354, 5664, 8752, 5331, 9955, 334, 4120, 4369, 6876, 2383, 6233, 7948, 4754, 6609, 5356, 6320, 1258, 2475, 348, 8181, 5686, 4850, 3180, 7487, 802, 3977, 9240, 9710, 3190, 4487, 2496, 3667, 6865, 8796, 1126, 8072, 6108, 3079, 6710, 5223, 3686, 9766, 1334, 5986, 2857, 142, 3874, 572, 2797, 6395, 6676, 7061, 4345, 4966, 1242, 8497, 1931, 4504, 7794, 6021, 6585, 5531, 1521, 2538, 231, 8613, 9756, 2050, 2789, 7842, 614, 5943, 2567, 9428, 7721, 459, 3007, 7280, 1218, 5811, 3958, 3703, 5535, 4024, 1294, 9455, 9569, 5799, 9978, 9391, 1432, 7638, 3258, 4135, 3456, 7599, 1310, 7779, 8702, 7271, 8064, 2183, 5310, 2575, 3741, 1798, 4313, 2601, 467, 7338, 5210, 9776, 4223, 2685, 1635, 1571, 1441, 1456, 4769, 4548, 1553, 8452, 3886, 5022, 9638, 1655, 2271, 4471, 7549, 6908, 5879, 7463, 5502, 7553, 1001, 2105, 110, 5741, 6193, 9337, 6402, 4529, 9884, 3269, 1267, 4983, 5037, 9967, 9079, 4337, 1777, 7523, 613, 6437, 6917, 3401, 3625, 4262, 1287, 9921, 2753, 352, 2923, 2509, 486, 3342, 4569, 6128, 8138, 5122, 696, 8117, 2734, 2489, 7999, 1853, 7872, 5541, 3197, 3587, 5465, 7161, 5156, 1498, 3182, 3657, 2645, 8252, 3779, 6709, 7136, 9590, 5381, 5424, 9027, 1385, 4339, 5926, 7601, 3483, 9382, 642, 4624, 5311, 7594, 597, 3122, 9199, 4811, 8368, 6137, 6304, 2950, 8121, 2901, 3754, 5970, 2160, 9053, 18, 5055, 1892, 9224, 6511, 9404, 8568, 555, 9670, 6505, 6974, 8430, 6520, 216, 7864, 3355, 5658, 1347, 5195, 7353, 9832, 3039, 2107, 4341, 5862, 2643, 9244, 5161, 6887, 36, 1990, 6303, 8545, 35, 1289, 8822, 6112, 7666, 8844, 29, 7985, 3402, 2730, 776, 4687, 3649, 6672, 2543, 5171, 3791, 7911, 7322, 5209, 6394, 6483, 94, 8451, 788, 5751, 7402, 3061, 267, 8495, 2961, 6697, 6437, 2743, 9416, 6644, 845, 616, 8210, 3939, 2715, 6776, 7879, 3621, 6348, 3254, 9167, 6184, 961, 4914, 1280, 5165, 634, 429, 6564, 2173, 9729, 8012, 7359, 9979, 8528, 3975, 9061, 9460, 7539, 6325, 1432, 7306, 9305, 1040, 6939, 5345, 3194, 8702, 6991, 1939, 3634, 6625, 10, 8876, 1265, 2838, 9064, 2782, 9036, 452, 2151, 6181, 4294, 6051, 5303, 5071, 8774, 2866, 5626, 3924, 961, 1021, 8153, 2304, 591, 1246, 3194, 4983, 1588, 5720, 4167, 5513, 153, 912, 1179, 2667, 4366, 3516, 3869, 5393, 449, 850, 2227, 181, 2180, 9071, 9807, 9923, 4183, 5906, 6850, 6463, 2262, 534, 5410, 8643, 3205, 5985, 3691, 2817, 5869, 4688, 4541, 5214, 6036, 6838, 2841, 5350, 1647, 1354, 1082, 7346, 231, 285, 2412, 7666, 5763, 6500, 5029, 4345, 7744, 5348, 203, 2472, 4185, 5520, 1344, 7431, 9372, 5305, 9115, 1281, 9998, 4996, 6774, 1399, 1506, 5909, 6655, 2449, 1025, 1616, 3505, 2081, 2783, 2542, 2562, 1215, 659, 132, 995, 9829, 5839, 8555, 6378, 9998, 5199, 3385, 9652, 8748, 1269, 6440, 2794, 6441, 5121, 1704, 1827, 7093, 3082, 9851, 4440, 6578, 6037, 5024, 7055, 7522, 6017, 8107, 3507, 7729, 3515, 9258, 4008, 5766, 6409, 2290, 6358, 9109, 9920, 1151, 8151, 8978, 4069, 7929, 446, 8576, 485, 6817, 1418, 6187, 2907, 9361, 5842, 8180, 4503, 401, 9526, 6089, 8785, 3166, 8838, 9718, 9519, 9188, 1520, 7680, 6754, 5009, 8138, 5098, 3245, 5437, 9133, 385, 5097, 7038, 1501, 6686, 2552, 5309, 8873, 643, 6082, 4381, 1061, 4850, 6520, 2126, 634, 1016, 6993, 9748, 9304, 3983, 9403, 9371, 6478, 2155, 8507, 2071, 1928, 2788, 3379, 7447, 8397, 4626, 9806, 5474, 8357, 7874, 252, 2187, 3684, 1631, 6017, 2110, 2178, 3106, 5831, 3321, 1058, 7363, 3873, 7186, 2782, 9765, 3543, 3767, 4177, 3524, 3680, 3949, 2342, 8090, 9564, 7350, 4894, 272, 5984, 1878, 4561, 3507, 8488, 9009, 2440, 7184, 8541, 9010, 6560, 8781, 611, 9259, 6307, 417, 3373, 8524, 7782, 4778, 0, 5436, 3070, 9941, 7359, 8539, 336, 9403, 4528, 3522, 2547, 5885, 7258, 3284, 1431, 1441, 5690, 1567, 4050, 1298, 7446, 6000, 556, 8165, 8934, 3838, 5766, 7409, 1202, 6913, 2347, 780, 5394, 1817, 6147, 713, 5778, 402, 1205, 2880, 3750, 9211, 5342, 4778, 167, 4263, 27, 2845, 119, 8098, 2227, 4725, 8212, 5628, 9014, 7725, 1209, 7917, 5582, 8902, 4622, 3486, 931, 8470, 3580, 4378, 3214, 7335, 5329, 8635, 279, 1669, 4577, 5508, 7556, 5894, 9136, 9140, 8854, 8672, 3711, 4271, 8816, 7885, 6489, 284, 3253, 7954, 9349, 3083, 4024, 9268, 8581, 3143, 6893, 4237, 8605, 2245, 5806, 2691, 6580, 715, 3859, 4898, 7434, 7346, 9721, 9136, 9114, 6838, 1332, 7596, 9917, 5190, 3557, 8202, 3917, 4115, 4310, 9500, 6290, 7888, 1599, 8670, 6834, 4930, 6149, 2498, 4012, 7136, 2, 4164, 4850, 2991, 5013, 8710, 5920, 3263, 4861, 7663, 2303, 7626, 8315, 3237, 4244, 1301, 4573, 3863, 3999, 5609, 5760, 2740, 6623, 2255, 7225, 7689, 3214, 9358, 3484, 1270, 8276, 2494, 4649, 5682, 3601, 2113, 9309, 831, 2458, 7571, 4767, 4485, 3325, 8368, 2897, 7101, 8085, 1239, 7011, 6137, 3318, 9641, 9406, 4453, 7851, 4263, 319, 8107, 1803, 3691, 6802, 2858, 7218, 8501, 8253, 9620, 9455, 6533, 9357, 8317, 78, 513, 4183, 8896, 6896, 6214, 896, 6375, 1814, 4438, 8418, 7929, 9771, 1264, 7736, 7336, 4899, 7948, 2835, 4594, 859, 6203, 6768, 7525, 1437, 2497, 7704, 1513, 2620, 2794, 8403, 5940, 6927, 9802, 8318, 4100, 615, 4456, 2738, 3070, 1864, 4239, 1673, 3458, 9996, 302, 4745, 5099, 3901, 1142, 7402, 4024, 2401, 8019, 9812, 3996, 8705, 5743, 5518, 7202, 6679, 8574, 4255, 1523, 5074, 7737, 5663, 3810, 5099, 7808, 8336, 9378, 9732, 7082, 8944, 3728, 7333, 2357, 7394, 9044, 1753, 6144, 9039, 1193]
#
# print(longestConsecutiveSequence(A))
# end_time = time.perf_counter()
#
# elapsed_time = end_time - start_time
#
# print(f"Elapsed time: {elapsed_time:.4f} seconds")


# def q1_bruteForce(input_array):
#     n = len(input_array)
#     ordered_array = [0] * n
#     for i in range(n):
#         order = 1
#         for j in range(n):
#             if input_array[j] > input_array[i]:
#                 order += 1
#         ordered_array[i] = order
#     return ordered_array

# def q1_efficient(input_array):
#     # n = len(input_array)
#     n = len(input_array)
#     # ordered_array has the same length as input_array and is initialized with 0
#     ordered_array = [0] * n
#     # sorted_array is a clone of input_array sorted in descending order
#     sorted_array = sorted(input_array, reverse=True)
#     # d is a dictionary that maps each element of sorted_array to its order
#     d = {}
#     # for each element of sorted_array, we add it to the dictionary d
#     for i in range(n):
#         if sorted_array[i] not in d:
#             d[sorted_array[i]] = i + 1
#     # for each element of input_array, we find its order in the dictionary d
#     for i in range(n):
#         ordered_array[i] = d[input_array[i]]
#     # we return the ordered_array
#     return ordered_array

# def q3_brute_force(input_array):
#     max_len = 0
#     for num in input_array:
#         curr_num = num
#         curr_len = 1
#         while curr_num + 1 in input_array:
#             curr_num += 1
#             curr_len += 1
#         max_len = max(max_len, curr_len)
#     return max_len


# def q3_efficient(nums):
#     # we convert the list to a set
#     nums = set(nums)
#     # we initialize the maximum length of the sequence
#     max_len = 0
#     # for each number in the set
#     for num in nums:
#         # if the number is the first of a sequence
#         if num - 1 not in nums:
#             # we initialize the current number and the current length of the sequence
#             curr_num = num
#             curr_len = 1
#             # while the next number in the sequence is in the set
#             while curr_num + 1 in nums:
#                 # we update the current number and the current length of the sequence
#                 curr_num += 1
#                 curr_len += 1
#             # we update the maximum length of the sequence
#             max_len = max(max_len, curr_len)
#     # we return the maximum length of the sequence
#     return max_len

#
# def find_triplet(arr):
#     n = len(arr)
#     max_k = [0] * n  # Create an auxiliary array to store the index of the largest element to the right of each element
#     max_k[n - 1] = n - 1  # Initialize the last element of max_k as n-1
#     # Iterate through the elements of arr from right to left
#     for i in range(n - 2, -1, -1):
#         # If the current element is larger than the largest element to its right, set its index as the largest
#         if arr[i] > arr[max_k[i + 1]]:
#             max_k[i] = i
#         else:  # Otherwise, the index of the largest element to the right remains the same
#             max_k[i] = max_k[i + 1]
#     # Iterate through the elements of arr from left to right, up to the second-to-last element
#     for i in range(n - 2):
#         # Check if the current element is larger than the largest element to its right
#         if arr[i] > arr[max_k[i + 1]]:
#             # Iterate through the elements of arr to the right of the current element
#             for j in range(i + 1, n - 1):
#                 # Check if the current element and the current element to its right are larger than the largest
#                 # element to the right of the second element
#                 if arr[max_k[j + 1]] < arr[j] < arr[i]:
#                     return [arr[i], arr[j], arr[max_k[j + 1]]]
#     # If no triplet is found, return an empty list
#     return []
#
#
# A = [9, 1, 6, 7, 3, 4, 5]
# print(find_triplet(A))
#


# def Q1_brute_force(arr):
#     res = []
#     for i in range(len(arr)):
#         count = 1
#         for j in range(len(arr)):
#             if arr[j] > arr[i]:
#                 count += 1
#         res.append(count)
#     return res
#
# a = [10,12,17,14,8,3,22]
# print(Q1_brute_force(a))

"""
Algorithm: Q_1brute_force(arr)

1. Initialize an empty list res
2. For each element of arr
    2.1. Initialize a counter count to 1
    2.2. For each element of arr
        2.2.1. If the current element is larger than the element of arr
        add 1 to count
    2.3. Append count to res
3. Return res

steps:
1.res = new empty array
2.for i from 0 to n-1:
    2.1count = 1
    2.2for j from to n-1:
       2.2.1 if arr[j] > arr[i]:
            2.2.1.1count += 1
    2.3 res.append(count)
3. return res

analysis:
time complexity: O(n^2) because we have two nested loops that iterate over the array
space complexity: O(n) because we create a new array of size n
"""

"""
Q_1_efficient(arr)
1. Initialize an empty list pairs_list
2. For each element of arr
    2.1. Append a tuple (element, index) to pairs_list
3. Sort pairs_list in descending order by the first element of each tuple
4. For each element of pairs_list
    4.1. Set element to the first element of the tuple
    4.2. Set index to the second element of the tuple
    4.3. Set arr[index] to i + 1
5. Return arr

steps:
1. pairs_list = new empty array
2. for i from 0 to n-1:
    2.1 pairs_list.append((arr[i], i))
3. sorted_pairs = sort pairs_list in descending order by the first element of each tuple
4. for i from 0 to n-1:
    4.1 element, index = sorted_pairs[i]
    4.2 arr[index] = i + 1
5. return arr

analysis:
time complexity: O(nlogn) because we sort the array in descending order and then iterate over it
space complexity: O(n) because we create a new array of size n
"""

#

"""
Algorithm: Q_2brute_force(arr)
1. Initialize a counter count to 0
2. For each element of arr
    2.1. For each element of arr
        2.1.1. For each element of arr
            if arr[i] > arr[j] > arr[k]:
               return arr[i], arr[j], arr[k]
3. If no triplet is found, return an empty list

steps:
n = length(arr)  
for i from 0 to n-1:
    for j from i+1 to n-1:
        for k from j+1 to n-1:
            if arr[i] > arr[j] > arr[k]:
               return arr[i], arr[j], arr[k]
return []

analysis:
time complexity: O(n^3) because we have three nested loops that iterate over the array
space complexity: O(n) because we create a new array of size n
"""
#
# def Q_2_brute_force(arr):
#     n = len(arr)
#     for i in range(n-2):
#         for j in range(i+1, n-1):
#             for k in range(j+1, n):
#                 if arr[i] > arr[j] > arr[k]:
#                     return arr[i], arr[j], arr[k]
#     return []
#
# a = [9, 1, 6, 7, 3, 4, 5]
# print(Q_2_brute_force(a))

"""
Algorithm: Q_2efficient(arr)
1. Initialize an empty list triplet_list
2. n is the length of arr
3. i, j, k are indices of arr
4. While i, j, k are valid indices
    4.1. If arr[i] > arr[j] > arr[k] append [arr[i], arr[j], arr[k]] to triplet_list
    4.2. If k is the last index of arr
        4.2.1. Increment j by 1
        4.2.2. Set k to j + 1
    4.3. Else
        4.3.1. Increment k by 1
    4.4. If j is the last index of arr
        4.4.1. Increment i by 1
        4.4.2. Set j to i + 1
        4.4.3. Set k to j + 1
5. Return triplet_list

steps:
1. triplet_list = new empty array
2. n = length(arr)
3. i = 0, j = 1, k = 2
4. while i < j < k < n:
    4.1 if arr[i] > arr[j] > arr[k]:
        triplet_list.append([arr[i], arr[j], arr[k]])
    4.2 if k == n - 1:
        j += 1
        k = j + 1
    4.3 else:
        k += 1
    4.4 if j == n - 1:
        i += 1
        j = i + 1
        k = j + 1
5. return triplet_list

analysis:
time complexity: O(n) because we iterate over the array once and do constant time operations
space complexity: O(n) because we create a new array of size n

"""

# def Q2_efficient(arr):
#     # Initialize an empty list triplet_list
#     triplet_list = []
#     # n is the length of arr
#     n = len(arr)
#     # i, j, k are indices of arr
#     i = 0
#     j = 1
#     k = 2
#     # While i, j, k are valid indices
#     while i < j < k < n:
#         # If arr[i] > arr[j] > arr[k] append [arr[i], arr[j], arr[k]] to triplet_list
#         if arr[i] > arr[j] > arr[k]:
#             triplet_list.append([arr[i], arr[j], arr[k]])
#
#         if k == n - 1:
#             j += 1
#             k = j + 1
#         else:
#             k += 1
#         if j == n - 1:
#             i += 1
#             j = i + 1
#             k = j + 1
#     # Return the first triplet in triplet_list if triplet_list is not empty, otherwise return an empty list
#     return triplet_list[0] if triplet_list else []
#
#
# a = [9, 1, 6, 7, 3, 4, 5]
# print(Q2_efficient(a))


"""
Algorithm: Q_3_brute_force(arr)
1. Initialize a counter count to 0
2. For each element of arr
    2.1. current number =  num
    2.2. current length = 1
    2.3. While current number + 1 is in arr
        2.3.1. current number += 1
        2.3.2. current length += 1
    2.4. count = max(count, current length)
3. Return count

steps:
1. max_length = 0
2. for num in arr:
    2.1 curr_num = num
    2.2 curr_len = 1
    2.3 while curr_num + 1 in arr:
        curr_num += 1
        curr_len += 1
    2.4 max_length = max(max_length, curr_len)
3. return max_length

analysis:
time complexity: O(n^2) because we have a nested loop that iterates over the array
space complexity: O(n)

"""

# def Q_3brute_force(arr):
#     max_length = 0
#     for num in arr:
#         curr_num = num
#         curr_len = 1
#         while curr_num + 1 in arr:
#             curr_num += 1
#             curr_len += 1
#         max_length = max(max_length, curr_len)
#     return max_length
#
#
# a = [100, 4, 200, 1, 3, 2]
# print(longestConsecutive(a))


"""
Algorithm: Q_3_efficient(arr)
1. Initialize a hash set hash_set
2. For each element of arr
    2.1. Add the element to hash_set
3. Initialize a counter max_length to 0
4. For each element of arr
    4.1. If element - 1 is not in hash_set
    4.1.1. current number =  num
    4.1.2. current length = 1
    4.1.3. While current number + 1 is in hash_set
        curr_num += 1
        curr_len += 1
    4.1.4. max_length = max(max_length, current length)
5. Return max_length

steps:
1. hash_set = new empty set
2. for num in arr:
    2.1 hash_set.add(num)
3. max_length = 0
4. for num in arr:
    4.1 if num - 1 not in hash_set:
        curr_num = num
        curr_len = 1
        while curr_num + 1 in hash_set:
            curr_num += 1
            curr_len += 1
        max_length = max(max_length, curr_len)
5. return max_length

analysis:
time complexity: O(n) because we iterate over the array once and do constant time operations
space complexity: O(n) because we create a new set of size n

"""


# def Q_3Efficient(arr):
#     hash_set = set(arr)
#     max_length = 0
#     for num in arr:
#         if num - 1 not in hash_set:
#             curr_num = num
#             curr_len = 1
#             while curr_num + 1 in hash_set:
#                 curr_num += 1
#                 curr_len += 1
#             max_length = max(max_length, curr_len)
#     return max_length
#
#
# a = [100, 4, 200, 1, 3, 2]
# print(Q_3Efficient(a))

#

def is_ascending(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


# def find_descending_sorted_triplet_efficient(A):
#     A.sort(reverse=True)
#
#     i = 0
#     j = 1
#     while i < len(A) - 1 and A[i] == A[i + 1]:
#         i += 1
#     while j < len(A) - 1 and A[j] == A[j + 1]:
#         j += 1
#
#     if i >= len(A) - 1 or j >= len(A) - 1:
#         return None
#     elif len(A) == 3:
#         return A[i], A[j], A[j + 1]
#     else:
#         return A[i], A[j], A[j + 2]
#
#
# A = [9, 1, 6, 7, 3, 4, 5]
# if is_ascending(A):
#     print("None")
# else:
#     print(find_descending_sorted_triplet_efficient(A))
#
def min_time_to_acquire_skills(books):
    skill_counts = [0, 0]
    for book in books:
        for i in range(2):
            if book[1][i] == '1':
                skill_counts[i] += 1

    for book in books:
        if book[1] == '11':
            return book[0]

    for i in range(2):
        if skill_counts[i] == 0:
            return -1
    min_time = float('inf')
    for j in range(len(books)):
        if books[j][1][0] == '1':
            for k in range(len(books)):
                if k != j and books[k][1][1] == '1':
                    min_time = min(min_time, books[j][0] + books[k][0])
    if min_time == float('inf'):
        return -1
    return min_time


for _ in range(int(input())):
    n = int(input())
    s1 = s2 = s12 = float("inf")

    for _ in range(n):
        m, s = input().split()
        if s == "10":
            s1 = min(s1, int(m))
        elif s == "01":
            s2 = min(s2, int(m))
        elif s == "11":
            s12 = min(s12, int(m))
        else:
            continue

    if s12 < s1 + s2:
        print(s12)
    else:
        print(s1 + s2) if s1 != float("inf") and s2 != float("inf") else print(-1)
