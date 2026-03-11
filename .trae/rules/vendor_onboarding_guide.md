# 厂家接入规范

本文档描述了为新厂家创建 API 文档的完整流程，以 OpenAI 文档为模板，替换厂家特定的模型和配置。

## 1. 前提条件

- 已有基础 OpenAPI 文件：`docs/zh/openapi/example.yaml`
- 测试环境地址已配置
- API Key 已设置到环境变量 `$NGAA_LLM_API_KEY`

## 2. 流程概览

1. **获取测试环境模型信息**：从测试环境获取模型列表和详细信息
2. **分析模型类型**：确定模型支持的功能模式
3. **创建厂家特定的 OpenAPI 文件**：基于模板创建并修改
4. **创建 Markdown 说明文档**：为每个功能点创建对应的说明文档
5. **更新目录结构**：在 SUMMARY.md 中添加相应的目录项
6. **生成 Bundled YAML**：运行脚本生成最终的 API 文档文件

## 3. 详细步骤

### 3.1 获取测试环境模型信息

#### 3.1.1 获取所有模型列表

```bash
curl -X GET "https://devaillm.nscloud.ai/v1/model/info" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY"
```

保存响应到 `test_openapi/model_info.json` 并直接 JSON 格式化：

```bash
curl -X GET "https://devaillm.nscloud.ai/v1/model/info" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  | jq '.' > test_openapi/model_info.json
```

#### 3.1.2 提取目标厂家模型

基于 `original_provider` 字段筛选目标厂家的模型：

```bash
cat test_openapi/model_info.json | jq -r '.data[] | select(.model_info.original_provider | ascii_downcase | contains("{vendor}")) | .model_name'
```

#### 3.1.3 分析模型类型

确定每个模型支持的功能模式：

```bash
cat test_openapi/model_info.json | jq -r '.data[] | select(.model_info.original_provider | ascii_downcase | contains("{vendor}")) | "\(.model_name): \(.model_info.mode // \"\")"'
```

#### 3.1.4 常见模式类型

| 模式 | 说明 | 对应端点 |
|------|------|----------|
| `chat` | 对话补全 | `/v1/chat/completions` 和 `/v1/completions` |
| `completion` | 文本补全 | `/v1/completions` |
| `embedding` | 向量嵌入 | `/v1/embeddings` |
| `image_generation` | 图片生成 | `/v1/images/generations` 和 `/v1/images/edits` |
| `audio_transcription` | 音频转录 | `/v1/audio/transcriptions` |

#### 3.1.5 测试建议

对于 `chat` 模式的模型，建议使用简单的测试问题，如 "Hello!"，而不是复杂的问题或流式请求，以确保基础功能正常工作。

### 3.2 创建厂家 OpenAPI 文件

#### 3.2.1 复制模板文件

以 `example.yaml` 为基础，创建新厂家的 OpenAPI 文件：

```bash
cp docs/zh/openapi/example.yaml docs/zh/openapi/{vendor}.yaml
```

#### 3.2.2 替换厂家标识

在 `{vendor}.yaml` 中进行以下替换：

| 替换项 | 原始值 | 目标值 |
|--------|--------|--------|
| 厂家标签 | `_example` | `_{vendor}` |
| 标签名称 | `chat_completions_example` | `chat_completions_{vendor}` |
| operationId | `_example` | `_{vendor}` |
| 模型名称 | `gpt-4`, `gpt-3.5-turbo-instruct` 等 | 目标厂家的实际模型名称 |

#### 3.2.3 使用 sed 命令批量替换

```bash
# 替换标签名
sed -i '' 's/_example/_{vendor}/g' docs/zh/openapi/{vendor}.yaml

# 替换 operationId
sed -i '' 's/createChatCompletion_example/createChatCompletion_{vendor}/g' docs/zh/openapi/{vendor}.yaml
sed -i '' 's/createCompletion_example/createCompletion_{vendor}/g' docs/zh/openapi/{vendor}.yaml
sed -i '' 's/createEmbedding_example/createEmbedding_{vendor}/g' docs/zh/openapi/{vendor}.yaml
sed -i '' 's/createImageGeneration_example/createImageGeneration_{vendor}/g' docs/zh/openapi/{vendor}.yaml
sed -i '' 's/createImageEdit_example/createImageEdit_{vendor}/g' docs/zh/openapi/{vendor}.yaml
sed -i '' 's/createTranscription_example/createTranscription_{vendor}/g' docs/zh/openapi/{vendor}.yaml
```

