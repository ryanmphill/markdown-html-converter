# Markdown HTML Converter API

This API converts markdown to HTML and vice versa. 

## Endpoints:

### `/markdown-to-html` `POST`: 

Converts markdown text to html

**Payload:**

```json
{
    "markdown": "# Markdown text goes here\n It comes back as html"
}
```

**Response**

`200 OK`

```json
{
    "html": "<h1>Markdown text goes here</h1> <p>It comes back as html</p>"
}
```

### `/html-to-markdown` `POST`: 

Converts html content to markdown

**Payload:**

```json
{
    "html": "<h1>HTML goes here</h1> <p>It comes back as markdown</p>"
}
```

**Response**

`200 OK`

```json
{
    "markdown": "# HTML goes here\n It comes back as markdown"
}
```

## Links

### Site
Visit the live application [here](http://markdown-html-converter.s3-website.us-east-2.amazonaws.com/)

### Client Side Repository

[https://github.com/ryanmphill/markdown-html-converter-client](https://github.com/ryanmphill/markdown-html-converter-client)