# OpenAI - 图像生成

### 1. 概述

OpenAI 的图像生成 API，与 OpenAI 接口格式兼容。

{% hint style="success" %}
本 API 与 OpenAI 接口格式兼容。
{% endhint %}

**模型列表：**

* `gpt-image-1` (image_generation 模式)

### 功能验证说明

| 功能 | 状态 | 说明 |
|------|------|------|
| 基础请求 | ✅ 验证通过 | /v1/images/generations 验证通过 |
| 图像编辑 | ✅ 验证通过 | /v1/images/edits 验证通过 |

### 2. 接口详情

{% openapi-operation spec="openai-zh-global" path="/v1/images/generations" method="post" %}
[OpenAPI openai](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/global/zh/openai.bundled.yaml)
{% endopenapi-operation %}
