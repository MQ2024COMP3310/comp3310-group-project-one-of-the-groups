# Task 9:
CHANGES:

## Search By Category
* Created code stubs on `admin.html` page, to allow admin users to perform superuser actions on the database (create/remove).
* Added `category` column to `photos.db`
* Added `search.html` page to allow users to search by category. Code stubs added to represent the search form. Also added route in `main.py`
* Added code stubs in `edit.html` to allow users to change the image category when editing an image

## Likes System
* Add `likes` column to `photos.db`
* Add `likes` column to `users.db`, using `ENUM` datatype to hold up to 65535 photo ids
* Added code stubs on `index.html` to display number of likes for each photo, and for users to add likes, and the widget users will use to like/unlike a photo
* Added code stub on `user_home.html` to display user's liked photos, from `user.likes` in `user.db`
* Added code stub in `main.py` to handle likes functions

---

## Search By Category Tests:
* Admins should be able to add or remove categories
* Users should be able to search by category; search should only return all images that match the queried category
* Logged-in users should be able to change the category of an image when editing
  * Test should fail if the user is not logged-in

## Likes System Tests:
* Logged-in users should be able to add a like to a photo:
  * The photo's like counter should be incremented
  * The photo's id should be added to the user's likes list
  * Non-logged-in users should not be able to add a like to a photo
* Logged-in users should be able to remove a like from a photo:
  * The photo's like counter should be decremented
  * The photo's id should be removed from the user's likes list
  * Non-logged-in users should not be able to remove a like from a photo
* Users should be able to add/remove a like only once every 30 seconds
  * Adding/removing a like within the timeframe should return a timeout message