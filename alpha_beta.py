def alpha_beta(branch, depth, alpha, beta):
    for child in branch:
        if type(child) is list:
            (nalpha, nbeta) = alpha_beta(child, depth +1, alpha, beta)
            #print(nalpha,nbeta)
            if depth % 2 == 1:
                beta = nalpha if nalpha < beta else beta
            else:
                alpha = nbeta if nbeta > alpha else alpha
        else:
            if depth % 2 == 0 and alpha < child:
                alpha = child
            if depth % 2 == 1 and beta > child:
                beta = child
    return (alpha, beta)
tree = [[[1,5,2], [8,-8,-9]], [[9,4,5], [-3,4,3]]]
root = 0
(alpha, beta) = alpha_beta(tree, root, -100, 100) 
print ("(alpha, beta): ", alpha, beta)
print ("Result: ", alpha)
