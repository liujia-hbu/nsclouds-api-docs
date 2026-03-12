# OpenAI - 文本补全

### 1. 概述

OpenAI 的文本补全 API，与 OpenAI 接口格式兼容。

{% hint style="success" %}
本 API 与 OpenAI 接口格式兼容。
{% endhint %}

**模型列表：**

* `gpt-5` (chat 模式，支持 completion)
* `gpt-5.2` (chat 模式，支持 completion)
* `gpt-5.4` (chat 模式，支持 completion)
* `gpt-5.3-codex` (chat 模式，支持 completion)

### 功能验证说明

| 功能 | 状态 | 说明 |
|------|------|------|
| 基础请求 | ✅ 验证通过 | /v1/completions 验证通过 |
| 流式响应 | ✅ 验证通过 | /v1/chat/completions 流式响应验证通过 |

### 2. 接口详情

{% openapi-operation spec="openai-zh-global" path="/v1/completions" method="post" %}
[OpenAPI openai](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/global/zh/openai.bundled.yaml)
{% endopenapi-operation %}
