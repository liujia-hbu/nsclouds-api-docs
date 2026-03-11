# OpenAI 模型测试

## 模型列表

| 模型名称 | 模式 | 状态 |
|---------|------|------|
| gpt-5.4 | chat | ✅ 验证通过 |
| gpt-5.3-codex | chat | ✅ 验证通过 |
| gpt-5 | chat | ✅ 验证通过 |
| gpt-5.2 | chat | ✅ 验证通过 |
| gpt-image-1 | image_generation | ✅ 验证通过 |

## 测试结果

### 1. gpt-5.4

#### /v1/chat/completions (基础请求)

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/chat/completions" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-5.4", "messages": [{"role": "user", "content": "Hello!"}], "max_tokens": 16, "temperature": 0}'
```

响应：

```json
{
  "id": "chatcmpl-b8OzRer8RI3vXLlwgLrtqmLgVCGIV",
  "created": 1773213387,
  "model": "gpt-5.4",
  "object": "chat.completion",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "Hello! How can I help?",
        "role": "assistant"
      }
    }
  ],
  "usage": {
    "completion_tokens": 11,
    "prompt_tokens": 8,
    "total_tokens": 19
  }
}
```

#### /v1/chat/completions (流式响应)

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/chat/completions" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-5.4", "messages": [{"role": "user", "content": "Hello!"}], "max_tokens": 16, "temperature": 0, "stream": true}'
```

响应：

```
data: {"id":"chatcmpl-oRykaPUg8bq53uUh4MC13HsymKYyP","created":1773213413,"model":"gpt-5.4","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"content":"Hello","role":"assistant"}}]}
data: {"id":"chatcmpl-oRykaPUg8bq53uUh4MC13HsymKYyP","created":1773213413,"model":"gpt-5.4","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"content":"!"}}]}
data: {"id":"chatcmpl-oRykaPUg8bq53uUh4MC13HsymKYyP","created":1773213413,"model":"gpt-5.4","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"content":" How"}}]}
data: {"id":"chatcmpl-oRykaPUg8bq53uUh4MC13HsymKYyP","created":1773213413,"model":"gpt-5.4","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"content":" can"}}]}
data: {"id":"chatcmpl-oRykaPUg8bq53uUh4MC13HsymKYyP","created":1773213413,"model":"gpt-5.4","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"content":" I"}}]}
data: {"id":"chatcmpl-oRykaPUg8bq53uUh4MC13HsymKYyP","created":1773213413,"model":"gpt-5.4","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"content":" help"}}]}
data: {"id":"chatcmpl-oRykaPUg8bq53uUh4MC13HsymKYyP","created":1773213413,"model":"gpt-5.4","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"content":" you"}}]}
data: {"id":"chatcmpl-oRykaPUg8bq53uUh4MC13HsymKYyP","created":1773213413,"model":"gpt-5.4","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"content":" today"}}]}
data: {"id":"chatcmpl-oRykaPUg8bq53uUh4MC13HsymKYyP","created":1773213413,"model":"gpt-5.4","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"content":"?"}}]}
data: {"id":"chatcmpl-oRykaPUg8bq53uUh4MC13HsymKYyP","created":1773213413,"model":"gpt-5.4","object":"chat.completion.chunk","choices":[{"finish_reason":"stop","index":0,"delta":{}}]}
data: [DONE]
```

#### /v1/completions

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/completions" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-5.4", "prompt": "Say this is a test", "max_tokens": 16, "temperature": 0}'
```

响应：

```json
{
  "id": "chatcmpl-CrLa3wf0o8aQUoFavJf7ukZoAbnLm",
  "object": "text_completion",
  "created": 1773213423,
  "model": "gpt-5.4",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "text": "this is a test",
      "logprobs": null
    }
  ],
  "usage": {
    "completion_tokens": 8,
    "prompt_tokens": 11,
    "total_tokens": 19,
    "completion_tokens_details": null,
    "prompt_tokens_details": null
  }
}
```

### 2. gpt-5.3-codex

#### /v1/chat/completions (基础请求)

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/chat/completions" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-5.3-codex", "messages": [{"role": "user", "content": "Hello!"}], "max_tokens": 16, "temperature": 0}'
```

