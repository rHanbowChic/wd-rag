# The 'select' field type

Defines a multi-value selection field. Requires a set of values. If you specify two to four values, you get a horizontal radio field. If you specify five or more values, you get a drop-down select field. For example:

```
[[form]]
  type:
    label: Music type
    type: select
    values:
      0: Classical
      1: Country
      2: Folk
      3: Indie
      4: Jazz
      5: Pop
      6: Rock
    default: 6
[[/form]]
```

In the above example the properties of the select field were 0 to 6 with the default property of 6 which set the value to Rock. However, you can use words as properties, for example:

```
  type:
    label: Music type
    type: select
    values:
      cl: Classical
      co: Country
      fk: Folk
      in: Indie
      jz: Jazz
      po: Pop
      ro: Rock
    default: ro
```

The specific properties you can use on a select field:

- **default**: defines a default value for the field shown on new pages. For example **default:1**

**Reserved values in a select field:**

The values of **Yes**, **No**, **True** and **False** are reserved values that have a special meaning in the YAML code that powers data forms. To use them in your data form you need to place them inside quotemarks as follows otherwise they will not work:

```
  done:
    label: Done?
    type: select
    values:
      not: "No"
      done: "Yes"
    default: not
```
