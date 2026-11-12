# scripts/save_summary.py
import sys
from pathlib import Path
from datetime import date

def main():
    if len(sys.argv) < 2:
        print("用法: python save_summary.py <摘要内容文件> [输出路径]")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    if not input_path.exists():
        print(f"错误：文件不存在 {input_path}")
        sys.exit(1)

    content = input_path.read_text(encoding="utf-8")

    if len(sys.argv) >= 3:
        output_path = Path(sys.argv[2])
    else:
        output_path = Path(f"summary-{date.today().isoformat()}.md")

    output_path.write_text(content, encoding="utf-8")
    print(f"摘要已保存到: {output_path.resolve()}")

if __name__ == "__main__":
    main()