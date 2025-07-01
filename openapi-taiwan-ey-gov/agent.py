# pip install google-adk certifi

import os
import certifi
import requests
from google.adk.agents import LlmAgent
from google.adk.tools.openapi_tool.openapi_spec_parser.openapi_toolset import OpenAPIToolset
import json

# ─── 一、透過環境變數指定完整 CA 憑證路徑（推薦） ───
# 讓 Python SSLContext 與 requests 同步使用 certifi 的最新根憑證，
# 通常能補足缺少 Subject Key Identifier 的伺服器憑證。
os.environ['SSL_CERT_FILE'] = certifi.where()
os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()

# ─── 二、若仍驗證失敗，或在開發環境需快速解法，可全面關閉驗證 ───
# ※ 僅建議在測試或受控環境使用，生產環境請勿關閉 SSL 驗證。
_orig_request = requests.Session.request
def _patched_request(self, method, url, *args, **kwargs):
    # 若呼叫時未指定 verify，則自動加上 verify=False
    if 'verify' not in kwargs:
        kwargs['verify'] = False
    return _orig_request(self, method, url, *args, **kwargs)

requests.Session.request = _patched_request


# ─── 以下為您本機載入 swagger.json，並建立 Agent 的程式 ───

# 1. 讀取本機 OpenAPI 規格
swagger_path = "adk-example/data/swagger.json"
try:
    with open(swagger_path, encoding="utf-8") as f:
        openapi_spec_json = f.read()
        _ = json.loads(openapi_spec_json)  # 驗證 JSON
except FileNotFoundError as fnf:
    raise RuntimeError(f"找不到 swagger 檔案：{swagger_path}") from fnf
except json.JSONDecodeError as jde:
    raise RuntimeError(f"swagger.json 非有效 JSON：{jde}") from jde

# 2. 建立 OpenAPI 工具組
toolset = OpenAPIToolset(
    spec_str=openapi_spec_json,
    spec_str_type="json",
)

# 3. 初始化 LLM 代理人，並掛載工具
root_agent = LlmAgent(
    name="openapi_adk_taiwan_ey_gov_agent",
    model="gemini-2.0-flash",
    instruction="使用台灣人習慣使用的繁體中文回覆問題。",
    tools=[toolset],
)
