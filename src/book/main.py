# generated by fastapi-codegen:
#   filename:  book-webapp-fastapi_API-specification.yaml
#   timestamp: 2022-08-08T05:59:32+00:00

from __future__ import annotations

from typing import List, Optional, Union

from fastapi import FastAPI, Header, Path

from models import (
    Book,
    BooksBookIdDeleteResponse,
    BooksBookIdGetResponse,
    BooksBookIdGetResponse1,
    BooksBookIdGetResponse2,
    BooksBookIdPutResponse,
    BooksPostRequest,
    BooksPostResponse,
)

app = FastAPI(
    title='book-webapp-fastapi_API-specification',
    version='0.1',
    description='OpenAPI定義による図書WebアプリのAPI仕様書',
    summary='図書Webアプリのサマリ',
    contact={'name': 'fujioka', 'email': 'example.com'},
    servers=[{'url': 'http://localhost:3000'}],
)


@app.get("/hello")
async def hello():
    # テスト
    return {"message": "hello world!"}


@app.post('/books', response_model=BooksPostResponse)
def post_book(
    authorization: Optional[str] = Header(None, alias='Authorization'),
    body: BooksPostRequest = None,
) -> BooksPostResponse:
    """
    Create New Book
    """
    pass


@app.get('/books', response_model=List[Book])
def get_books(
    authorization: Optional[str] = Header(None, alias='Authorization')
) -> List[Book]:
    pass


@app.get(
    '/books/{book_id}',
    response_model=Book,
    responses={
        '401': {'model': BooksBookIdGetResponse},
        '404': {'model': BooksBookIdGetResponse1},
        '500': {'model': BooksBookIdGetResponse2},
    },
)
def get_books_book_id(
    authorization: str = Header(..., alias='Authorization'),
    book_id: str = Path(..., alias='bookId'),
) -> Union[
    Book, BooksBookIdGetResponse, BooksBookIdGetResponse1, BooksBookIdGetResponse2
]:
    """
    Get Book Info by Book ID
    """
    pass


@app.put('/books/{book_id}', response_model=BooksBookIdPutResponse)
def put_books_book_id(
    authorization: str = Header(..., alias='Authorization'),
    book_id: str = Path(..., alias='bookId'),
    body: Book = None,
) -> BooksBookIdPutResponse:
    pass


@app.delete('/books/{book_id}', response_model=BooksBookIdDeleteResponse)
def delete_books_book_id(
    authorization: str = Header(..., alias='Authorization'),
    book_id: str = Path(..., alias='bookId'),
) -> BooksBookIdDeleteResponse:
    """
    delete one books according to bookId
    """
    pass
