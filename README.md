# Niki.ai-backend-assignment
 The number of possible bit strings without consecutive 0s can be visualized as (n+2)th fibonacci number where<br>
 n is length of bit string<br>
 So (n+2)th fibonacci number is the solution for the given problem<br>
 To find fibonacci number, Matrix power method is used so that it can be obtained in O(log N) time<br>
 In Matrix method where template matrix is used (T = [[1, 1], [1, 0]] ) and<br>
 after power(T,n)<br>
 T[0][0] gives (n+1)th fibonacci number<br>
