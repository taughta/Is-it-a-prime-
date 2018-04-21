# Is-it-a-prime?

This little simple tool checks if the entered number is a prime number.

First the user enters the number. The program checks if the input is valid.

Then the possible divisors are generated - from to "2" to the number minus one.
For example if the number is 50 then divisors are "2, 3, 4, 5 ... 49".
Although I used generator instead of the good ol' list since the number of divisors
may be really long if someone enters a crazy high number (eg.: 999999999999). This way we don't run out of memory (hopefully).

Then a for loop checks the number against the divisors one by one and determines if it can be divided evenly.

-If it can then all of the divisors are stored in a list and at the end of the loop the user is informed that
it is not a prime number and all of the possible divisors are presented to him/her.

-If it is not possible then the user is informed that this number is a prime number.
