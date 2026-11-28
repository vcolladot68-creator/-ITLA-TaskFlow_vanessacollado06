
from flask import Blueprint, render_template
from flask_login import login_required, current_user

from app.models import Task, Project

main = Blueprint("main", __name__)


@main.route("/")
@login_required
def dashboard():

    # Consultar las tareas del usuario autenticado
    user_tasks = Task.query.filter_by(user_id=current_user.id)

    # Estadísticas de tareas
    total_tasks = user_tasks.count()
    pending_tasks = user_tasks.filter_by(status="pending").count()
    in_progress_tasks = user_tasks.filter_by(status="in_progress").count()
    completed_tasks = user_tasks.filter_by(status="completed").count()

    # Cantidad de proyectos
    total_projects = Project.query.filter_by(
        user_id=current_user.id
    ).count()

    # Últimas cinco tareas
    recent_tasks = user_tasks.order_by(
        Task.created_at.desc()
    ).limit(5).all()

    return render_template(
        "main/dashboard.html",
        total_tasks=total_tasks,
        pending_tasks=pending_tasks,
        in_progress_tasks=in_progress_tasks,
        completed_tasks=completed_tasks,
        total_projects=total_projects,
        recent_tasks=recent_tasks
    )
