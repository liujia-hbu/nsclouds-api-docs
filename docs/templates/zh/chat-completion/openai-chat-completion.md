# OpenAI

### 1. 概述

OpenAI 是全球领先的 AI 研究机构，提供强大的 GPT 系列大语言模型，包括 GPT-4、GPT-3.5 等，支持文本生成、对话、图像生成等多种 AI 能力。

{% hint style="success" %}
本 API 与 OpenAI 接口格式兼容。
{% endhint %}

**模型列表：**

* `gpt-5` (chat 模式)
* `gpt-5.2` (chat 模式)
* `gpt-5.4` (chat 模式)
* `gpt-5.3-codex` (chat 模式)

### 功能验证说明

| 功能 | 状态 | 说明 |
|------|------|------|
| 基础请求 | ✅ 验证通过 | gpt-5, gpt-5.2 可用 |
| 流式响应 | ✅ 验证通过 | 测试成功，返回流式数据 |
| 图像输入 | ✅ 验证通过 | gpt-5.2 支持多模态图像输入 |
| 函数调用 | ⚠️ 部分支持 | 模型识别函数调用请求但未执行实际调用 |

### 2.接口详情

{% openapi-operation spec="openai-zh-{{ENV}}" path="/v1/chat/completions" method="post" %}
[OpenAPI openai](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/{{ENV}}/zh/openai.bundled.yaml)
{% endopenapi-operation %}