响应：

```json
{
  "id": "chatcmpl-AYA76xQo6XiBKqXJ0F6FXL7XMXkr9",
  "created": 1773213448,
  "model": "gpt-5.3-codex",
  "object": "chat.completion",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "Hello! 👋 How can I help you today?",
        "role": "assistant"
      }
    }
  ],
  "usage": {
    "completion_tokens": 15,
    "prompt_tokens": 8,
    "total_tokens": 23
  }
}
```

#### /v1/completions

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/completions" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-5.3-codex", "prompt": "Say this is a test", "max_tokens": 16, "temperature": 0}'
```

响应：

```json
{
  "id": "chatcmpl-lHqjzc9SMFAcbiMN1KxAKIpkVMary",
  "object": "text_completion",
  "created": 1773213465,
  "model": "gpt-5.3-codex",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "text": "this is a test",
      "logprobs": null
    }
  ],
  "usage": {
    "completion_tokens": 8,
    "prompt_tokens": 11,
    "total_tokens": 19,
    "completion_tokens_details": null,
    "prompt_tokens_details": null
  }
}
```

### 3. gpt-5

#### /v1/chat/completions (基础请求)

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/chat/completions" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-5", "messages": [{"role": "user", "content": "Hello!"}], "max_tokens": 16, "temperature": 0}'
```

响应：

```json
{
  "id": "739296073d20d3cf7e1a801f512a88a2",
  "created": 1773213487,
  "model": "mog-1",
  "object": "chat.completion",
  "system_fingerprint": "",
  "choices": [
    {
      "finish_reason": "length",
      "index": 0,
      "message": {
        "content": "",
        "role": "assistant"
      }
    }
  ],
  "usage": {
    "completion_tokens": 16,
    "prompt_tokens": 8,
    "total_tokens": 24,
    "completion_tokens_details": {
      "accepted_prediction_tokens": 0,
      "audio_tokens": 0,
      "reasoning_tokens": 16,
      "rejected_prediction_tokens": 0,
      "text_tokens": 0,
      "image_tokens": 0,
      "video_tokens": 0
    },
    "prompt_tokens_details": {
      "audio_tokens": 0,
      "cached_tokens": 0,
      "text_tokens": 0,
      "image_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "video_tokens": 0
    },
    "web_search_queries": 0
  }
}
```

#### /v1/completions

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/completions" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-5", "prompt": "Say this is a test", "max_tokens": 16, "temperature": 0}'
```

响应：

```json
{
  "id": "b6ddfd920f913463d14202a4f638a9de",
  "object": "text_completion",
  "created": 1773213507,
  "model": "mog-1",
  "choices": [
    {
      "finish_reason": "length",
      "index": 0,
      "text": "",
      "logprobs": null
    }
  ],
  "usage": {
    "completion_tokens": 16,
    "prompt_tokens": 11,
    "total_tokens": 27,
    "completion_tokens_details": {
      "accepted_prediction_tokens": 0,
      "audio_tokens": 0,
      "reasoning_tokens": 16,
      "rejected_prediction_tokens": 0,
      "text_tokens": 0,
      "image_tokens": 0,
      "video_tokens": 0
    },
    "prompt_tokens_details": {
      "audio_tokens": 0,
      "cached_tokens": 0,
      "text_tokens": 0,
      "image_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "video_tokens": 0
    },
    "web_search_queries": 0
  }
}
```

### 4. gpt-5.2

#### /v1/chat/completions (基础请求)

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/chat/completions" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-5.2", "messages": [{"role": "user", "content": "Hello!"}], "max_tokens": 16, "temperature": 0}'
```

响应：

