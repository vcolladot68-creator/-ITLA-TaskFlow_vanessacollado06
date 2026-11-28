

from datetime import datetime

from sqlalchemy import or_

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user

from app import db
from app.models import Task, Project, Category


tasks = Blueprint("tasks", __name__, url_prefix="/tasks")

VALID_STATUSES = ["pending", "in_progress", "completed"]
VALID_PRIORITIES = ["low", "medium", "high"]


def get_form_options():
    """Obtiene únicamente los proyectos y categorías del usuario actual."""
    projects = Project.query.filter_by(user_id=current_user.id).all()
    categories = Category.query.filter_by(user_id=current_user.id).all()
    return projects, categories


def validate_task_form():
    """Valida los datos recibidos del formulario."""

    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    status = request.form.get("status", "pending")
    priority = request.form.get("priority", "medium")
    due_date_value = request.form.get("due_date", "")
    project_id_value = request.form.get("project_id", "")
    category_id_value = request.form.get("category_id", "")

    # Validar título
    if not title:
        return None, "El título de la tarea es obligatorio."

    if len(title) < 3:
        return None, "El título debe tener al menos 3 caracteres."

    if len(title) > 150:
        return None, "El título no puede superar los 150 caracteres."

    # Validar descripción
    if len(description) > 1000:
        return None, "La descripción no puede superar los 1000 caracteres."

    # Validar estado y prioridad
    if status not in VALID_STATUSES:
        return None, "El estado seleccionado no es válido."

    if priority not in VALID_PRIORITIES:
        return None, "La prioridad seleccionada no es válida."

    # Validar fecha
    due_date = None

    if due_date_value:
        try:
            due_date = datetime.strptime(
                due_date_value, "%Y-%m-%d"
            ).date()
        except ValueError:
            return None, "La fecha seleccionada no es válida."

    # Validar proyecto
    project = None

    if project_id_value:
        try:
            project_id = int(project_id_value)
        except ValueError:
            return None, "El proyecto seleccionado no es válido."

        project = Project.query.filter_by(
            id=project_id,
            user_id=current_user.id
        ).first()

        if not project:
            return None, "El proyecto seleccionado no es válido."

    # Validar categoría
    category = None

    if category_id_value:
        try:
            category_id = int(category_id_value)
        except ValueError:
            return None, "La categoría seleccionada no es válida."

        category = Category.query.filter_by(
            id=category_id,
            user_id=current_user.id
        ).first()

        if not category:
            return None, "La categoría seleccionada no es válida."

    data = {
        "title": title,
        "description": description,
        "status": status,
        "priority": priority,
        "due_date": due_date,
        "project_id": project.id if project else None,
        "category_id": category.id if category else None
    }

    return data, None


@tasks.route("/")
@login_required
def index():
    """Muestra las tareas con opciones de búsqueda y filtrado."""

    task_query = Task.query.filter_by(user_id=current_user.id)

    search = request.args.get("q", "").strip()
    status = request.args.get("status", "").strip()
    priority = request.args.get("priority", "").strip()

    # Buscar por título o descripción
    if search:
        task_query = task_query.filter(
            or_(
                Task.title.ilike(f"%{search}%"),
                Task.description.ilike(f"%{search}%")
            )
        )

    # Filtrar por estado
    if status in VALID_STATUSES:
        task_query = task_query.filter_by(status=status)
    else:
        status = ""

    # Filtrar por prioridad
    if priority in VALID_PRIORITIES:
        task_query = task_query.filter_by(priority=priority)
    else:
        priority = ""

    user_tasks = task_query.order_by(
        Task.created_at.desc()
    ).all()

    return render_template(
        "tasks/index.html",
        tasks=user_tasks,
        search=search,
        selected_status=status,
        selected_priority=priority
    )


@tasks.route("/create", methods=["GET", "POST"])
@login_required
def create():
    """Permite crear una nueva tarea."""

    projects, categories = get_form_options()

    if request.method == "POST":
        data, error = validate_task_form()

        if error:
            flash(error, "danger")
            return render_template(
                "tasks/create.html",
                projects=projects,
                categories=categories
            )

        new_task = Task(
            **data,
            user_id=current_user.id
        )

        db.session.add(new_task)
        db.session.commit()

        flash("La tarea se creó correctamente.", "success")
        return redirect(url_for("tasks.index"))

    return render_template(
        "tasks/create.html",
        projects=projects,
        categories=categories
    )


@tasks.route("/<int:task_id>/edit", methods=["GET", "POST"])
@login_required
def edit(task_id):
    """Permite editar una tarea del usuario actual."""

    task = Task.query.filter_by(
        id=task_id,
        user_id=current_user.id
    ).first_or_404()

    projects, categories = get_form_options()

    if request.method == "POST":
        data, error = validate_task_form()

        if error:
            flash(error, "danger")
            return render_template(
                "tasks/edit.html",
                task=task,
                projects=projects,
                categories=categories
            )

        task.title = data["title"]
        task.description = data["description"]
        task.status = data["status"]
        task.priority = data["priority"]
        task.due_date = data["due_date"]
        task.project_id = data["project_id"]
        task.category_id = data["category_id"]

        db.session.commit()

        flash("La tarea se actualizó correctamente.", "success")
        return redirect(url_for("tasks.index"))

    return render_template(
        "tasks/edit.html",
        task=task,
        projects=projects,
        categories=categories
    )


@tasks.route("/<int:task_id>/delete", methods=["POST"])
@login_required
def delete(task_id):
    """Elimina únicamente tareas pertenecientes al usuario actual."""

    task = Task.query.filter_by(
        id=task_id,
        user_id=current_user.id
    ).first_or_404()

    db.session.delete(task)
    db.session.commit()

    flash("La tarea se eliminó correctamente.", "success")
    return redirect(url_for("tasks.index"))
