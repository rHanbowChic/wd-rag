# Reference

> Documentation > Data Forms > Reference

The form definition is made in [YAML](http://yaml.org), which is a simple structured markup language. A *_template* may have a single form. The form starts and ends with [[form]] and [[/form]] as for code blocks. Within those tags, we describe the form using YAML:

```
[[form]]
fields:                           #  This is always required at the start
  name-of-the-field:              #  Use a valid YAML name (i.e not starting with a number)
    label: Label                  #  This is what the user sees when using the form
    type: type-of-field           #  The field types
    property: value...            #  Depending on the field type
[[/form]]
```

The default field type is 'text', unless you specify one or more values, in which case it defaults to 'select'.

> **Always start name of the field form with a letter. Field names starting with a digit or some other character are invalid. In case of special YAML symbols like `true`, `false`, `yes`, `no`, you may need to surround those with simple quote signs like this: "yes".**
