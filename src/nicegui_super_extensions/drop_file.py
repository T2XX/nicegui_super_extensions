import base64
from nicegui import ui


class DropDetectArera(ui.card):
    def __init__(self):
        super().__init__()
        dropfile = ui.html("")
        id = "drop" + str(dropfile.id)
        self.dropfile = id
        dropfile.set_content(f"""<div id="{id}"></div>""")
        
        self.component(dropfile)

    def start_monitor(self, backgroundColor="lightblue"):
        ui.run_javascript(
            f'const dr = document.getElementById("{self.id}");\n'
            + "dr.addEventListener('dragover', (event) => {"
            + "event.preventDefault();"
            + f'dr.style.backgroundColor = "{backgroundColor}";\n'
            + "});"
            + """dr.addEventListener('drop', (event) => {
  // 阻止默认行为
  event.preventDefault();
  // 设置拖放区域的样式恢复默认
  dr.style.backgroundColor = 'white';

  // 获取拖放的文件列表
  const files = event.dataTransfer.files;

  // 遍历文件列表
  for (const file of files) {
    // 处理文件，例如读取文件内容
    const reader = new FileReader();
    reader.onload = (e) => {
      // 文件内容
      console.log(e.target.result);
    };
    // 读取文件内容
    reader.readAsText(file);
  }
});

// 当鼠标离开拖放区域时
dr.addEventListener('dragleave', () => {
  // 设置拖放区域的样式恢复默认
  dr.style.backgroundColor = 'white';
});"""
        )
