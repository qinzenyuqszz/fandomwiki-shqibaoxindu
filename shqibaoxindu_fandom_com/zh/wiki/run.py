import os

def generate_html_index():
    # 获取当前文件夹的路径
    folder_path = os.getcwd()
    
    # 获取当前文件夹的文件列表
    file_list = os.listdir(folder_path)
    
    # 创建索引文件
    with open('index.html', 'w') as f:
        # 写入HTML头部
        f.write('<html>\n<head>\n<title>Index</title>\n</head>\n<body>\n')
        
        # 写入文件列表
        for file_name in file_list:
            # 排除隐藏文件和文件夹
            if not file_name.startswith('.'):
                # 使用HTML超链接来显示文件名和路径
                file_path = os.path.join('.', file_name)  # 使用相对路径
                f.write(f'<a href="{file_path}">{file_name}</a><br>\n')
        
        # 写入HTML尾部
        f.write('</body>\n</html>')

# 调用函数生成索引
generate_html_index()