#### 3.2.4 手动替换 examples 中的模型名称

编辑 `{vendor}.yaml`，将 examples 中的模型名称替换为该厂家的实际模型：

**Chat Completions 端点**

```yaml
# 替换示例模型
value:
  model: gpt-4  # 替换为目标厂家模型
  messages:
    - role: user
      content: Hello!
```

**Completions 端点**

```yaml
value:
  model: gpt-3.5-turbo-instruct  # 替换为目标厂家模型
  prompt: Once upon a time
```

**Embeddings 端点**

```yaml
value:
  model: text-embedding-ada-002  # 替换为目标厂家嵌入模型
  input: The quick brown fox
```

**Image Generations 端点**

```yaml
value:
  model: dall-e-3  # 替换为目标厂家图像生成模型
  prompt: A cat wearing a hat
```

### 3.3 创建 Markdown 说明文档

#### 3.3.1 创建功能点目录结构

根据模型类型，在 `docs/zh/` 目录下创建对应的功能点文件夹：

| 功能点 | 文件夹路径 | 说明 |
|--------|------------|------|
| 对话生成 | `docs/zh/chat-completion/` | 对应 `/v1/chat/completions` 端点 |
| 文本补全 | `docs/zh/completions/` | 对应 `/v1/completions` 端点 |
| 向量嵌入 | `docs/zh/embeddings/` | 对应 `/v1/embeddings` 端点 |
| 图像生成 | `docs/zh/image-generations/` | 对应 `/v1/images/generations` 端点 |
| 音频转录 | `docs/zh/audio-transcriptions/` | 对应 `/v1/audio/transcriptions` 端点 |

#### 3.3.2 创建厂家说明文档

在每个功能点文件夹下创建 `{vendor}-{endpoint}.md` 文档。

> **重要**：模型列表需要从 `/v1/model/info` 接口获取，只添加该厂家实际拥有的模型，不要添加不存在的模型。

**对话生成（chat-completion）**

在 `docs/zh/chat-completion/` 目录下创建 `{vendor}-chat-completion.md`：

```markdown
# {Vendor 名称} - 对话生成

### 1. 概述

{Vendor} 的对话生成 API，与 OpenAI 接口格式兼容。

**模型列表：**

* `vendor/model-name-1` (chat 模式)
* `vendor/model-name-2` (chat 模式)

### 功能验证说明

| 功能 | 状态 | 说明 |
|------|------|------|
| 基础请求 | ⏳ 待验证 | - |
| 流式响应 | ⏳ 待验证 | - |
| 图像输入 | ⏳ 待验证 | - |
| 函数调用 | ⏳ 待验证 | - |

### 2. 接口详情

{% openapi-operation spec="{vendor}" path="/v1/chat/completions" method="post" %}
[OpenAPI {vendor}](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/zh/{vendor}.bundled.yaml)
{% endopenapi-operation %}
```

**文本补全（completions）**

在 `docs/zh/completions/` 目录下创建 `{vendor}-completions.md`：

```markdown
# {Vendor 名称} - 文本补全

### 1. 概述

{Vendor} 的文本补全 API，与 OpenAI 接口格式兼容。

**模型列表：**

* `vendor/model-name-1` (completion 模式)
* `vendor/model-name-2` (completion 模式)

### 功能验证说明

| 功能 | 状态 | 说明 |
|------|------|------|
| 基础请求 | ⏳ 待验证 | - |
| 流式响应 | ⏳ 待验证 | - |

### 2. 接口详情

{% openapi-operation spec="{vendor}" path="/v1/completions" method="post" %}
[OpenAPI {vendor}](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/zh/{vendor}.bundled.yaml)
{% endopenapi-operation %}
```

**向量嵌入（embeddings）**

在 `docs/zh/embeddings/` 目录下创建 `{vendor}-embeddings.md`：

