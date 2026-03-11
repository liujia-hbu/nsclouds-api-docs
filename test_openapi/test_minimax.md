# MiniMax API 测试记录

测试环境：`https://devaillm.nscloud.ai`

## 模型列表

从 `/v1/model/info` 获取的 MiniMax 模型：

- `MiniMax-M2.5` (chat 模式)

## 功能测试

### `/v1/chat/completions` - 基础请求

**测试命令**:

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/chat/completions" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "MiniMax-M2.5",
    "messages": [
      {"role": "user", "content": "Hello!"}
    ],
    "max_completion_tokens": 50
  }'
```

**响应结果**:

```json
{
  "id": "chatcmpl-5f8c2c44-08dd-98f7-b111-c18d6281f6ee",
  "created": 1773225557,
  "model": "MiniMax-M2.5",
  "object": "chat.completion",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "Hello! How can I help you today?",
        "role": "assistant",
        "reasoning_content": "The user has sent a simple greeting. I should respond in a friendly and helpful manner."
      },
      "provider_specific_fields": {}
    }
  ],
  "usage": {
    "completion_tokens": 31,
    "prompt_tokens": 40,
    "total_tokens": 71,
    "completion_tokens_details": {
      "reasoning_tokens": 17
    },
    "prompt_tokens_details": {
      "cached_tokens": 0
    }
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
    "model": "MiniMax-M2.5",
    "messages": [
      {"role": "user", "content": "Hello!"}
    ],
    "stream": true
  }'
```

**响应结果**:

```
data: {"id":"chatcmpl-dfa65e7d-7c0e-9fe2-9fb6-88e76061dd4a","object":"chat.completion.chunk","created":1773225567,"model":"MiniMax-M2.5","choices":[{"index":0,"delta":{"reasoning_content":"The user has just said \"Hello!\" - a simple greeting. I should respond in a friendly, welcoming manner and offer to help them with whatever they need.\n"},"reasoning_content":"The user has just said \"Hello!\" - a simple greeting. I should respond in a friendly, welcoming manner and offer to help them with whatever they need.\n"}],"usage":{"completion_tokens":0,"prompt_tokens":0,"total_tokens":0}}
data: {"id":"chatcmpl-dfa65e7d-7c0e-9fe2-9fb6-88e76061dd4a","object":"chat.completion.chunk","created":1773225567,"model":"MiniMax-M2.5","choices":[{"index":0,"delta":{"content":"Hello!"}}],"usage":{"completion_tokens":0,"prompt_tokens":0,"total_tokens":0}}
data: {"id":"chatcmpl-dfa65e7d-7c0e-9fe2-9fb6-88e76061dd4a","object":"chat.completion.chunk","created":1773225567,"model":"MiniMax-M2.5","choices":[{"index":0,"delta":{"content":" How are you doing"}}],"usage":{"completion_tokens":0,"prompt_tokens":0,"total_tokens":0}}
data: {"id":"chatcmpl-dfa65e7d-7c0e-9fe2-9fb6-88e76061dd4a","object":"chat.completion.chunk","created":1773225567,"model":"MiniMax-M2.5","choices":[{"index":0,"delta":{"content":" today? Is there"}}],"usage":{"completion_tokens":0,"prompt_tokens":0,"total_tokens":0}}
data: {"id":"chatcmpl-dfa65e7d-7c0e-9fe2-9fb6-88e76061dd4a","object":"chat.completion.chunk","created":1773225567,"model":"MiniMax-M2.5","choices":[{"index":0,"delta":{"content":" something I can help"}}],"usage":{"completion_tokens":0,"prompt_tokens":0,"total_tokens":0}}
data: {"id":"chatcmpl-dfa65e7d-7c0e-9fe2-9fb6-88e76061dd4a","object":"chat.completion.chunk","created":1773225567,"model":"MiniMax-M2.5","choices":[{"index":0,"delta":{"content":" you with?"}}],"usage":{"completion_tokens":0,"prompt_tokens":0,"total_tokens":0}}
data: {"id":"chatcmpl-dfa65e7d-7c0e-9fe2-9fb6-88e76061dd4a","object":"chat.completion.chunk","created":1773225567,"model":"MiniMax-M2.5","choices":[{"finish_reason":"stop","index":0,"delta":{}}],"usage":{"completion_tokens":0,"prompt_tokens":0,"total_tokens":0}}
data: [DONE]
```

**状态**: ✅ 验证通过

---

### `/v1/chat/completions` - 图像输入

**测试命令**:

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/chat/completions" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "MiniMax-M2.5",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "What is in this image?"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "https://ark-project.tos-cn-beijing.volces.com/doc_image/seedream4_5_imageToimage.png"
            }
          }
        ]
      }
    ],
    "max_completion_tokens": 300
  }'
```

