# Help/Manual Compendium Reader/Viewer

## Information
### Description
+ An assistant CLI utility used to retrieve/read help/manuals from the compendium on the local machine

### Features
1. Check if the manual/help of the topic of choice exists in the temporary directory
1.1. If the file does not exist: 
1.1.1. Pull down the manual of choice from the remote repository
1.1.2. Write the manual into a file stored in a temporary directory as cache
1.2. If the file exists: Proceed
2. Read the downloaded manual from the cache temporary directory into buffer
3. Print the manual

