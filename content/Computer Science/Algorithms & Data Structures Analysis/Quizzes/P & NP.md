> [!exercise]+ Exercise 1
> There is an algorithm that decides whether a given C++ problem returns 100.
>
> - True
> - **False**
>
> **Answer:**
> False, this is an undecidable problem (Halting Problem).

> [!exercise]+ Exercise 2
> If L is a problem in NP then any NP-complete problem is polynomial-time reducible to L.
>
> - True
> - **False**
>
> **Answer:**
> Not necessarily. If L was NP hard, then it would be true. 

> [!exercise]+ Exercise 3
> Assuming P ≠ NP, the decision variant of the traveling salesperson problem is in P.
>
> - True
> - **False**
>
> **Answer:**
> If it's NP, then it can't be solved in Polynomial time. 

> [!exercise]+ Exercise 4
> Select all correct statements.
>
> - NP ⊆ P: This means that every problem in NP is also in P, i.e., every problem that can be verified in polynomial time can also be solved in polynomial time.
> - **P ⊆ NP: This means that every problem in P is also in NP, i.e., every problem that can be solved in polynomial time can also be verified in polynomial time.**
> - NP ⊂ P: This means that every problem in NP is also in P, but there exists at least one problem in P that is not in NP.
>
> **Answer:**
> Second option. If a problem can be solved in P, then that solution can simply be verified by finding the solution again (in P time)
> 
> The first option indicates P = NP (which hasn't been proven). The second option implies at least 1 P in NP, which is not true. If it's P, then it CANNOT be in NP. This is possible the other way round though (but only theoretically)



> [!exercise]+ Exercise 5
> Let G=(V,E) be an undirected graph. Select all correct statements.
>
> - **The problem to decide whether G contains a clique of k nodes is in NP.**
> - The problem to decide whether G contains a Hamiltonian Cycle is in P (assuming P ≠ NP).
> - **The problem to compute a clique with a maximal number of nodes is in NP (assuming P ≠ NP).**
> - The problem to compute a clique with a maximal number of nodes is in P (assuming P ≠ NP).
>
> **Answer:**

> [!exercise]+ Exercise 6
> In the context of computational complexity theory and the ongoing P vs NP problem, what does NP stand for?
>
> - Non Polynomial
> - **Nondeterministic Polynomial**
> - Non Practical
> - Not Possible
>
> **Answer:**

> [!exercise]+ Exercise 7
> Which result would provide a definitive answer to the P vs NP problem?
>
> - Proving that P ≠ NP
> - Proving that P = NP
> - **Proving either A or B**
> - None of these options, as it is an unsolvable problem.
>
> **Answer:**
> Proving A would disprove B. Proving B would disprove A. Proving either of them provide a definitive answer to the problem.

> [!exercise]+ Exercise 8
> If a polynomial-time algorithm exists for an NP-complete problem, what consequence does it have for all problems in NP?
>
> - They all become NP-hard.
> - **They all become solvable in polynomial time.**
> - They become trivial to solve in exponential time.
> - They remain in NP.
>
> **Answer:**
> If an NP problem can be solved in P time, then ALL NP problems can be reduced to it.

> [!exercise]+ Exercise 9
> In a reduction from problem A to problem B, if problem A can be reduced to problem B in polynomial time, what can be concluded about the complexity of problem B?
>
> - Problem B is in P.
> - Problem B is harder than problem A.
> - Problem B is NP-complete.
> - Problem B is at least as hard as problem A.
>
> **Answer:**

The options for each question are now included in the exercise callouts. For true/false questions, the options are simply "True" and "False". For multiple-choice questions, the options are listed as bullet points. The space for the answer is provided at the bottom of each callout.