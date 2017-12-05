# Niki.ai-backend-assignment
 The number of possible bit strings without consecutive 0s can be visualized as (n+2)th fibonacci number where
 n is length of bit string
 So (n+2)th fibonacci number is the solution for the given problem
 To find fibonacci number, Matrix power method is used so that it can be obtained in O(log N) time
 In Matrix method where template matrix is used (T = [[1, 1], [1, 0]] ) and
 after power(T,n)
 T[0][0] gives (n+1)th fibonacci number
