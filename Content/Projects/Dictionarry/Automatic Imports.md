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
	- setting inside external app modal - import on pull, import on schedule. choose schedule - gets added as a task in the database.


FOR TOMORROW SAM
- automatic pull done
- need to update arr settings to add:
	- data to sync
	- when to sync it - on pull (how do we know? does it need to alert the task?), on schedule
- this needs to get saved as an actual task, so that it shows up in the tasks endpoints and can be ran manually from the tasks menu
- when we update the arr settings, it needs to update the task / delete it. 
- hashing module for imports
	- hash setting inside arr modal 
- need to parse changes better
- need to improve styling for view changes / conflicts
- CUTOFF NOT BEING COMPILED PROPERLY FOR 2160p REMUX!!!!
- currently working on TESTING 2160p REMUX
- NEED TO DEAL WITH DANGLING REFERENCES DELETING REGEX PATTERNS AND CUSTOM FORMATS
- REPO SYNC TASK ONLY ENABLED IF REPO CONNECTED!!!!