**响应结果**:

```json
{
  "id": "chatcmpl-dbce134a-0923-99e8-82d8-bda6891b9418",
  "created": 1773225586,
  "model": "MiniMax-M2.5",
  "object": "chat.completion",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "I'm sorry, but I can't see or analyze images directly. If you'd like, you can describe what's in the image, or paste any text or details you see, and I'll gladly help with that!",
        "role": "assistant",
        "reasoning_content": "The user asks: \"What is in this image?\" This presumably refers to an image they have provided, but there's no image in the conversation. There's no image file attached. However, they might have included an image URL? The conversation shows only the text \"What is in this image?\" It's possible that in the UI, there's an image but the model doesn't see it. In that case, the model must note that it cannot view the image, or ask for more details. According to policy: The user is asking for content from an image that is not provided (but presumably might have been provided in the UI). The request is: \"What is in this image?\" Since we cannot see any image, we must respond that we cannot see the image and ask for clarification. According to policy: \"If the user provides an image that is not visible to the model, respond that we cannot see the image.\" The user likely expects the assistant to describe the content of an image. The correct approach: politely let them know we cannot see the image. Ask for a description or request the user to describe the image. We must not make assumptions or hallucinate. So answer: I'm sorry, I can't view images directly. Please provide a description or text of the image."
      },
      "provider_specific_fields": {}
    }
  ],
  "usage": {
    "completion_tokens": 304,
    "prompt_tokens": 44,
    "total_tokens": 348,
    "completion_tokens_details": {
      "reasoning_tokens": 254
    },
    "prompt_tokens_details": {
      "cached_tokens": 0
    }
  }
}
```

**状态**: ❌ 不支持（模型无法识别图像输入）

---

### `/v1/completions` - 基础请求

**测试命令**:

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/completions" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "MiniMax-M2.5",
    "prompt": "Say this is a test",
    "max_tokens": 7,
    "temperature": 0
  }'
```

**响应结果**:

```json
{
  "error": {
    "message": "litellm.BadRequestError: OpenAIException - Error code: 404 - {'error': {'message': 'Unsupported model `MiniMax-M2.5` for OpenAI compatibility mode.', 'type': 'invalid_request_error', 'param': None, 'code': 'model_not_supported'}, 'request_id': 'e93fe9cd-cc52-9992-9026-e150213d7582'}. Received Model Group=MiniMax-M2.5\nAvailable Model Group Fallbacks=None",
    "type": null,
    "param": null,
    "code": "400"
  }
}
```

**状态**: ❌ 不支持（模型不支持 completions 端点）

---

## 功能测试汇总

| 功能 | 状态 | 说明 |
|------|------|------|
| 基础请求 | ✅ | 验证通过 |
| 流式响应 | ✅ | 验证通过，支持 reasoning_content |
| 图像输入 | ❌ | 不支持 |
| 函数调用 | ⏳ | 待验证 |
| completions 接口 | ❌ | 不支持 |

## 各模型详细验证

### MiniMax-M2.5

| 端点/功能 | 状态 |
|-----------|------|
| chat/completions 基础 | ✅ |
| chat/completions 流式 | ✅ |
| chat/completions 图像输入 | ❌ |
| chat/completions 函数调用 | ⏳ |
| completions | ❌ |

---

## 总结

1. **已验证端点**:
   - `/v1/chat/completions` 基础请求 ✅
   - `/v1/chat/completions` 流式响应 ✅

2. **已验证功能**:
   - 基础对话生成
   - 流式响应（支持 reasoning_content）

3. **不支持端点**:
   - `/v1/completions`（模型不支持 OpenAI 兼容模式）
   - `/v1/chat/completions` 图像输入（模型无法识别图像）

4. **模型特点**:
   - MiniMax-M2.5 为 chat 模式
   - 响应中包含 `reasoning_content` 字段，显示模型的推理过程
   - 流式响应先返回 reasoning_content，再返回 content
   - 不支持 completions 端点
   - 不支持图像输入