from flask import Blueprint, render_template, request, redirect, abort
from datetime import date, datetime

from config import ALLOWED_EXTENSIONS
from helpers import save_profile_picture

user_bp = Blueprint("user_bp", __name__, template_folder="templates")

users = []


@user_bp.route("/")
def show_user():
    this_year = date.today().year
    return render_template("show_user.html", users=users, this_year=this_year)


@user_bp.post("/sign_up")
def sign_up():
    info = "username", "password", "surname", "name", "birth_year"
    user_info = {}
    for i in info:
        value = request.form.get(i, "").strip(" ")
        if value == "":
            return redirect("/sign_up")
        user_info[i] = value
    profile_picture = request.files["photo"]
    extension = request.files["photo"].filename.rsplit('.', 1)[-1].lower()
    if extension not in ALLOWED_EXTENSIONS:
        abort(400)  # izin verilmeden uzantıda dosya yüklenirse verilecek hata!
    profile_picture_path = save_profile_picture(input_file=profile_picture, extension=extension)
    user_info["profile_picture"] = profile_picture_path
    user_info["birth_year"] = datetime.strptime(user_info["birth_year"], "%Y-%m-%d").year
    print(user_info)
    users.append(user_info)
    return redirect("/")


@user_bp.get("/register")
def register():
    max_year = date.today().year - 18
    min_year = date.today().year - 100
    image_extensions = ",".join(["." + ext for ext in ALLOWED_EXTENSIONS])
    return render_template("sign_up.html", max_year=max_year, min_year=min_year, image_extensions=image_extensions)
