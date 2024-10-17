> [!exercise] Question 1
> List two ways a system could use to determine which disk blocks are free. Give advantages of each way.
>
> *Answer:*
> 
> 1. **Bitmap:** Uses a bit array where each bit represents a disk block.  
>    *Advantage:* Efficient in space and allows quick allocation and deallocation.
> 
> 2. **Linked List:** Maintains a linked list of free blocks.  
>    *Advantage:* Simple to implement and easy to traverse for allocation.

---

> [!exercise] Question 2
> What is contiguous allocation? Name one advantage and one disadvantage of contiguous allocation.
>
> *Answer:*
> 
> **Contiguous allocation** assigns consecutive blocks on the disk to a file.
> 
> *Advantage:* Simple and fast access due to sequential storage.
> 
> *Disadvantage:* Prone to external fragmentation and difficult to resize files.

---

> [!exercise] Question 3
> What is the difference between a hard link and a symbolic link? Give an advantage of each one. How does a symbolic link work?
>
> *Answer:*
> 
> **Hard Link:** Points directly to the inode of a file.  
> *Advantage:* Efficient and remains valid even if the original name is removed.
> 
> **Symbolic Link:** Points to the pathname of a file.  
> *Advantage:* Can link to directories and across different filesystems.
> 
> **Symbolic Link Mechanism:** It stores the path to the target file, and the system resolves this path when accessing the link.

---

> [!exercise] Question 4
> Three different protection mechanisms that we have discussed are capabilities, access control lists, and the UNIX rwx bits. For each of the following protection problems, tell which of these mechanisms can be used.
>
> (a) Ken wants his files readable by everyone except his office mate.  
> (b) Mitch and Steve want to share some secret files.  
> (c) Linda wants some of her files to be public.
>
> *Answer:*
> 
> (a) **Access Control Lists (ACLs)**
> 
> (b) **Capabilities**
> 
> (c) **UNIX rwx bits**

---

> [!exercise] Question 5
> Discuss some of the issues that can mean that even the best system design cannot guarantee invulnerability to malicious attacks.
>
> *Answer:*
> 
> - **Human Error:** Misconfigurations and mistakes can create vulnerabilities.
> - **Zero-Day Exploits:** Unknown vulnerabilities can be exploited before patches are available.
> - **Insider Threats:** Authorized users may misuse their access.
> - **Complexity:** Complex systems can have unforeseen flaws.
> - **Social Engineering:** Manipulating users to bypass security measures.