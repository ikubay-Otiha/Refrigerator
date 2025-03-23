## 冷蔵庫管理アプリ
### 導入
```bash
git clone <このリポジトリ>
```
プロジェクトのルートで以下を実行
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirement.txt
touch .env
```
作成した.envファイルに以下を記入
```bash
DEBUG=TRUE  
DJANGO_SECRET_KEY='your_secret_key'
```

Webサーバ起動
```bash
python3 manage.py runserver
```