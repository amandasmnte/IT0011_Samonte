
A = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'}
B = {'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'}
C = {'c', 'd', 'e', 'f', 'g'}

num_elements_A_B = len(A.union(B))
print(f"Number of elements in set A and B: {num_elements_A_B}")


num_elements_B_not_A_C = len(B - (A.union(C)))
print(f"Number of elements in B that are not part of A and C: {num_elements_B_not_A_C}")

# i. 
result_i = B.intersection({'h', 'i', 'j', 'k'})
print(f"Result i: {result_i}")

# ii. 
result_ii = A.intersection({'c', 'd', 'f'})
print(f"Result ii: {result_ii}")

# iii. 
result_iii = A.intersection({'b', 'c'}).union(B.intersection({'h'}))
print(f"Result iii: {result_iii}")

# iv. 
result_iv = A.intersection({'d', 'f'})
print(f"Result iv: {result_iv}")

# v. 
result_v = A.intersection({'c'})
print(f"Result v: {result_v}")

# vi.
result_vi = B.intersection({'l', 'm', 'o'})
print(f"Result vi: {result_vi}")