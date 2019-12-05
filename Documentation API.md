



# Kickstarter


teztteztze  ffzefez
****

```diff
+ POST Create a new Project
```

This api route is used to create new project.
## Headers:


>Key: Content
| application/json

>Key: Content-Type
| application/x-www-form-urlencoded

>Key: Authorization
| {{Authorization}}
## [urlencoded] Body:

### title *text*


Le nom de votre projet
### description *text*


La descrption de votre projet
### author *text*


L'id de l'auteur du projet
### wanted_price *text*


Le prix voulu  
****

```diff
+ GET Get all projects
```

The api route for getting all projects (expect lag with big database [use projets/<page>] instead.)
## Headers:


>Key: Authorization
| {{Authorization}}  
****

```diff
+ GET Get projets with pagination
```

Get projets per page of 20 items.
## Headers:


>Key: Content
| application/json

>Key: Authorization
| {{Authorization}}

>Key: Content-Type
| {{Authorization}}  
****

```diff
+ GET Get Projet
```

Get the data of an project with is id.
## Headers:


>Key: Authorization
| {{Authorization}}  
****

```diff
+ POST Auth login
```

Login to our api system for another request
## Headers:


>Key: Content-Type
| application/x-www-form-urlencoded

>Key: Authorization
| eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NzU1NDQ5MjQsInVzZXIiOnsiaWQiOjEsInVzZXJuYW1lIjoidGVzdCIsInBhc3N3b3JkIjoidGVzdCJ9fQ.XMIJ2sRXHGO_rVfkBUz1nm4Z9gM0aT_jCepr0xXh91I
## [urlencoded] Body:

### username *text*


L'username de votre utilisateur
### password *text*


Le mots de passe de votre utilisateur  
****