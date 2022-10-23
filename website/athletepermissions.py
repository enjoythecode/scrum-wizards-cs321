from urllib import request
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import Note

views = Blueprint('views', __name__)

#@views.route('/', methods=['GET', 'POST'])
#@login_required
#def home():
#
#    if request.method == "POST":
#        note = request.form.get('note')
#
#        if len(note) < 1:
#            flash('Note is too short!', category='error')
#        else:
#            new_note = Note(data=note, user_id=current_user.id)
#            db.session.add(new_note)
#            db.session.commit()
#            flash('Note added!', category='success')
#
#    return render_template("home.html", user=current_user)


# deleting a user 
@views.route("/remove/<string:id>", methods=['GET'])
@login_required
def remove(id):
    user = User.query.get(id)
    
    if user:
        if user.user_id == current_user.id:
            db.session.delete(user)
            db.session.commit()
            flash('User deleted!', category='success')

    return redirect(url_for('views.home'))