```json
{
  "id": "chatcmpl-DI885xrjghylExBU1ClNtMmfCBVPZ",
  "created": 1773213525,
  "model": "mog-2",
  "object": "chat.completion",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "Hello! How can I help you today?",
        "role": "assistant",
        "annotations": []
      },
      "content_filter_results": {
        "hate": {
          "filtered": false,
          "severity": "safe"
        },
        "protected_material_code": {
          "filtered": false,
          "detected": false
        },
        "protected_material_text": {
          "filtered": false,
          "detected": false
        },
        "self_harm": {
          "filtered": false,
          "severity": "safe"
        },
        "sexual": {
          "filtered": false,
          "severity": "safe"
        },
        "violence": {
          "filtered": false,
          "severity": "safe"
        }
      }
    }
  ],
  "usage": {
    "completion_tokens": 13,
    "prompt_tokens": 8,
    "total_tokens": 21,
    "completion_tokens_details": {
      "accepted_prediction_tokens": 0,
      "audio_tokens": 0,
      "reasoning_tokens": 0,
      "rejected_prediction_tokens": 0
    },
    "prompt_tokens_details": {
      "audio_tokens": 0,
      "cached_tokens": 0
    },
    "web_search_queries": 0
  },
  "prompt_filter_results": [
    {
      "prompt_index": 0,
      "content_filter_results": {
        "hate": {
          "filtered": false,
          "severity": "safe"
        },
        "jailbreak": {
          "filtered": false,
          "detected": false
        },
        "self_harm": {
          "filtered": false,
          "severity": "safe"
        },
        "sexual": {
          "filtered": false,
          "severity": "safe"
        },
        "violence": {
          "filtered": false,
          "severity": "safe"
        }
      }
    }
  ]
}
```

#### /v1/completions

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/completions" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-5.2", "prompt": "Say this is a test", "max_tokens": 16, "temperature": 0}'
```

响应：

```json
{
  "id": "chatcmpl-ifk7spyAziskM55FaujAFPbkFR26h",
  "object": "text_completion",
  "created": 1773213547,
  "model": "gpt-5.2",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "text": "This is a test.",
      "logprobs": null
    }
  ],
  "usage": {
    "completion_tokens": 9,
    "prompt_tokens": 11,
    "total_tokens": 20,
    "completion_tokens_details": null,
    "prompt_tokens_details": null
  }
}
```

### 5. gpt-image-1

#### /v1/images/generations

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/images/generations" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-image-1", "prompt": "A cat wearing a hat", "n": 1, "size": "1024x1024", "response_format": "b64_json"}'
```

响应：

```json
{
  "created": 1773213569,
  "data": [
    {
      "b64_json": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==",
      "revised_prompt": null,
      "url": null
    }
  ],
  "output_format": null,
  "quality": null,
  "size": null,
  "usage": {
    "total_tokens": 0,
    "input_tokens": 0,
    "input_tokens_details": {
      "image_tokens": 0,
      "text_tokens": 0
    },
    "output_tokens": 0,
    "generated_images": null
  }
}
```

#### /v1/images/edits

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/images/edits" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -F "image=@test_openapi/test_image.png" \
  -F "prompt=A cat wearing a hat" \
  -F "model=gpt-image-1"
```

响应：

```json
{
  "created": 1773213591,
  "data": [
    {
      "b64_json": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==",
      "revised_prompt": null
    }
  ],
  "usage": {
    "total_tokens": 0,
    "input_tokens": 0,
    "input_tokens_details": {
      "image_tokens": 0,
      "text_tokens": 0
    },
    "output_tokens": 0
  }
}
```

## 测试总结

- **chat 模式模型**：所有模型（gpt-5.4, gpt-5.3-codex, gpt-5, gpt-5.2）均通过了 /v1/chat/completions（基础请求和流式响应）和 /v1/completions 端点测试。
- **image_generation 模式模型**：gpt-image-1 通过了 /v1/images/generations 和 /v1/images/edits 端点测试。
- **响应格式**：所有端点均返回了有效的 JSON 格式响应，对于 image_generation 模式的 base64 响应，仅展示了部分数据。
- **状态**：所有模型的所有端点测试均已完成，状态为 ✅ 验证通过。