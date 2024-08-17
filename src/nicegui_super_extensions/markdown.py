import base64
from nicegui import ui


def encode_string(string):
    """
    Encode the string using base64 and ensure that the encoded result is of string type.

    Args:
    String: The string to be encoded.

    Returns:
    The encoded string.
    """

    encoded_bytes = base64.b64encode(string.encode("utf-8"))
    encoded_string = encoded_bytes.decode("utf-8")
    return encoded_string


def initMarkdownPreViewerDependence():
    """load  Dependence in page, !YOU NEED LOAD BEFORE PAGE FIRST LOAD!"""
    ui.add_head_html(
        """<link rel="stylesheet" href="https://unpkg.com/vditor/dist/index.css" />
<script src="https://unpkg.com/vditor/dist/index.min.js"></script>"""
    )


class MarkdownPreViewer(ui.html):

    def __init__(self):
        super().__init__()
        self.content = f"""<div id="{self.id}"></div>"""

    def render(
        self,
        markdown: str,
        cdn: str = "https://cdn.jsdelivr.net/npm/vditor",
        anchor: int = 0,
    ):
        """
        render markdown in preViewer

        Args:
        markdown: the origin markdown to render
        optional:
        cdn(optional): use which cdn to load the vditor
        more to see: https://ld246.com/article/1549638745630#options-preview
        """
        select_div = f'const el = document.getElementById("{self.id}");\n'
        rebuild = (
            f"markdown=decodeURIComponent(escape(atob('{ encode_string(markdown) }')));"
        )
        render = (
            'Vditor.preview(el,markdown,{ cdn: "'
            + cdn
            + '", anchor: '
            + str(anchor)
            + " });\n"
        )
        ui.run_javascript(select_div + rebuild + render)
