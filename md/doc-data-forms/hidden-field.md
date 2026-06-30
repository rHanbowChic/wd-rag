# The 'hidden' field type

Adds data to the form that the user cannot see or edit. It takes no space visually. This is for putting data into the page so that data can be used later. The value of the field is defined by the 'value' property.

```
[[form]]
fields:
  version:
    type: hidden
    value: 1.0
[[/form]]
```

The specific properties you can use on a hidden field:

- **value**: sets the value of the field
