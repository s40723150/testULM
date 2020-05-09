# https://mde.tw/cd2020 協同設計專案
#!/usr/bin/python
# 導入 os 模組, 主要用來判斷是否在遠端或近端上執行
import os
# 導入同目錄下的 myflaskapp.py
import myflaskapp
import ssl

# 即使在近端仍希望以 https 模式下執行
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('cd2020.crt', 'cd2020.key')

uwsgi = False

# 以下開始判斷在遠端或近端執行
if uwsgi:
    # 表示程式在雲端執行
    application = myflaskapp.app
else:
    # 表示在近端執行
    myflaskapp.app.run(host='127.0.0.1', port=8443, debug=True, ssl_context=context)
    

