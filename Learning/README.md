# TelegramBot

Learn by courses on YouTube: *https://www.youtube.com/c/PythonHubStudio*

This project realize TelegramBot by name [Bookworm](https://t.me/book_getter_bot)

This bot save book(or other files) on data base and for all books(or files) all users have access

***
***

# UsersTypes

***

### Guest can do:

1. */registrate* - set user status as `User`
2. */reg [login] [password]* - set user status as `AdminUser` and this status must is confirmed SuperAdmin
3. */out* - set user status as `Guest`

***

### User can do:

1. */find [name]* - find book from database by it name(substring)
2. */id [id]* - find book from id
3. */author [author]* - find all books by author
4. and all what `Guest`

***

### AdminUser can do:
1. */add [file]* - save file if its _**mimetype**_ is one of `FB2` `PDF` `EPUB`, `MOBI`, `TXT`, `LaTeX`
2. */del [id]* - del book by id
3. and all what can `User`

***

### SuperAdmin(must be 1) can:
1. */confirmation [id]* - confirmation of user rights with id
2. and all what can do `AdminUser`
