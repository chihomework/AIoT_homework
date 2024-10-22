# 簡單線性回歸模型演示

這個項目是一個基於Flask的網頁應用,用於演示簡單線性回歸模型。用戶可以通過調整參數來觀察線性回歸模型的變化。

## 功能

- 調整線性方程的斜率
- 調整數據的噪聲水平
- 調整數據點的數量
- 生成並顯示線性回歸模型的圖形

## 安裝

1. 確保您的系統已安裝Python 3.7或更高版本。

2. 克隆此存儲庫:
   ```
   git clone https://github.com/yourusername/simple-linear-regression-demo.git
   cd simple-linear-regression-demo
   ```

3. 創建並激活虛擬環境(可選但推薦):
   ```
   python -m venv venv
   source venv/bin/activate  # 在Windows上使用 venv\Scripts\activate
   ```

4. 安裝所需的依賴:
   ```
   pip install -r requirements.txt
   ```

## 使用方法

1. 運行Flask應用:
   ```
   python app.py
   ```

2. 在瀏覽器中打開 http://127.0.0.1:5000

3. 使用滑桿調整參數:
   - 斜率 (a): 調整線性方程 y = ax + b 中的 a 值
   - 噪聲水平: 調整添加到數據中的隨機噪聲量
   - 數據點數量: 調整生成的數據點數量

4. 點擊"生成模型"按鈕來更新圖形

5. 觀察生成的圖形,了解參數變化如何影響線性回歸模型

## 文件結構

- `app.py`: Flask應用的主要代碼
- `templates/index.html`: 網頁的HTML模板
- `requirements.txt`: 項目依賴列表

## 依賴

- Flask
- NumPy
- Matplotlib
- scikit-learn

## 貢獻

歡迎提交問題和拉取請求。對於重大更改,請先開issue討論您想要更改的內容。

## 許可

[MIT](https://choosealicense.com/licenses/mit/)