#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: hihug
# @Date: 2025/6/6
# common/extract_utils.py
import re
import json
import jsonpath_rw_ext as jp
from common.log import logger


class Extractor:
    @staticmethod
    def extract_value(response, extract_config):
        """根据配置提取响应中的值"""
        if not extract_config:
            return None

        value = None
        try:
            # 正则表达式提取
            if extract_config.get('type') == 'regex':
                pattern = extract_config['pattern']
                match = re.search(pattern, response.text)
                if match:
                    # 返回第一个捕获组（如果有），否则返回整个匹配
                    value = match.group(1) if match.groups() else match.group(0)

            # JSONPath 提取（默认方式）
            else:
                # 尝试解析为 JSON
                try:
                    json_data = response.json()
                    jsonpath_expr = list(extract_config.values())[0]
                    matches = jp.match(jsonpath_expr, json_data)
                    if matches:
                        value = matches[0]
                except json.JSONDecodeError:
                    logger.warning("响应不是有效的JSON，无法使用JSONPath提取")

        except Exception as e:
            logger.error(f"提取值失败: {str(e)}")

        if value:
            logger.info(f"提取值成功: {value[:10]}...")  # 只显示前10个字符
        else:
            logger.warning(f"未提取到值，配置: {extract_config}")

        return value