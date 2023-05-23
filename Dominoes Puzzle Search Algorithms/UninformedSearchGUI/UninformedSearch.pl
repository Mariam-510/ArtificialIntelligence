go([M,N],[P1,P2],[P3,P4],Output):-
    S is M*N,
    createList([],L1,S),
    I1 is ((P1-1)*N+P2)-1,
    replace(L1,I1,b,L2),
    I2 is ((P3-1)*N+P4)-1,
    replace(L2,I2,b,L3),
    search([[L3,null]],[],[],M,N,Output).

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
search([],[H|RestClosed],_,M,N,Output):-
    % Search print in Gui
     createResult(RestClosed,[],Output),!.
    % Search print in Prolog
    %printSolution(RestClosed,M,N),!.

search(Open, Closed,L,M,N,Output):-
    getState(Open, [CurrentState,Parent], TmpOpen),
    \+ move(CurrentState,Next,M,N),!,
    append(Closed, [[CurrentState,Parent]], NewClosed),
    append(L, [CurrentState], NewL),
    search(TmpOpen, NewClosed,NewL,M,N,Output).

search(Open, Closed,L,M,N,Output):-
    getState(Open, CurrentNode, TmpOpen),
    getAllValidChildren(CurrentNode,TmpOpen,Closed,Children,M,N),
    addChildren(Children, TmpOpen, NewOpen),
    append(Closed, [CurrentNode], NewClosed),
    search(NewOpen, NewClosed,L,M,N,Output).

% Implementation of getting the next states
getAllValidChildren(Node, Open, Closed, Children,M,N):-
    findall(Next, getNextState(Node, Open, Closed, Next,M,N), Children).

getNextState([State,_], Open, Closed, [Next,State],M,N):-
    move(State, Next,M,N),
    not(member([Next,_], Open)),
    not(member([Next,_], Closed)),
    isOkay(Next).

% Implementation of BFS to getState and addChildren.
getState([CurrentNode|Rest], CurrentNode, Rest).
addChildren(Children, Open, NewOpen):-
    append(Open, Children, NewOpen).

% This problem has no rules
isOkay(_):- true.

% Create Result
createResult([[State,_]|T],L,Out):-
    append(L, [State], NewL),
    createResult(T,NewL,Out).
createResult([],L,L).

% Print solution
printSolution([[State,_]|T],M,N):-
     \+formatedPrint(State,M,N,N),
     nl,write("------------"),nl,
    printSolution(T,M,N).
printSolution([],_,_).

% Format board
formatedPrint(_,0,_,_).
formatedPrint([H|T],M,N,0):-
    M>0,
    NewM is M-1,
    nl,
    formatedPrint([H|T],NewM,N,N).
formatedPrint([H|T],M,N,Temp):-
    M>0,
    Temp>0,
    write(H),
    write(' '),
    NewTemp is Temp-1,
    formatedPrint(T,M,N,NewTemp).

% Moves
move(State,Next,M,N):-
    right(State,Next,M,N,1);
    up(State,Next,M,N,2).

right(State, Next,M,N,C):-
    nth0(EmptyTileIndex, State, 0),
    NextEmptyTileIndex is EmptyTileIndex+1,
     not(0 is NextEmptyTileIndex mod N),
    nth0(NextEmptyTileIndex, State, Num),
    Num == 0,
    replace(State,EmptyTileIndex,C,NewState),
    replace(NewState,NextEmptyTileIndex,C,Next).

up(State, Next,M,N,C):-
    nth0(EmptyTileIndex, State, 0),
    EmptyTileIndex > N-1,
    NextEmptyTileIndex is EmptyTileIndex-N,
    nth0(NextEmptyTileIndex, State, Num),
    Num == 0,
    replace(State,EmptyTileIndex,C,NewState),
    replace(NewState,NextEmptyTileIndex,C,Next).

