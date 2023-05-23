%check is member in list or not
memberList([H|_],H):-!.
memberList([_|T],E):-
    memberList(T,E).

%reverse the list
reverseList(L1,L2) :-
    reverseList(L1,L2,[]).
reverseList([],L2,L2) :- !.
reverseList([H|T],L2,Temp) :-
    reverseList(T,L2,[H|Temp]).

%Task1------------------------------------------------------------------------------
is_friend(P,X):-
    friend(P,X),!.
is_friend(P,X):-
    friend(X,P).

%Task2------------------------------------------------------------------------------
%get the list of all friends of a given person.
friendList(P, L) :-
    friendList(P, [], L1),
    reverseList(L1,L),!.

friendList(P, Temp, L) :-
    friend(P,X),
    \+ memberList(Temp,X), !,
    friendList(P, [X|Temp], L).

friendList(P, Temp, L) :-
    friend(X,P),
    \+ memberList(Temp,X), !,
    friendList(P, [X|Temp], L).

friendList(_, L, L).

%Task3------------------------------------------------------------------------------
%size of list tail recursion
size([],Temp,Temp).
size([_|T],Temp,S):-
    NewTemp is Temp+1,
    size(T,NewTemp,S).

%number of friends of a given person
friendListCount(P, N):-
    friendList(P, L),
    size(L,0,N).

%Task4-------------------------------------------------------------------------------
%suggest possible friends
peopleYouMayKnow(P,X):-
    friend(P,F1),
    friend(F1,X),
    not(friend(P,X)).

peopleYouMayKnow(P,X):-
    friend(P,F1),
    friend(X,F1),
    X \= P,
    not(friend(P,X)).

peopleYouMayKnow(P,X):-
    friend(F1,P),
    friend(F1,X),
    X \= P,
    not(friend(P,X)).

peopleYouMayKnow(P,X):-
    friend(F1,P),
    friend(X,F1),
    X \= P,
    not(friend(P,X)).

%Task5--------------------------------------------------------------------------------
%count element in list
countElement([H|T],C):-
    countElement([H|T],H,C).
countElement([],_,0).
countElement([Value|T],Value,C):-
    countElement(T,Value,NewC),
    C is NewC+1.
countElement([H|T],Value,C):-
    H\=Value,
    countElement(T,Value,C).

%count every element in list
countAllList([H|T],C,N,H):-
    countElement([H|T],C),
    C>=N,!.

countAllList([H|T],C,N,X):-
  countAllList(T,C,N,X).


%Check is 2 members in list or not
memberTwo([H,S|_],H,S):-!.
memberTwo([H,S|T],F,X):-
    memberTwo(T,F,X).

%return person, friend, suggested friend
suggestFriend(P,F1,X):-
    friend(P,F1),
    friend(F1,X),
    not(friend(P,X)).

suggestFriend(P,F1,X):-
    friend(P,F1),
    friend(X,F1),
    X \= P,
    not(friend(P,X)).

suggestFriend(P,F1,X):-
    friend(F1,P),
    friend(F1,X),
    X \= P,
    not(friend(P,X)).

suggestFriend(P,F1,X):-
    friend(F1,P),
    friend(X,F1),
    X \= P,
    not(friend(P,X)).

%make list of all suggested friends
makeList(P, L) :-
    makeList(P,[],[], L),!.

makeList(P,Tp,Temp, L) :-
    suggestFriend(P,F,X),
    \+ memberTwo(Tp,F,X), !,
    makeList(P,[F,X|Tp] ,[X|Temp], L).

makeList(_, _,L, L).

%suggest 1 possible friend to person if they have at least N mutual friends
peopleYouMayKnow(P,N,X) :-
   makeList(P,L1),
   reverseList(L1,L),
   countAllList(L,C,N,X).

%Task6--------------------------------------------------------------------------------
%get the list of all friends of a given person.
peopleYouMayKnowList(P, L) :-
    peopleYouMayKnowList(P, [], L1),
    reverseList(L1,L),!.

peopleYouMayKnowList(P, Temp, L) :-
    peopleYouMayKnow(P,X),
    \+ memberList(Temp,X), !,
    peopleYouMayKnowList(P, [X|Temp], L).

peopleYouMayKnowList(_, L, L).

%Bonus Task---------------------------------------------------------------------------
peopleYouMayKnow_indirect(P, X):-
    peopleYouMayKnow(P,Y),
     friend(Y,X),
     not(friend(P,X)),
     not(peopleYouMayKnow(P,X));
     not(friend(X,P)),
     not(peopleYouMayKnow(P,X)).
