
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import db, bcrypt
from app.models import User

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        if not username or not email or not password:
            flash("Todos los campos son obligatorios.", "danger")
            return render_template("auth/register.html")

        if len(password) < 8:
            flash("La contraseña debe tener al menos 8 caracteres.", "danger")
            return render_template("auth/register.html")

        if password != confirm_password:
            flash("Las contraseñas no coinciden.", "danger")
            return render_template("auth/register.html")

        existing_user = User.query.filter(
            (User.username == username) | (User.email == email)
        ).first()

        if existing_user:
            flash("El usuario o correo electrónico ya está registrado.", "warning")
            return render_template("auth/register.html")

        password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

        new_user = User(
            username=username,
            email=email,
            password_hash=password_hash
        )

        db.session.add(new_user)
        db.session.commit()

        flash("Tu cuenta ha sido creada correctamente. Inicia sesión.", "success")
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password_hash, password):
            login_user(user)
            flash("Bienvenido a ITLA TaskFlow.", "success")

            next_page = request.args.get("next")

            if next_page and next_page.startswith("/"):
                return redirect(next_page)

            return redirect(url_for("main.dashboard"))

        flash("Correo electrónico o contraseña incorrectos.", "danger")

    return render_template("auth/login.html")


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Has cerrado sesión correctamente.", "info")
    return redirect(url_for("auth.login"))
