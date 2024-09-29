# md-table-to-excel

这是一个使用pipx进行安装的工具，这个工具是一个命令行工具，可以接受一个markdown的内容，提取内容中的markdown中table格式的内容，然后转换为Excel能够直接粘贴的文本。

## 功能

1. 如果直接调用 md-table-to-excel ，则从粘贴板中读取markdown内容，然后输出到粘贴板中。
2. 如果调用 md-table-to-excel < markdown.md ，则从文件中读取markdown内容，然后输出到粘贴板中。
3. 如果调用 md-table-to-excel > output.txt ，则从粘贴板中读取markdown内容，然后输出到文件中。
4. 如果调用 md-table-to-excel -h ，则输出帮助信息。

## 安装

确保您已经安装了pipx，然后运行：

```bash
pipx install md-table-to-excel
```

## 使用

```bash
md-table-to-excel
```

```bash
md-table-to-excel < markdown.md
```

```bash
md-table-to-excel > output.txt
```

## 开发

如果您想要开发这个工具，请按照以下步骤操作：

1. 克隆仓库
2. 安装Poetry：`pip install poetry`
3. 安装依赖：`poetry install`
4. 进行开发
5. 构建项目：`poetry build`
6. 使用pipx安装本地版本：`pipx install .`

## 许可证

MIT

