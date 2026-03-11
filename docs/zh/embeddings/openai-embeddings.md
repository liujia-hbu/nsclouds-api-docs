# OpenAI - 向量嵌入

### 1. 概述

OpenAI 的向量嵌入 API，与 OpenAI 接口格式兼容。

{% hint style="success" %}
本 API 与 OpenAI 接口格式兼容。
{% endhint %}

**模型列表：**

（暂无）

### 功能验证说明

| 功能 | 状态 | 说明 |
|------|------|------|
| 基础请求 | ❌ 不可用 | model_info 中无 OpenAI embedding 模式模型 |

### 2. 接口详情

{% openapi-operation spec="openai-zh" path="/v1/embeddings" method="post" %}
[OpenAPI openai](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/zh/openai.bundled.yaml)
{% endopenapi-operation %}
