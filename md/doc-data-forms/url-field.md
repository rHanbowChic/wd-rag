# The 'url' field type

This lets the user enter URLs. This is displayed as a link.

```
[[form]]
fields:
  info_link:
    type: url
    default: ftp://example.com/files/
    match-error: Custom error msg.
    required: true
    default-schema: ftp://
[[/form]]
```

The specific properties you can use on a url field:

- **width**: specifies the visible field width in columns (fixed spaced characters, more or less).
- **default**: defines a default value for the field shown on new pages.
- **default-schema**: define a default schema for URL ('http://' if not specified).
- **match-error**: specifies a custom error message.
- **required**: specifies if the field is mandatory [true/false] ('false' if not specified).
