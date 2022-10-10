p=bool(int(input('Enter value for P:')))
q=bool(int(input('Enter value for Q:')))
r=bool(int(input('Enter value for R:')))
lhs_or=p or q or r
rhs_or=q or r or p
print('LHS_OR :',lhs_or)
print('RHS_OR :',rhs_or)
lhs_and=p and q and r
rhs_and=q and r and p
print('LHS_AND :',lhs_and)
print('RHS_AND :',rhs_and)
if lhs_or==rhs_or and lhs_and==rhs_and:
    print('P or Q or R = Q or R or P')
    print('P and Q and R = Q and R and P')
    print('Associative law is verified')
