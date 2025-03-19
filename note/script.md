# Javascript 筆記

*學習資源：w3schools*
*//是註解*
*/\*...\*/是多行解*
## script的寫法
- 直接寫在 html 檔內
- 獨立寫完再做引入

## 資料型態跟變數
- 字串
- 數字
- 布林值
- var 變數名稱：宣告變數
- 變數命名規則
    - 英文大小寫開頭
    - $或_開頭
    - 數字

## 字串
- "+"連接字串
- .length：回傳字串長度
- .toUpperCase：將字串轉成大寫
- .charAt(n)：回傳第 n 個字母
- .indexOf("h")：回傳字串在哪個位置
- substring(n,m)：刪掉 n 到 m 的字串

## 數字
基本上跟 C 差不多，只是變數沒有分小數跟整數
- Math.max(a,b,c,d,e,f)：回傳最大值
- Math.min(a,b,c,d,e,f)：回傳最小值
- Math.pow(n,m)：n 的 m 次方
- Math.sqrt(n)：回傳根號 n
- Math.round：四捨五入
- Math.random：隨機數

*prompt 跳出輸入視窗*
*alert 跳出訊息視窗*

## 陣列
基本上跟 C 差不多，但可以混雜不同的資料型態

## 函式
```
function 函式名稱(){
    函式功能
}
```

## 條件判斷 if
跟 C 一樣

## 物件
物件導向的概念
- 包含屬性
- 包含方法

## 迴圈
跟 C 一樣

## class  模板
物件導向的概念，先將不同物件的相同屬性先做好模板
