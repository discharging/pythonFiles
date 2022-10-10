/* Facts */

male(jack).
male(sam).
male(ali).
male(james).
male(simon).
male(harry).
male(john).

female(helen).
female(olive).
female(jess).
female(lily).
female(jennie).
female(rose).

parent_of(jack,jess).
parent_of(jack,lily).
parent_of(helen, jess).
parent_of(helen, lily).
parent_of(olive,james).
parent_of(sam, james).
parent_of(jess, simon).
parent_of(ali, simon).
parent_of(lily, harry).
parent_of(james, harry).
parent_of(lily, john).
parent_of(james, john).
parent_of(jennie, rose).
parent_of(harry, rose).

father_of(X,Y):- male(X),parent_of(X,Y).
mother_of(X,Y):- female(X),parent_of(X,Y).

grandfather_of(X,Y):- male(X),parent_of(X,Z),parent_of(Z,Y).
grandmother_of(X,Y):- female(X),parent_of(X,Z),parent_of(Z,Y).

sister_of(X,Y):- female(X),parent_of(P, Y), parent_of(P,X),X \= Y.
brother_of(X,Y):- male(X),parent_of(P, Y), parent_of(P,X),X \= Y.

uncle_of(X,Y):-male(X),parent_of(Z,Y), brother_of(X,Z).
aunt_of(X,Y):-female(X),parent_of(Z,Y), sister_of(X,Z).

sibling(X,Y):-parent_of(P,X),parent_of(P,Y),X\=Y.

nephew(N,X):-male(N),parent_of(P,N),sibling(X,P).
niece(N,X):-female(N),parent_of(P,N),sibling(X,P).

cousin(C,X):-parent_of(P,C),uncle_of(P,X).
cousin(C,X):-parent_of(P,C),aunt_of(P,X).
