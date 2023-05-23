# Prolog Program
Don't use any built-in predicates
* Task 1:
Implement "is_friend" which makes the "friend" relation a symmetric relation (i.e., if X is friends with Y then Y is friends with X).
Examples:
?- is_friend(ahmed, samy).
true.
?- is_friend(samy, ahmed).
true.
Note: In the knowledge base, we have only one relation for Ahmed and Samy.
* Task 2:
Get the list of all friends of a given person.
Examples:
?- friendList(ahmed, L).
L = [samy, fouad].
?- friendList(huda, L).
L = [mariam, aisha, lamia].
* Task 3:
Get the number of friends of a given person. (For the "count" rule, use tail recursion)
Examples:
?- friendListCount(ahmed, N).
N = 2.
?- friendListCount(huda, N).
N = 3.
* Task 4:
Suggest possible friends to a person if they have at least one friend in common (at least one mutual friend). Make sure that the suggested friend is not already a friend of
the person.
Examples:
?- peopleYouMayKnow(ahmed, X).
X = mohammed;
X = said;
…
?- peopleYouMayKnow(huda, X).
X = hagar;
X = zainab;
X = hend;
X = zainab;
…
*Task 5:
Suggest one possible friend to a person if they have at least N mutual friends. Make sure that the suggested friend is not already a friend of the person.
Examples:
?- peopleYouMayKnow(ahmed, 2, X).
X = abdullah.
Explanation: Ahmed is friends with Fouad and Samy and both have Abdullah as a friend,
so we can suggest Abdullah to Ahmed.
?- peopleYouMayKnow(huda, 3, X).
X = zainab.
Explanation: Huda is friends with mariam, lamia and aisha and all of
them have Zainab as a friend, so we can suggest Zainab to Huda.
* Task 6:
Get a list of all unique possible friends to a person if they have at least one mutual friend. Make sure that the suggested friends are not already friends of the person.
Examples:
?- peopleYouMayKnowList(ahmed, L).
L = [mohammed, said, omar, abdullah].
?- peopleYouMayKnowList(huda, L).
L = [hagar, zainab, hend].
* Bonus Task:
Suggest possible friends to a person if there is no direct mutual friend between them but there is a simple indirect relation (e.g., X is a friend of Y and Y is a friend of Z and Z is a friend of W, so we can suggest W to X even if there are no direct mutual friends between X and W). Make sure that the suggested friend(s) is(are) not already a friend of the person.
Examples:
?- peopleYouMayKnow_indirect(ahmed, X).
X = khaled;
X = ibrahim;
X = khaled;
…
?- peopleYouMayKnow_indirect(huda, X).
X = rokaya;
X = eman;
…