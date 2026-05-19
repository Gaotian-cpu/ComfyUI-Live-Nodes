# -*- coding: utf-8 -*-
"""
与请求有关的节点
"""
import os


class FileToKeyValue:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "file_path": ("STRING", {'default': ''}),
                "key_name": ("STRING", {"default": ""}),
            },
            'optional': {
                'key_value': ('KEY_VALUE', {'default': None}),
                'fail_on_error': ('BOOLEAN', {'default': False})
            }
        }

    RETURN_TYPES = ("KEY_VALUE",)
    FUNCTION = "convert"
    CATEGORY = "LiveNodes/RequestNode/Utils"

    def convert(self, file_path, key_name, key_value: dict = None, fail_on_error: bool = False):
        if not isinstance(key_value, dict):
            key_value = {}

        if not isinstance(file_path, str) or len(file_path) == 0:
            if fail_on_error:
                raise ValueError(u'文件路径为空，无法形成键值对')
            else:
                print(u'文件路径为空，无法形成键值对')
                return key_value

        if not os.path.isfile(file_path):
            if fail_on_error:
                raise ValueError(u'文件不存在，无法形成键值对：{}'.format(file_path))
            else:
                print(u'文件不存在，无法形成键值对：{}'.format(file_path))
                return key_value

        if not isinstance(key_name, str) or len(key_name) == 0:
            err_msg = u'键名为空，无法生成键值对！'
            if fail_on_error:
                raise ValueError(err_msg)
            else:
                print(err_msg)
                return key_value

        key_value.update({key_name: open(file_path, 'rb')})
        # Prepare files as a dictionary where keys are field names and values are file paths
        # Return a dictionary that can be consumed by the Key/Value node
        return key_value,



