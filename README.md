# book-webapp-fastapi
OpenAPIからのFastAPIへのエクスポートによる、基本的なWeb図書アプリの構築

## 方針 　
1)StoplightStudioを利用して、API仕様書を作成  
　・RESTとする  
　・記載はyml形式  
　・APIは、CRUDをそのまま利用する。すなわち、「get、post、put、delete」を記載する  
2)prismを利用して、モックを立てて動作確認をする  
　・prismの手順、使い勝手を確認  
　・APIは期待通りの挙動をするかチェック（Rest Clientを利用）    
3)作成したAPI仕様書のymlから、FastAPIへのクラス作成  
　・ymlインポートによる作成手順を確認  
　・参考サイト：https://gift-tech.co.jp/articles/fastapi-openapi/  
4)サーバーサイドの実装  
　・FastAPIによる実装  
　・テストケースはPytestとする  
