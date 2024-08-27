## RDBMS
- Relational database management systems
- Tables of data joined by data relations - the sql model  
- Only efficient if the transactions are ACID transactions

### ACID
- Atomicity
	- The guarantee that all steps of a transactions will / wont occur
	- Both parts of the transaction must complete otherwise the transaction fails, and we need to be able to revert it

![[Pasted image 20231016154218.png]]

- Consistency
	- Data has to meet all validation rules
	- In the example, we use A+B=100 as a constraint to validate a transaction
- Isolation
	- Transactions do not affect each other
- Durability
	- If a transaction IS successful, we want the database to stay like this and not revert back to a prior state

### Implementing ACID
- Locking
- Distributed Transactions
##### Examples
```
You are told that a transaction has gone through successfully. There is still a possible risk to the Durability, what is it?
```

- Some sort of crash occurs that causes data loss. No backups are kept that are able to restore this version