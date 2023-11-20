# Blog Api

- A basic blog api to create posts by admin.
- Contact request sending an email after the request creation.
- Deploy to railway
- Unit tests

## Endpoints

- **admin/**: Admin view
- **blog-articles/**: Get the blog articles paginated
- **blog-articles/<int:pk>/<slug:slug>/**: Get Blog article by id and slug
- **contact-request**: Contact request form
- **contact-request-success/**: Success view after contact request

## Enviromental variables

- **SECRET_KEY**: Django secret key
- **EMAIL_HOST**: Email host, for test I used my personal gmail
- **EMAIL_HOST_USER**: The email to sent the message
- **EMAIL_HOST_PASSWORD**: The password of the email to sent the message
- **EMAIL_PORT**: Email port, usually 587
- **EMAIL_USE_TLS**: True
- **EMAIL_TIMEOUT**: 300
