go([M,N],[P1,P2],[P3,P4],Output):-
    S is M*N,
    createList([],L1,S),
    I1 is ((P1-1)*N+P2)-1,
    replace(L1,I1,b,L2),
    I2 is ((P3-1)*N+P4)-1,
    replace(L2,I2,b,L3),
    search([[L3,null,0,x,0]],[],[],M,N,Output),!.

% Create list size M*N with initial state zeros
createList(L,L,0).
createList(L,L1,S):-
    S>0,
    append(L,[0],NewL),
    S1 is S-1,
    createList(NewL,L1,S1).

% Replace position of bombs with letter b
replace([_|T], 0, E, [E|T]):-!.
replace([H|T], I, E, [H|R]):-
    I > -1,
    NEWI is I-1,
    replace(T, NEWI, E, R), !.
replace(L, _, _, L).

% Search
search([],_,L,M,N,Output):-
    minZeros(L,M*N,Zeros),
    MxDominoes is ((M*N)-(Zeros+2))/2,
    getMxList(L,Zeros,[],List),
    % Search print in Gui
    append(List,[MxDominoes],Output),!.
    % Search print in Prolog
    /*write(MxDominoes),
    write(' is maximum number of dominoes that can be placed.'),nl
    ,printSolution(List,N),!.*/

search(Open, Closed,L,M,N,Output):-
    getBestState(Open, [CurrentState,Parent,G,H,F], TmpOpen),
    \+ move(CurrentState,_,M,N,1),!,
    append(Closed, [[CurrentState,Parent,G,H,F]], NewClosed),
    append(L, [CurrentState], NewL),
    search(TmpOpen, NewClosed,NewL,M,N,Output).

search(Open, Closed, L, M, N,Output):-
    getBestState(Open, CurrentNode, TmpOpen),
    getAllValidChildren(CurrentNode,TmpOpen,Closed,Children,M,N),
    addChildren(Children, TmpOpen, NewOpen),
    append(Closed, [CurrentNode], NewClosed),
    search(NewOpen, NewClosed, L,M,N,Output).

% Implementation of getting the next states
getAllValidChildren(Node, Open, Closed, Children,M,N):-
    findall(Next, getNextState(Node, Open, Closed, Next,M,N), Children).

% Implementation of addChildren
addChildren(Children, Open, NewOpen):-
    append(Open, Children, NewOpen).

% Implementation of getBestState
getBestState(Open, BestChild, Rest):-
    findMin(Open, BestChild),
    delete(Open, BestChild, Rest).

% Implementation of A* finMin
findMin([X], X):- !.
findMin([Head|T], Min):-
    findMin(T, TmpMin),
    Head = [_,_,_,_,HeadF],
    TmpMin = [_,_,_,_,TmpF],
    (TmpF < HeadF -> Min = TmpMin ; Min = Head).

% Implementation of A* getNextState
getNextState([State,_,G,_,_],Open,Closed,[Next,State,NewG,NewH,NewF],M,N):-
    move(State, Next,M,N,MoveCost),
    isOkay(Next),
    calculateH(Next, NewH),
    NewG is G + MoveCost,
    NewF is NewG + NewH,
    ( not(member([Next,_,_,_,_], Open)) ; memberButBetter(Next,Open,NewF) ),
    ( not(member([Next,_,_,_,_],Closed));memberButBetter(Next,Closed,NewF)).

memberButBetter(Next, List, NewF):-
    findall(F, member([Next,_,_,_,F], List), Numbers),
    min_list(Numbers, MinOldF),
    MinOldF > NewF.

% Heuristic function
calculateH([],0):-!.
calculateH([X|T],N) :- X \= 0,!, calculateH(T,N).
calculateH([0|T],N) :- calculateH(T,N1), N is N1 + 1.

% Minimum zeros (Maximum number of dominoes)
minZeros([],Mx,Mx):-!.
minZeros([H|T],Mx,Tmp):-
    calculateH(H, NewH),
    ( NewH<Mx -> minZeros(T,NewH,Tmp) ; minZeros(T,Mx,Tmp) ).

% Create list with max number of dominoes
getMxList([],_,L,L):-!.
getMxList([H|T],Zeros,L,List):-
   calculateH(H, NewH),
   (NewH==Zeros ->(append(L,[H],NL),getMxList(T,Zeros,NL,List)); getMxList(T,Zeros,L,List)).

% Print board
printSolution([],_):-!.
printSolution([H|T],N):-
     formatedPrint(H,N,N),nl,write('***********'),nl,
     printSolution(T,N).

% Format board
formatedPrint([],_,_):-!.
formatedPrint([H|T],N,Tmp):-
    ( N>0 -> (NewN is N-1,write(H));(NewN is Tmp-1 , nl,write(H)) ),
     write(' '),formatedPrint(T,NewN,Tmp).


isOkay(_):- true. % This problem has no rules

% Moves
move(State,Next,M,N,1):-
    right(State,Next,M,N,1);
    up(State,Next,M,N,2).

right(State, Next,_,N,C):-
    nth0(EmptyTileIndex, State, 0),
    NextEmptyTileIndex is EmptyTileIndex+1,
    not(0 is NextEmptyTileIndex mod N),
    nth0(NextEmptyTileIndex, State, Num),
    Num == 0,
    replace(State,EmptyTileIndex,C,NewState),
    replace(NewState,NextEmptyTileIndex,C,Next).

up(State, Next,_,N,C):-
    nth0(EmptyTileIndex, State, 0),
    EmptyTileIndex > N-1,
    NextEmptyTileIndex is EmptyTileIndex-N,
    nth0(NextEmptyTileIndex, State, Num),
    Num == 0,
    replace(State,EmptyTileIndex,C,NewState),
    replace(NewState,NextEmptyTileIndex,C,Next).
