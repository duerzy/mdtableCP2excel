import sys
import pyperclip
import markdown
from bs4 import BeautifulSoup

def extract_tables(md_content):
    html = markdown.markdown(md_content, extensions=['tables'])
    soup = BeautifulSoup(html, 'html.parser')
    tables = soup.find_all('table')
    return tables

def table_to_excel_format(table):
    rows = table.find_all('tr')
    excel_rows = []
    for row in rows:
        cells = row.find_all(['th', 'td'])
        excel_row = '\t'.join(
            '"{}"'.format('\n'.join(str(content).strip() for content in cell.contents).replace('\n', '').replace('<br/>', '\n').replace('<br>', '\n').replace('<br />', '\n'))
            for cell in cells
        )
        excel_rows.append(excel_row)
    return '\n'.join(excel_rows)

def main():
    if len(sys.argv) > 1 and sys.argv[1] == '-h':
        print("这是一个使用pipx安装的由花照小赵开发的md-table-to-excel工具，可以将markdown表格转换为excel表格。")
        print("使用方法:")
        print("1. md-table-to-excel：从剪贴板读取Markdown，输出到剪贴板")
        print("2. md-table-to-excel < markdown.md：从文件读取Markdown，输出到剪贴板")
        print("3. md-table-to-excel > output.txt：从剪贴板读取Markdown，输出到文件")
        return

    if sys.stdin.isatty():
        md_content = pyperclip.paste()
    else:
        md_content = sys.stdin.read()

    tables = extract_tables(md_content)
    excel_content = '\n\n'.join(table_to_excel_format(table) for table in tables)

    if sys.stdout.isatty():
        pyperclip.copy(excel_content)
        print("表格已转换并复制到剪贴板。")
    else:
        sys.stdout.write(excel_content)

if __name__ == "__main__":
    main()