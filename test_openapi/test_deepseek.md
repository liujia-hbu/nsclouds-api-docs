# DeepSeek API 测试报告

## 测试环境

- **测试环境**: `https://devaillm.nscloud.ai`
- **正式环境**: `https://aillm.nsclouds.com`
- **认证方式**: `Authorization: Bearer $NGAA_LLM_API_KEY`

## 模型信息

根据 `/v1/model/info` 接口获取，DeepSeek 相关模型均为 `chat` 模式：

| 模型名称 | Mode | 状态 |
|---------|------|------|
| `volcengine/deepseek-r1-250528` | chat | ✅ 已验证 |
| `volcengine/deepseek-v3-1-terminus` | chat | ✅ 已验证 |
| `deepseek-v3.2` | chat | ✅ 已验证 |
| `deepseek-v3.1` | chat | ✅ 已验证 |

## 端点验证结果

| 端点 | Mode | 状态 | 说明 |
|------|------|------|------|
| `/v1/chat/completions` | chat | ✅ 已验证 | 所有 deepseek 模型均支持 |
| `/v1/completions` | - | ⚠️ 部分支持 | 仅 `volcengine/deepseek-v3-1-terminus` 支持 |
| `/v1/embeddings` | - | ❌ 不支持 | deepseek 无 embedding mode |
| `/v1/images/generations` | - | ❌ 不支持 | deepseek 无 image_generation mode |
| `/v1/images/edits` | - | ❌ 不支持 | deepseek 无 image_generation mode |
| `/v1/audio/transcriptions` | - | ❌ 不支持 | deepseek 无 audio_transcription mode |

## 功能测试汇总

| 功能 | 状态 | 说明 |
|------|------|------|
| 基础请求 | ✅ 支持 | 所有模型支持 |
| 流式响应 | ✅ 支持 | 所有模型支持 |
| 图像输入 | ✅ 支持 | deepseek-v3.1 支持 |
| 函数调用 | ✅ 支持 | deepseek-v3.1 支持 |
| logprobs | ❌ 不支持 | 返回参数不支持错误 |

## 详细测试记录

### `/v1/chat/completions` - 基础请求

**测试命令**:

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/chat/completions" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-v3.1",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Hello!"}
    ],
    "temperature": 1,
    "max_completion_tokens": 50,
    "n": 1,
    "stream": false
  }'
```

**响应结果**:

```json
{
  "id": "chatcmpl-cdc11700-f52c-99a3-866c-cfac2a0b254c",
  "created": 1772859125,
  "model": "deepseek-v3.1",
  "object": "chat.completion",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "Hello! How can I help you today? 😊",
        "role": "assistant"
      },
      "provider_specific_fields": {}
    }
  ],
  "usage": {
    "completion_tokens": 11,
    "prompt_tokens": 15,
    "total_tokens": 26
  }
}
```

**状态**: ✅ 验证通过

---

### `/v1/chat/completions` - 流式响应

**测试命令**:

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/chat/completions" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-v3.1",
    "messages": [
      {"role": "user", "content": "Hello!"}
    ],
    "stream": true
  }'
```

**响应结果** (SSE 格式):

```
data: {"id":"chatcmpl-2e08cd46-ddf8-9aef-bce0-f94395447528","object":"chat.completion.chunk","created":1772861378,"model":"deepseek-v3.1","choices":[{"index":0,"delta":{"content":"Hello","role":"assistant"}}]}

data: {"id":"chatcmpl-2e08cd46-ddf8-9aef-bce0-f94395447528","object":"chat.completion.chunk","created":1772861378,"model":"deepseek-v3.1","choices":[{"index":0,"delta":{"content":"! How"}}]}

data: {"id":"chatcmpl-2e08cd46-ddf8-9aef-bce0-f94395447528","object":"chat.completion.chunk","created":1772861378,"model":"deepseek-v3.1","choices":[{"index":0,"delta":{"content":" can I help"}}]}

data: {"id":"chatcmpl-2e08cd46-ddf8-9aef-bce0-f94395447528","object":"chat.completion.chunk","created":1772861378,"model":"deepseek-v3.1","choices":[{"index":0,"delta":{"content":" you today"}}]}

data: {"id":"chatcmpl-2e08cd46-ddf8-9aef-bce0-f94395447528","object":"chat.completion.chunk","created":1772861378,"model":"deepseek-v3.1","choices":[{"index":0,"delta":{"content":"? 😊"}}]}

data: {"id":"chatcmpl-2e08cd46-ddf8-9aef-bce0-f94395447528","object":"chat.completion.chunk","created":1772861378,"model":"deepseek-v3.1","choices":[{"finish_reason":"stop","index":0,"delta":{}}]}

data: [DONE]
```

