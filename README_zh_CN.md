# nicegui_super_extensions

为Nicegui提供一系列扩展功能

<a title="MIT" target="_blank" href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/license-MIT-orange.svg?style=flat-square"></a>

<p align="center">
<a href="https://github.com/T2XX/nicegui_super_extensions/blob/main/README.md">English</a>  |  <a href="https://github.com/T2XX/nicegui_super_extensions/blob/main/README_zh_CN">简体中文</a>
</p>

# extensions

### [markdown](https://github.com/T2XX/nicegui_super_extensions/blob/main/src/nicegui_super_extensions/markdown.py)

- 使用[vditor](https://github.com/Vanessa219/vditor/blob/master/README_en_US.md)![vditor](https://b3log.org/images/brand/vditor-128.png) 提供支持, 你可以在[这里](https://github.com/Vanessa219/vditor/blob/master/README_en_US.md#--features)查看支持的功能

#### 安装

```shell
pip install nicegui_super_extensions 
```

#### 如何使用

1. 第一步，在页面加载成功前导入依赖

```python
from nicegui_super_extensions.markdown import (
    MarkdownPreViewer,
    initMarkdownPreViewerDependence,
)
initMarkdownPreViewerDependence()
```

2. 第二步，使用组件并渲染markdown

```python
MarkdownPreViewer().render(markdown)
```

3. (可选)第三步, 更新markdown内容

```python
md.render(new_markdown)
```

### [reconnect_box](https://github.com/T2XX/nicegui_super_extensions/blob/main/src/nicegui_super_extensions/reconnect_box.py)

- 之前

  ![before](https://github.com/T2XX/nicegui_super_extensions/blob/main/image/1723880105580.png?raw=true)
- 现在

  ![after](https://github.com/T2XX/nicegui_super_extensions/blob/main/image/1723879996849.png?raw=true)

#### 如何使用

1. 第一步

```python
from nicegui_super_extensions.reconnect_box import set_reconnect_box
```

1. 第二步

```python
# just can use after page load
set_reconnect_box()
# after page load to use it
app.on_connect(lambda: set_reconnect_box())
```

### [reorderable](https://github.com/T2XX/nicegui_super_extensions/blob/main/src/nicegui_super_extensions/draggable.py)

let an item reorderable in row or column

#### how to use it

1. 第一步

```python
nicegui_super_extensions.reorderable import ReorderableItem,ReorderableColumn
```

1. 第二步

```python
with ReorderableColumn() as col:
    with ReorderableItem() as draggable:
        ui.label("Draggable Item 1")

    with ReorderableItem() as draggable:
        ui.label("Draggable Item 2")

    with ReorderableItem() as draggable:
        ui.label("Draggable Item 3")
```
