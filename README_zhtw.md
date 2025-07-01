# google-adk-openapi-taiwan-ey-gov - 台灣行政院政府服務 OpenAPI ADK

這個專案展示了如何使用 Google 的 OpenAPI ADK (Agent Development Kit) 來整合台灣行政院 (EY) 的政府服務。它提供了一個範例代理程式，可以與各種政府 API 互動。

## 開始使用

請依照以下說明在您的本機機器上設定並執行此專案。

### 先決條件

- Python 3.8+
- pip (Python 套件安裝程式)
- virtualenv (建議用於依賴管理)

### 安裝

1.  **複製儲存庫：**

    ```bash
    git clone https://github.com/LiuYuWei/google-adk-openapi-taiwan-ey-gov.git
    cd google-adk-openapi-taiwan-ey-gov
    ```

2.  **建立並啟用虛擬環境：**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **安裝依賴項：**

    ```bash
    make install
    ```

### 配置

在 `openapi-taiwan-ey-gov/` 目錄中建立一個 `.env` 檔案，並添加您的環境變數。例如：

```
GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
```

### 執行應用程式

要啟動 ADK 代理程式，請使用 `make run` 命令：

```bash
make run
```

這將啟動 ADK 網頁介面，您可以透過它與代理程式互動。

### 專案結構

- `openapi-taiwan-ey-gov/`: 包含核心代理程式邏輯和配置。
  - `agent.py`: 主要的代理程式應用程式。
  - `swagger.json`: 政府服務的 OpenAPI 規範。
  - `.env`: 用於 API 金鑰和其他配置的環境變數。
- `venv/`: Python 虛擬環境。
- `Makefile`: 用於安裝和執行應用程式的自動化腳本。
- `requirements.txt`: Python 依賴項。

## 使用方式

應用程式運行後，您可以透過 ADK 網頁介面與代理程式互動。

![ADK Web Snapshot](./statics/adk_web_snapshot.png)

## 授權

本專案採用 MIT 授權 - 詳細資訊請參閱 LICENSE 檔案。