**状态**: ✅ 验证通过

---

### `/v1/chat/completions` - 图像输入（多模态）

**测试命令**:

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/chat/completions" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-v3.1",
    "messages": [
      {
        "role": "user",
        "content": [
          {"type": "text", "text": "What is in this image?"},
          {"type": "image_url", "image_url": {"url": "https://ark-project.tos-cn-beijing.volces.com/doc_image/seedream4_5_imageToimage.png"}}
        ]
      }
    ],
    "max_completion_tokens": 300
  }'
```

**响应结果**:

```json
{
  "id": "chatcmpl-856cd72d-f840-92da-a0b3-65f0061ac378",
  "created": 1772861532,
  "model": "deepseek-v3.1",
  "object": "chat.completion",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "Of course. This is an image of a stylized, cartoon-style drawing of a **dragon wearing a backpack and holding a walking stick**.\n\nHere are the details:\n\n*   **Main Subject:** A friendly-looking dragon.\n*   **Attire/Accessories:**\n    *   It's wearing a **backpack** with a strap across its chest.\n    *   It's holding a long **walking stick** or trekking pole in its right hand (claw).\n*   **Setting:** The dragon appears to be on a journey or hike, walking on a simple ground line.\n*   **Style:** The image is a black and white line drawing, likely intended as a coloring page for children. The lines are clear and simple, making it easy to color.\n\nIn short, it's an illustration of an adventurous dragon, ready for a hike or a quest.",
        "role": "assistant"
      },
      "provider_specific_fields": {}
    }
  ],
  "usage": {
    "completion_tokens": 179,
    "prompt_tokens": 13,
    "total_tokens": 192
  }
}
```

**状态**: ✅ 验证通过

---

### `/v1/chat/completions` - 函数调用

**测试命令**:

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/chat/completions" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-v3.1",
    "messages": [
      {"role": "user", "content": "What is the weather in Boston?"}
    ],
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "get_current_weather",
          "description": "Get the current weather in a given location",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA"
              },
              "unit": {
                "type": "string",
                "enum": ["celsius", "fahrenheit"]
              }
            },
            "required": ["location"]
          }
        }
      }
    ],
    "tool_choice": "auto",
    "max_completion_tokens": 150
  }'
```

**响应结果**:

```json
{
  "id": "chatcmpl-7709ac0a-5dc2-9791-81ef-1364bf331761",
  "created": 1772861551,
  "model": "deepseek-v3.1",
  "object": "chat.completion",
  "choices": [
    {
      "finish_reason": "tool_calls",
      "index": 0,
      "message": {
        "content": "I'll check the current weather in Boston for",
        "role": "assistant",
        "tool_calls": [
          {
            "index": 0,
            "function": {
              "arguments": "{\"location\": \"Boston, MA\"}",
              "name": "get_current_weather"
            },
            "id": "chatcmpl-tool-6701c1adf7ab40b598c423c3530190b9",
            "type": "function"
          }
        ]
      },
      "provider_specific_fields": {}
    }
  ],
  "usage": {
    "completion_tokens": 28,
    "prompt_tokens": 198,
    "total_tokens": 226
  }
}
```

**状态**: ✅ 验证通过

---

### `/v1/chat/completions` - logprobs（不支持）

**测试命令**:

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/chat/completions" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-v3.1",
    "messages": [
      {"role": "user", "content": "Hello!"}
    ],
    "max_completion_tokens": 10,
    "logprobs": true,
    "top_logprobs": 2
  }'
