# book-webapp-fastapi
OpenAPIからのFastAPIへのエクスポートによる、基本的なWeb図書アプリの構築

## 方針 　
1)StoplightStudioを利用して、API仕様書を作成  
　・RESTとする  
　・記載はyml形式  
　・APIは、CRUDをそのまま利用する。すなわち、「get、post、put、delete」を記載する  
　・認証は、ひとまずナシ。  
2)prismを利用して、モックを立てて動作確認をする  
　・prismの手順、使い勝手を確認  
　・APIは期待通りの挙動をするかチェック（Rest Clientを利用）    
　⇒Dreddを利用して、OpenAPI仕様書通りのリクエスト・レスポンスが得られるかテスト実施  
3)作成したAPI仕様書のymlから、FastAPIへのクラス作成  
　・ymlインポートによる作成手順を確認  
　・参考サイト：https://gift-tech.co.jp/articles/fastapi-openapi/  
4)サーバーサイドの実装  
　・FastAPIによる実装  
　・テストケースはPytestとする  
　・Bookオブジェクトの取り回しには、Dataclassを利用する。  

## 作業実施 
1) StoplightStudioを利用して、API仕様書を作成   
・StoplightStudioクライアント版をインストール。  
・Default Specificationから、yml修正する。  
・１メソッド＆クラスに対して、Form形式である程度の枠を作成する。  
　⇒Code形式で複製し、他メソッドを作成する。  
★パラメータの型定義、必須/非必須、Payload例など、コレ１つで出来ることが多い。  
  
![スクリーンショット 2022-08-07 17 08 38](https://user-images.githubusercontent.com/44053575/183281622-817116e3-59f3-412e-adc1-92db0fef03c8.png)  
  
2) prismを利用して、モックを立てて動作確認をする
・Stoplightで作成した仕様書をエクスポートする  
・以下コマンドからモックサーバーを配置する  
```
npx prism mock book-webapp-fastapi_API-specification.yaml -p 8080
```
