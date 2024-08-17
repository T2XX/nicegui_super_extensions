from fastapi import FastAPI
from nicegui import ui
import sys
import os

sys.path.append(os.getcwd())
from src.nicegui_super_extensions.reorderable import (
    ReorderableItem,
    ReorderableColumn,
)

app = FastAPI()


def init(fastapi_app: FastAPI) -> None:

    @ui.page("/")
    def show():
        with ReorderableColumn() as col:
            with ReorderableItem() as draggable:
                ui.label("Draggable Item 1")

            with ReorderableItem() as draggable:
                ui.label("Draggable Item 2")

            with ReorderableItem() as draggable:
                ui.label("Draggable Item 3")

    ui.run_with(
        fastapi_app, mount_path="/", storage_secret="pick your private secret here"
    )


if __name__ == "__main__":
    import uvicorn

    init(app)
    uvicorn.run(app, host="127.0.0.1", port=8000)
