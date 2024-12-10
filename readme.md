# Python flask webapp
## Work in progress
Web application for creating posts in Markdown with thread categorization.
 - Python 3.11
 - MVC
 - sqlite3 database
 - Custom Token-based Authentication with Server-side State

## Database
 - POSTS
   - ID
   - TITLE
   - CONTENT
   - THREAD_ID
   - AUTHOR_ID
   - TIME_CREATE
   - TIME_EDIT
   - HIDDEN
 - USERS
   - ID
   - LOGIN
   - PASSWORD
   - BAN
   - AVATAR
 - THREADS - names of threads
   - ID
   - NAME
   - ICON
 - ADMINS - list of users with administrative privileges
   - ID
   - USER_ID
 - READ - permissions for users to read specific threads
   - ID
   - USER_ID
   - THREAD_ID
 - WRITE - permissions for users to add posts to specific threads
   - ID
   - USER_ID
   - THREAD_ID
