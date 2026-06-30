# The 'text' field type

Defines a text or text box field. Allows 'width' and 'height' as properties. If you don't specify a height you get a normal 1-line text field. If you do specify it, you get a text box. For example:

```
[[form]]
fields:
  name:
    label: Your name
    type: text
    width: 30
  comment:
    label: Your comment
    type: text
    width: 50
    height: 3
  email:
    label: email address
    match: /^[_a-zA-Z0-9\-\+]+(\.[_a-zA-Z0-9-]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+$/
[[/form]]
```

The specific properties you can use on a text field:

- **width**: specifies the visible field width in columns (fixed spaced characters, more or less).
- **height**: specifies the field height in rows, 1 is normal text field, 2 or more is a text box.
- **match**: specifies a regular expression (regex) that the field value must match.
- **match-error**: specifies a custom error message.
- **hint**: provides a string of text that is displayed in the field when empty.
- **default**: defines a default value for the field shown on new pages.

In the hint, if you want to use special characters like a # then you need to escape the character using \. For example, **hint: enter a colorname like white or a hex value like \#468259**

Wiki syntax does not work in a text field.