```markdown
# {Vendor 名称} - 向量嵌入

### 1. 概述

{Vendor} 的向量嵌入 API，与 OpenAI 接口格式兼容。

**模型列表：**

* `vendor/model-name-1` (embedding 模式)

### 功能验证说明

| 功能 | 状态 | 说明 |
|------|------|------|
| 基础请求 | ⏳ 待验证 | - |

### 2. 接口详情

{% openapi-operation spec="{vendor}" path="/v1/embeddings" method="post" %}
[OpenAPI {vendor}](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/zh/{vendor}.bundled.yaml)
{% endopenapi-operation %}
```

**图像生成（image-generations）**

在 `docs/zh/image-generations/` 目录下创建 `{vendor}-image-generations.md`：

```markdown
# {Vendor 名称} - 图像生成

### 1. 概述

{Vendor} 的图像生成 API，与 OpenAI 接口格式兼容。

**模型列表：**

* `vendor/model-name-1` (image_generation 模式)

### 功能验证说明

| 功能 | 状态 | 说明 |
|------|------|------|
| 基础请求 | ⏳ 待验证 | - |

### 2. 接口详情

{% openapi-operation spec="{vendor}" path="/v1/images/generations" method="post" %}
[OpenAPI {vendor}](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/zh/{vendor}.bundled.yaml)
{% endopenapi-operation %}
```

**音频转录（audio-transcriptions）**

在 `docs/zh/audio-transcriptions/` 目录下创建 `{vendor}-audio-transcriptions.md`：

```markdown
# {Vendor 名称} - 音频转录

### 1. 概述

{Vendor} 的音频转录 API，与 OpenAI 接口格式兼容。

**模型列表：**

* `vendor/model-name-1` (audio_transcription 模式)

### 功能验证说明

| 功能 | 状态 | 说明 |
|------|------|------|
| 基础请求 | ⏳ 待验证 | - |

### 2. 接口详情

{% openapi-operation spec="{vendor}" path="/v1/audio/transcriptions" method="post" %}
[OpenAPI {vendor}](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/zh/{vendor}.bundled.yaml)
{% endopenapi-operation %}
```

#### 3.3.3 创建 README.md 文档

在每个功能点文件夹下创建 `README.md` 文档，用于介绍该功能点：

**对话生成 README.md**

```markdown
# 对话生成 (chat.completion)

对话生成 API 允许您与模型进行对话，支持多轮交互。

## 支持的厂家

* [深度求索(DeepSeek)](deepseek-chat-completion.md)
* [字节豆包(volcengine)](volcengine-chat-completion.md)
* [OpenAI](openai-chat-completion.md)
```

**文本补全 README.md**

```markdown
# 文本补全 (completions)

文本补全 API 允许您生成文本内容，适用于文本续写、总结等场景。

## 支持的厂家

* [深度求索(DeepSeek)](deepseek-completions.md)
* [字节豆包(volcengine)](volcengine-completions.md)
* [OpenAI](openai-completions.md)
```

**向量嵌入 README.md**

```markdown
# 向量嵌入 (embeddings)

向量嵌入 API 允许您将文本转换为向量表示，适用于语义搜索、聚类等场景。

## 支持的厂家

* [深度求索(DeepSeek)](deepseek-embeddings.md)
* [字节豆包(volcengine)](volcengine-embeddings.md)
* [OpenAI](openai-embeddings.md)
```

**图像生成 README.md**

```markdown
# 图像生成 (image generations)

图像生成 API 允许您根据文本提示生成图像。

## 支持的厂家

* [深度求索(DeepSeek)](deepseek-image-generations.md)
* [字节豆包(volcengine)](volcengine-image-generations.md)
* [OpenAI](openai-image-generations.md)
```

**音频转录 README.md**

```markdown
# 音频转录 (audio transcriptions)

音频转录 API 允许您将音频文件转换为文本。

## 支持的厂家

* [深度求索(DeepSeek)](deepseek-audio-transcriptions.md)
* [字节豆包(volcengine)](volcengine-audio-transcriptions.md)
* [OpenAI](openai-audio-transcriptions.md)
```

### 3.4 更新目录结构

#### 3.4.1 更新 SUMMARY.md

在 `SUMMARY.md` 中添加功能点的目录结构。根据该厂家从 `/v1/model/info` 获取的模型 `mode` 类型，只添加实际拥有的端点功能。

