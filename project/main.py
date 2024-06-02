from flask import (
  Blueprint, render_template, request, 
  flash, redirect, url_for, send_from_directory, 
  current_app, make_response
)
from flask_login import login_user, login_required, logout_user
from .models import Photo
from sqlalchemy import asc, text
from . import db
import os

main = Blueprint('main', __name__)

# This is called when the home page is rendered. It fetches all images sorted by filename.
@main.route('/')
def homepage():
  photos = db.session.query(Photo).order_by(asc(Photo.file))
  return render_template('index.html', photos = photos)

@main.route('/uploads/<name>')
def display_file(name):
  return send_from_directory(current_app.config["UPLOAD_DIR"], name)

# Upload a new photo
@main.route('/upload/', methods=['GET','POST'])
# Login required
@login_required
def new_photo():
  if request.method == 'POST':
    file = None
    if "fileToUpload" in request.files:
      file = request.files.get("fileToUpload")
    else:
      flash("Invalid request!", "error")

    if not file or not file.filename:
      flash("No file selected!", "error")
      return redirect(request.url)

    filepath = os.path.join(current_app.config["UPLOAD_DIR"], file.filename)
    file.save(filepath)

    newPhoto = Photo(name = request.form['user'], 
                    caption = request.form['caption'],
                    description = request.form['description'],
                    file = file.filename)
    db.session.add(newPhoto)
    flash('New Photo %s Successfully Created' % newPhoto.name)
    db.session.commit()
    return redirect(url_for('main.homepage'))
  else:
    return render_template('upload.html')

# This is called when clicking on Edit. Goes to the edit page.
@main.route('/photo/<int:photo_id>/edit/', methods = ['GET', 'POST'])
@login_required
def edit_photo(photo_id):
  # TODO: If logged-in user's name is not the same as the 
  # name of the photo's owner, then return them to the 
  # main page

  #TODO: If photo_id is out of range of the db, return them
  # to the main page instead of displaying an SQLAlchemy error

  editedPhoto = db.session.query(Photo).filter_by(id = photo_id).one()
  if request.method == 'POST':
    if request.form['user']:
      editedPhoto.name = request.form['user']
      editedPhoto.caption = request.form['caption']
      editedPhoto.description = request.form['description']
      db.session.add(editedPhoto)
      db.session.commit()
      flash('Photo Successfully Edited %s' % editedPhoto.name)
      return redirect(url_for('main.homepage'))
  else:
    return render_template('edit.html', photo = editedPhoto)


# This is called when clicking on Delete. 
@main.route('/photo/<int:photo_id>/delete/', methods = ['GET','POST'])
@login_required
def deletePhoto(photo_id):
  #TODO: If the user's name does not match the name of the requested
  # photo's owner, return them to the main page


  #TODO: If photo_id is out of range of the db, return them
  # to the main page instead of displaying an SQLAlchemy error



  fileResults = db.session.execute(text('select file from photo where id = ' + str(photo_id)))
  filename = fileResults.first()[0]
  filepath = os.path.join(current_app.config["UPLOAD_DIR"], filename)
  os.unlink(filepath)
  db.session.execute(text('delete from photo where id = ' + str(photo_id)))
  db.session.commit()
  
  flash('Photo id %s Successfully Deleted' % photo_id)
  return redirect(url_for('main.homepage'))


#------------------------------------------------------------------------------------------------------
# Added features

@main.route('/user')
@login_required
def user_page():
  #TODO: Should return user's homepage (and not another user's)
  return render_template('user_home.html')

@main.route('/search')
def search_page():
  return render_template('search.html')

@main.route('/like', methods = ['GET'])
@login_required
def likes(photo_id, user_id):
  # If user has not liked the photo, add it to the 'likes' ENUM variable in `users.db` AND 
  #   increment the `likes` variable for the photo in `photos.db`
  # Else remove the photo id from the `likes` variable

  # This code stub should have a timeout feature (30 seconds) to prevent spam:
  #   attempting to add/remove a like within this period should return
  #   a timeout message: "Try again in a short while"

  return