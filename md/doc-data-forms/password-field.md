# The 'password' field type

This lets the user enter masked text. To the user, each character they type is replaced by an asterisk ( * ).

```
[[form]]
fields:
  pass:
    type: password
[[/form]]
```

**Important:** Entered text is not encrypted, you can always read it in page source.
