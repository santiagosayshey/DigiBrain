- Task to automatically pull
	- should this happen on repo sync? if changes found && if auto pull on, then pull
- Task to automatically import based on???
	- external app - new section for choosing which things to import
		- import as unique (generate a hash of the name + name of app and append to name of data)
		- find unique imports by hashing again, getting existing, hashing those and looking for matches
	- when does this run?
		- on pull
		- on schedule - maybe hash on import, then hash again before trying to import, see if hashes are same (no files changed, dont try to import if so)


we need settings for:
- automatic pull
	- not recommended if you are planning to edit database
	- toggle inside repo container
	- add a new task, toggle should say whether or not task is enabled and should run
- automatic import
	- doesnt run if the repo is in a merge state
	- 