> **重要**：
> - 如果该厂家没有某个 `mode` 类型的模型，则不需要在 SUMMARY.md 中添加对应的目录项
> - 例如：如果厂家没有 `embedding` 模式的模型，则不需要添加 `向量嵌入(embeddings)` 目录项
> - 同样，如果厂家没有 `image_generation` 模式的模型，则不需要添加 `图像生成(image generations)` 目录项

```markdown
# Table of contents

* [简介](README.md)
{% if vendor has chat mode %}
* [对话生成(chat.completion)](docs/zh/chat-completion/README.md)
  * [深度求索(DeepSeek)](docs/zh/chat-completion/deepseek-chat-completion.md)
  * [字节豆包(volcengine)](docs/zh/chat-completion/volcengine-chat-completion.md)
  * [{Vendor 名称}](docs/zh/chat-completion/{vendor}-chat-completion.md)
  * [OpenAI](docs/zh/chat-completion/openai-chat-completion.md)
{% endif %}
{% if vendor has completion mode %}
* [文本补全(completions)](docs/zh/completions/README.md)
  * [深度求索(DeepSeek)](docs/zh/completions/deepseek-completions.md)
  * [字节豆包(volcengine)](docs/zh/completions/volcengine-completions.md)
  * [{Vendor 名称}](docs/zh/completions/{vendor}-completions.md)
  * [OpenAI](docs/zh/completions/openai-completions.md)
{% endif %}
{% if vendor has embedding mode %}
* [向量嵌入(embeddings)](docs/zh/embeddings/README.md)
  * [深度求索(DeepSeek)](docs/zh/embeddings/deepseek-embeddings.md)
  * [字节豆包(volcengine)](docs/zh/embeddings/volcengine-embeddings.md)
  * [{Vendor 名称}](docs/zh/embeddings/{vendor}-embeddings.md)
  * [OpenAI](docs/zh/embeddings/openai-embeddings.md)
{% endif %}
{% if vendor has image_generation mode %}
* [图像生成(image generations)](docs/zh/image-generations/README.md)
  * [深度求索(DeepSeek)](docs/zh/image-generations/deepseek-image-generations.md)
  * [字节豆包(volcengine)](docs/zh/image-generations/volcengine-image-generations.md)
  * [{Vendor 名称}](docs/zh/image-generations/{vendor}-image-generations.md)
  * [OpenAI](docs/zh/image-generations/openai-image-generations.md)
{% endif %}
{% if vendor has audio_transcription mode %}
* [音频转录(audio transcriptions)](docs/zh/audio-transcriptions/README.md)
  * [深度求索(DeepSeek)](docs/zh/audio-transcriptions/deepseek-audio-transcriptions.md)
  * [字节豆包(volcengine)](docs/zh/audio-transcriptions/volcengine-audio-transcriptions.md)
  * [{Vendor 名称}](docs/zh/audio-transcriptions/{vendor}-audio-transcriptions.md)
  * [OpenAI](docs/zh/audio-transcriptions/openai-audio-transcriptions.md)
{% endif %}
```

**判断厂家拥有哪些端点功能**：

```bash
# 查看厂家拥有的所有 mode 类型
cat test_openapi/model_info.json | jq -r '.data[] | select(.model_info.original_provider | ascii_downcase | contains("{vendor}")) | .model_info.mode' | sort -u
```

### 3.5 生成 Bundled YAML

#### 3.5.1 更新 swagger_cli.sh

在 `scripts/swagger_cli.sh` 中添加新厂家的 bundled 生成命令：

```bash
swagger-cli bundle docs/zh/openapi/{vendor}.yaml -o docs/bundled/zh/{vendor}.bundled.yaml -t yaml
swagger-cli validate docs/bundled/zh/{vendor}.bundled.yaml
```

#### 3.5.2 运行生成脚本

```bash
bash scripts/swagger_cli.sh
```

## 4. 参考信息

### 4.1 OpenAI YAML 结构（模板）

```
openai.yaml
├── tags (标签定义)
│   ├── chat_completions_* (对话补全)
│   ├── embeddings_* (向量嵌入)
│   ├── image_generations_* (图片生成)
│   ├── image_edits_* (图片编辑)
│   └── audio_transcriptions_* (音频转录)
├── paths (端点)
│   ├── /v1/chat/completions
│   ├── /v1/completions
│   ├── /v1/embeddings
│   ├── /v1/images/generations
│   ├── /v1/images/edits
│   └── /v1/audio/transcriptions
└── components (组件)
    ├── schemas (数据模型)
    ├── securitySchemes (安全方案)
    └── responses (响应)
```

