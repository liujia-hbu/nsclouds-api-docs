import json
import yaml
import glob
import os

# 自定义 YAML 代表器，确保标签顺序
class OrderedDumper(yaml.SafeDumper):
    pass

def represent_dict(dumper, data):
    # 定义 OpenAPI 规范的标签顺序
    openapi_order = [
        'openapi', 'info', 'servers', 'paths', 'components',
        'security', 'tags', 'externalDocs'
    ]
    items = []
    # 先添加顺序标签
    for key in openapi_order:
        if key in data:
            items.append((key, data[key]))
    # 再添加其他标签
    for key, value in data.items():
        if key not in openapi_order:
            items.append((key, value))
    return dumper.represent_mapping('tag:yaml.org,2002:map', items)

OrderedDumper.add_representer(dict, represent_dict)

# 查找所有 openapi.json 文件
json_files = glob.glob('docs/**/openapi.json', recursive=True)

for json_file in json_files:
    # 生成对应的 YAML 文件路径
    yaml_file = json_file.replace('.json', '.yaml')
    
    # 读取 JSON 文件
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 写入 YAML 文件，使用自定义的 dumper
    with open(yaml_file, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, Dumper=OrderedDumper, default_flow_style=False, allow_unicode=True)
    
    print(f"转换完成：{yaml_file}")

print("所有文件转换完成！")