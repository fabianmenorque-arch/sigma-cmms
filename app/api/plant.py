from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/ui/plant")
def plant(request: Request):

    # demo data (luego lo conectás a DB)
    data = {
        "total": 12,
        "pending": 5,
        "in_progress": 4,
        "completed": 3
    }

    return templates.TemplateResponse(
        "plant.html",
        {"request": request, **data}
    )
