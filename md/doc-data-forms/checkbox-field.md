# The 'checkbox' field type

Defines a checkbox field, stored in the form data as 0 or 1. For example:

```
[[form]]
fields:
  onions:
    label: Do you want onions?
    type: checkbox
  salami:
    label: How about extra salami?
    type: checkbox
    default: 1
[[/form]]
```

The specific properties you can use on a checkbox field:

- **default**: defines a default value for the field shown on new pages.
