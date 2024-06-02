# Task 7:
CHANGES:
* Created user.py to store User class
* Created auth.py to handle login, signup, logout
* Created login.html, signup.html, admin.html, user_home.html stubs
* Added users table to database, and imported users to the app in __init__.py
* Added @login required to photo upload, edit, delete
* Added code stubs for photo edit, photo delete
* Session token should be created by Flask’s login libraries
* Added code stub for only accessing admin.html if the user has the admin role
* Added code stub for trying to view or edit an out-of-index image


## Tests
* New users must be able to signup using a name (non-unique), password (non-unique), username (unique), email (unique):
  * Test should fail if SQL injection commands are detected in any of the fields
  * Test should fail if username or email already exist
  * Test should fail if email is not in valid format
  * Test should fail if password does not match the safety features in `auth.py` (min. 12 chars, 1+ special chars)
  * Password should be hashed using SHA256
  * User should be redirected to the homepage
* Existing non-logged-in users should be able to login using their username/email and password
  * Users should be redirected to their user homepage on successful login, or
  * Users should be redirected to a clean login page on failed login
* Logged-in users should be able to logout
* Admins should be able to access the admin page
  * If the user does not have the 'admin' role, they should be disallowed access to the admin page
* Non-logged-in users should not be able to upload/edit/delete photos, and should be redirected to the login page