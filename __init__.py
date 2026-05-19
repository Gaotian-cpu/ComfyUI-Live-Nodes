from .nodes.request_nodes import FileToKeyValue


NODE_CLASS_MAPPINGS = {
    # "FileToKeyValue": FileToKeyValue,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    # "FileToKeyValue": "File to KeyValue",
}

# 告诉 ComfyUI 前端资源所在的目录
WEB_DIRECTORY = "./web"

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']