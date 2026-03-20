# OpenAI

### 1. 概述

OpenAI 是全球领先的 AI 研究机构，提供强大的 GPT 系列大语言模型，包括 GPT-4、GPT-3.5 等，支持文本生成、对话、图像生成等多种 AI 能力。

{% hint style="success" %}
本 API 与 OpenAI 接口格式兼容。
{% endhint %}

**模型列表：**

* `gpt-5` (chat 模式)
* `gpt-5.1` (chat 模式)
* `gpt-5.2` (chat 模式)
* `gpt-5.4` (chat 模式)
* `gpt-5.3-codex` (chat 模式)

### 功能验证说明

| 功能 | 状态 | 说明 |
|------|------|------|
| 基础请求 | ✅ 验证通过 | 所有模型均可用且响应正常 |
| 流式响应 | ✅ 验证通过 | 所有模型均支持流式响应 |
| 图像输入 | ✅ 验证通过 | 所有模型均支持多模态图像输入 |
| 函数调用 | ✅ 验证通过 | 所有模型均正确处理函数调用请求 |

### 2.接口详情

{% openapi-operation spec="openai-zh-{{ENV}}" path="/v1/chat/completions" method="post" %}
[OpenAPI openai](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/{{ENV}}/zh/openai.bundled.yaml)
{% endopenapi-operation %}
