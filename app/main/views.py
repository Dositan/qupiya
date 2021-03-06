import secrets

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_babel import _
from flask_login import current_user, login_required

from .forms import GenerateForm, RecordForm
from .models import Record

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    """
    `/` endpoint

    App's about page: its purposes, usage and mission
    """
    return render_template("main/index.html")


@bp.route("/generate", methods=("GET", "POST"))
def generate():
    """
    `/generate` endpoint

    Generates a random safe password for you.
    """
    form = GenerateForm(request.form)
    if form.validate_on_submit():
        result = secrets.token_urlsafe(form.length.data)
        return render_template("main/result.html", result=result)

    return render_template("main/generate.html", form=form)


@bp.route("/save", methods=("GET", "POST"))
@login_required
def save():
    """
    `/save` endpoint

    Save a record: `name`, `login`, `password` and `comment`.
    """
    form = RecordForm(request.form)
    if form.validate_on_submit():
        Record.create(
            name=form.name.data,
            login=form.login.data,
            password=form.password.data,
            comment=form.comment.data,
            user_id=current_user.id,
        )
        flash(_("Your password has been saved."), "success")
        return redirect(url_for("main.index"))
    return render_template("main/save.html", form=form)


@bp.route("/<int:id>/update", methods=("GET", "POST"))
@login_required
def update(id):
    form = RecordForm(request.form)
    record = Record.get_by_id(id)
    if form.validate_on_submit():
        record.update(
            name=form.name.data,
            login=form.login.data,
            password=form.password.data,
            comment=form.comment.data,
            user_id=current_user.id,
        )
        flash(_("Your credentials were updated."), "success")
        return redirect(url_for("main.index"))
    return render_template("main/update.html", form=form, record=record)


@bp.route("/<int:id>/delete", methods=("POST",))
@login_required
def delete(id):
    Record.get_by_id(id).delete()
    flash(_("Your password has been deleted."), "success")
    return redirect(url_for("main.index"))
