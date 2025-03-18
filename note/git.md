Git 下載路徑：https://git-scm.com/downloads
Git 追蹤的是檔案的變化而非檔案本身

基礎指令：
- git --version：檢查版本
- git config --gloabl user.name：設定使用者名稱
- git config --gloabl user.email：設定使用者電子郵件
- git init：初始化資料夾
    - 初始後會創建.git資料夾
    - 紀錄版本資訊
    - 刪除後所有備份紀錄就消失了
- git status：顯示檔案狀態
- git add：追蹤檔案
- git commit -m "標示提交原因"
    - -m:message
- git log：日誌，顯示提交歷史包含作者及說明文字
    - git log --oneline：簡化內容輸出
- git diff 快照ID -- 檔案名稱：顯示版本差異
    - 按 Q 退出
- git checkout 快照ID -- 檔案名稱：提檔
    - 需要重新 commit 創建新的快照
- git reset --hard：提檔並刪除該快照後的快照
    
- 檔案狀態：
    - untrack 未追蹤
    - tracked 已追蹤
    - staged 已暫存
    - commited 已提交

![alt text](image.png)代表有修改
![alt text](image-1.png)代表未追蹤
![alt text](image-2.png)已加入暫存
