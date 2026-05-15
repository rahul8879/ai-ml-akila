# fast api logic

# rest endpoint ??


from fastapi import FastAPI
from app.core.config import get_setings
from fastapi.responses import HTMLResponse
from pathlib import Path
app = FastAPI()
from app.router import batch
settings = get_setings()

app.include_router(batch.router)


@app.get("/", include_in_schema=False)
def dashboard():
    """Serves the ScamGuard AI dashboard."""
    html_content = Path("home.html").read_text(encoding="utf-8")
    return HTMLResponse(content=html_content)






@app.get("/",tags=["health"])
def home():
    from app.prompts.registry import prompt_registry
    return {
        "default_version": settings.default_prompt_version,
        "available_versions": prompt_registry.list_versions()
    }

@app.get("/versions",tags=["health"])
def list_prompt_versions():
    from app.prompts.registry import prompt_registry
    return {
        "default_version": settings.default_prompt_version,
        "available_versions": prompt_registry.list_versions()
    }



