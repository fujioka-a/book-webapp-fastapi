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
5)サーバーを立ててアクセスしてみる  
・Dockerなどを用いて、作成したFastAPIのサーバーをローカルから立てる  
　⇒まずは簡易なやり方として、uvicornを利用する  

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
・Rest Clientを用いて、モックに対してアクセスをしてみる。  
　・リクエストボディを持つ場合（PUT、POST）：「Contentーtype：application.json」を利用する  
　・リクエストボディを持つ場合（GET、DELETE）：特になし  
  
3) 作成したAPI仕様書のymlから、FastAPIへのクラス作成  
・OpenAPI Generatorを利用する  
・datamodel-code-generator、pydanticをインストールする  
・以下コマンドより、DataclassやAPI実装を、自動作成することができる。  
　①Datamodel.pyが出力される。  
```
datamodel-codegen --input openapi/specification/book-webapp-fastapi_API-specification.yaml --input-file-type openapi --output datamodel.py
```
　②以下コマンドより、FastAPI形式でのDatamodelとAPI実装を自動作成する。  
```
fastapi-codegen --input openapi/specification/book-webapp-fastapi_API-specification.yaml --output src/book
```
  
4) サーバーサイドの実装  
・code Generatorからの出力をひとまずそのまま利用する。  
　⇒以下は後で実施  
　　・認証（account）を実装に入れる  
　　・pytest作成  

5) サーバーを立ててアクセスしてみる  
・以下コマンドよりサーバーを起動する  
　※mainとmodelのパス定義は、現状の設定に従うこと  
```
cd src/book  
(to move dir. which main file is located in)
uvicorn main:app --reload
```