### 4.2 需要替换的关键字段

| 字段位置 | 原始值 | 替换为 |
|----------|--------|--------|
| tags[].name | `chat_completions_example` | `chat_completions_{vendor}` |
| paths[].*.operationId | `createChatCompletion_example` | `createChatCompletion_{vendor}` |
| examples[].value.model | `gpt-4`, `gpt-3.5-turbo-instruct` | 目标厂家模型 |
| 链接 URL | `example.bundled.yaml` | `{vendor}.bundled.yaml` |

### 4.3 模型名称格式

通常格式为 `{vendor}/{model-name}`，例如：
- `volcengine/doubao-seed-1-8-251228`
- `deepseek/deepseek-chat`

## 5. 常见问题

### 5.1 如何确定需要创建哪些端点的文档？

根据测试环境模型信息的 `mode` 字段：
- 有 `chat` 模式模型 → 创建 `/v1/chat/completions` 和 `/v1/completions` 端点文档
- 有 `completion` 模式模型 → 创建 `/v1/completions` 端点文档
- 有 `embedding` 模式模型 → 创建 `/v1/embeddings` 端点文档
- 有 `image_generation` 模式模型 → 创建 `/v1/images/generations` 和 `/v1/images/edits` 端点文档
- 有 `audio_transcription` 模式模型 → 创建 `/v1/audio/transcriptions` 端点文档

### 5.2 如何验证模型是否支持某个功能？

可以使用简单的测试请求验证，例如：

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/chat/completions" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "vendor/model-name", "messages": [{"role": "user", "content": "test"}], "max_completion_tokens": 10}'
```

### 5.3 如何更新 SUMMARY.md 以适配已测试的模型？

根据厂家实际测试的模型类型，只在 SUMMARY.md 中保留已测试的功能点目录项：
- 已测试 `chat` 模式 → 保留 `对话生成(chat.completion)` 目录
- 已测试 `completion` 模式 → 保留 `文本补全(completions)` 目录
- 已测试 `image_generation` 模式 → 保留 `图像生成(image generations)` 目录
- 未测试的模式 → 暂时从 SUMMARY.md 中移除对应的目录项，待测试完成后再添加

## 6. OpenAI 模型测试状态

### 6.1 已测试的模型

| 模型名称 | 支持模式 | 说明 |
|----------|----------|------|
| `gpt-5` | chat | 支持 completion |
| `gpt-5.2` | chat | 支持 completion |
| `gpt-5.4` | chat | 支持 completion |
| `gpt-5.3-codex` | chat | 支持 completion |
| `gpt-image-1` | image_generation | - |

### 6.2 端点测试状态

| 端点 | 状态 | 说明 |
|------|------|------|
| `/v1/chat/completions` | ✅ 验证通过 | 基础请求和流式响应均验证通过 |
| `/v1/completions` | ✅ 验证通过 | 基础请求和流式响应均验证通过 |
| `/v1/images/generations` | ✅ 验证通过 | 基础请求验证通过 |
| `/v1/images/edits` | ✅ 验证通过 | 基础请求验证通过 |

## 7. 示例：添加新厂家

假设要添加一个名为 "Anthropic" 的厂家：

```bash
# 1. 复制模板
cp docs/zh/openapi/openai.yaml docs/zh/openapi/anthropic.yaml

# 2. 替换标识符
sed -i '' 's/_openai/_anthropic/g' docs/zh/openapi/anthropic.yaml

# 3. 替换模型名称（在编辑器中手动完成）
# gpt-4 → anthropic/claude-3-opus-20240229
# gpt-3.5-turbo-instruct → anthropic/claude-3-sonnet-20240229

# 4. 创建 Markdown 文档
touch docs/zh/chat-completion/anthropic-chat-completion.md

# 5. 更新 SUMMARY.md
# 添加 anthropic 入口

# 6. 更新 swagger_cli.sh
# 添加 anthropic.bundled.yaml 生成

# 7. 生成 bundled 文件
bash scripts/swagger_cli.sh
```