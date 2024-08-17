from nicegui import ui


def set_reconnect_box(title="与服务器连接断开👽", message="正在重连中。。。"):
    """change the connect_box text, must call after ui is running"""
    ui.run_javascript(
        'const popup = document.getElementById("popup");\n'
        + "if (popup) {\n"
        + 'const spans = popup.querySelectorAll("span");\n'
        + 'spans[0].textContent ="'
        + title
        + '";\n'
        + 'spans[1].textContent ="'
        + message
        + '";\n}'
    )