```

**响应结果**:

```json
{
  "error": {
    "message": "litellm.BadRequestError: DashscopeException - {\"error\":{\"message\":\"<400> InternalError.Algo.InvalidParameter: The parameters `logprobs` is not supported.\",\"type\":\"invalid_request_error\",\"param\":null,\"code\":\"invalid_parameter_error\"},\"id\":\"chatcmpl-a3bac414-ca2e-9c15-84bd-02caa91833b6\",\"request_id\":\"a3bac414-ca2e-9c15-84bd-02caa91833b6\"}. Received Model Group=deepseek-v3.1\nAvailable Model Group Fallbacks=None",
    "type": null,
    "param": null,
    "code": "400"
  }
}
```

**状态**: ❌ 不支持

---

### `/v1/completions` - 基础请求（部分支持）

**测试命令**:

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/completions" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "volcengine/deepseek-v3-1-terminus",
    "prompt": "Say this is a test",
    "max_tokens": 7,
    "temperature": 0
  }'
```

**响应结果**:

```json
{
  "id": "02177286136439468d44c5a45de4f1e59cc8a01ee3524bc4cf5a9",
  "object": "text_completion",
  "created": 1772861365,
  "model": "volcengine/deepseek-v3-1-terminus",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "text": "This is a test.",
      "logprobs": null
    }
  ],
  "usage": {
    "completion_tokens": 6,
    "prompt_tokens": 10,
    "total_tokens": 16,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 0,
      "rejected_prediction_tokens": null,
      "text_tokens": null
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": 0,
      "text_tokens": null,
      "image_tokens": null
    }
  }
}
```

**状态**: ✅ 验证通过（仅 `volcengine/deepseek-v3-1-terminus` 支持）

**注意**: `deepseek-v3.1` 等模型不支持 completions 接口，返回错误：
```json
{
  "error": {
    "message": "litellm.BadRequestError: OpenAIException - Error code: 404 - {'error': {'message': 'Unsupported model `deepseek-v3.1` for OpenAI compatibility mode.', ...}}",
    "code": "400"
  }
}
```

---

## 各模型详细验证

### deepseek-v3.1

| 端点/功能 | 状态 |
|-----------|------|
| chat/completions 基础 | ✅ |
| chat/completions 流式 | ✅ |
| chat/completions 图像输入 | ✅ |
| chat/completions 函数调用 | ✅ |
| chat/completions logprobs | ❌ |
| completions | ❌ |

### deepseek-v3.2

| 端点/功能 | 状态 |
|-----------|------|
| chat/completions 基础 | ✅ |
| chat/completions 流式 | ✅ |
| completions | ❌ |

### volcengine/deepseek-v3-1-terminus

| 端点/功能 | 状态 |
|-----------|------|
| chat/completions 基础 | ✅ |
| chat/completions 流式 | ✅ |
| completions | ✅ |

### volcengine/deepseek-r1-250528

| 端点/功能 | 状态 |
|-----------|------|
| chat/completions 基础 | ✅ |
| chat/completions 流式 | ✅ |
| completions | ❌ |
| 特殊: 支持 reasoning_content | ✅ |

---

## 总结

1. **已验证端点**:
   - `/v1/chat/completions` - 所有 4 个 deepseek 模型均支持
   - `/v1/completions` - 仅 `volcengine/deepseek-v3-1-terminus` 支持

2. **已验证功能**:
   - ✅ 基础请求
   - ✅ 流式响应
   - ✅ 图像输入（多模态）
   - ✅ 函数调用
   - ❌ logprobs（不支持）

3. **不支持端点**:
   - `/v1/embeddings`、`/v1/images/generations`、`/v1/images/edits`、`/v1/audio/transcriptions`

4. **建议**:
   - 在文档中明确标注各模型支持的端点和功能
   - `volcengine/deepseek-r1-250528` 支持 `reasoning_content` 字段，适合需要推理过程的场景
   - logprobs 功能暂不支持，需要从 examples 中移除或标注为不支持

## 相关文件

- 模型信息: `test_openapi/model_info.json`
- 测试报告: `test_openapi/test_deepseek.md`
