% --- FACTS ---
male(john).
male(peter).
male(mike).
female(mary).
female(susan).
female(anna).

% parent(Parent, Child)
parent(john, peter).
parent(john, susan).
parent(mary, peter).
parent(mary, susan).
parent(peter, mike).
parent(susan, anna).

% --- RULES ---
% Grandparent rule
grandparent(GP, GC) :- parent(GP, Parent), parent(Parent, GC).

% Sibling rule (They share a parent, and X is not Y)
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.

% Uncle rule (Uncle is male, is a sibling of a parent)
uncle(Uncle, NieceNephew) :- male(Uncle), sibling(Uncle, P), parent(P, NieceNephew).

% Cousin rule (Their parents are siblings)
cousin(C1, C2) :- parent(P1, C1), parent(P2, C2), sibling(P1, P2).
