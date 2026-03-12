---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/x8h0Gte093KpUAW4Bcpp/audio-transcriptions/openai-audio-transcriptions
---

# OpenAI

### 1. Overview

OpenAI's audio transcription API, compatible with OpenAI interface format.

{% hint style="success" %}
This API is compatible with OpenAI interface format.
{% endhint %}

**Model List:**

(None)

### Feature Verification

| Feature | Status | Description |
| ---- | ----- | -- |
| Basic Request | ❌ Unavailable | No OpenAI audio_transcription mode models in model_info |

### 2. API Details

{% openapi-operation spec="openai-en-{{ENV}}" path="/v1/audio/transcriptions" method="post" %}
[OpenAPI openai](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/{{ENV}}/en/openai.bundled.yaml)
{% endopenapi-operation %}
