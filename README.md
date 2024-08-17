# nicegui_super_extensions

provide extension features for Nicegui

<a title="MIT" target="_blank" href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/license-MIT-orange.svg?style=flat-square"></a>

<p align="center">
<a href="https://github.com/T2XX/nicegui_super_extensions/blob/main/README.md">English</a>  |  <a href="https://github.com/T2XX/nicegui_super_extensions/blob/main/README_zh_CN.md">简体中文</a>
</p>

# extensions

### [markdown](https://github.com/T2XX/nicegui_super_extensions/blob/main/src/nicegui_super_extensions/markdown.py)

- powered by [vditor](https://github.com/Vanessa219/vditor/blob/master/README_en_US.md)![vditor](https://b3log.org/images/brand/vditor-128.png), you can see the feature from [here](https://github.com/Vanessa219/vditor/blob/master/README_en_US.md#--features)

#### install

```shell
pip install nicegui_super_extensions 
```

#### how to use it

1. step 1, load Dependence before page require

```python
from nicegui_super_extensions.markdown import MarkdownPreViewer, initMarkdownPreViewerDependence
initMarkdownPreViewerDependence()
```

2. step 2, create widget and render markdown

```python
md = MarkdownPreViewer().render(markdown)
```

3. (optional)step 3, update markdown

```python
md.render(new_markdown)
```

### [reconnect_box](https://github.com/T2XX/nicegui_super_extensions/blob/main/src/nicegui_super_extensions/reconnect_box.py)

- before

  ![before](https://github.com/T2XX/nicegui_super_extensions/blob/main/image/1723880105580.png?raw=true)
- after

  ![after](https://github.com/T2XX/nicegui_super_extensions/blob/main/image/1723879996849.png?raw=true)

#### how to use it

1. step 1

```python
from nicegui_super_extensions.reconnect_box import set_reconnect_box
```

1. step 2

```python
# just can use after page load
set_reconnect_box()
# after page load to use it
app.on_connect(lambda: set_reconnect_box())
```

### [reorderable](https://github.com/T2XX/nicegui_super_extensions/blob/main/src/nicegui_super_extensions/reorderable.py)

let an item reorderable in row or column

#### how to use it

1. step 1

```python
nicegui_super_extensions.reorderable import ReorderableItem,ReorderableColumn
```

1. step 2

```python
with ReorderableColumn() as col:
    with ReorderableItem() as draggable:
        ui.label("Draggable Item 1")

    with ReorderableItem() as draggable:
        ui.label("Draggable Item 2")

    with ReorderableItem() as draggable:
        ui.label("Draggable Item 3")
```
