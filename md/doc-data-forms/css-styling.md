# CSS Styling

You can modify the look and feel of your data forms using CSS (either per-site, or per page using the [CSS module](http://www.wikidot.com/doc:css-module). This is the CSS model for data forms:

- **table**

  *class*: form-table
  - **tr**

    *class*: form-row row-{row number}
  - **td**

    *class*: form-labels
  - **span**

    *class*: form-label
  - **td**

    *class*: form-values
  - **span/div** (div for wiki and static)

    *class*: form-value field-{name}

    *class*': form-error (added to field while save when there is matching error)
    - **{field}**

      *class*: form-{type}
    - **span**

      *class*: form-message

### Styling the hint text

If you have a long hint text you might find that it is longer than the text box. This is because by default the text box is a partcular width. In this case you can either set the width of that particular field to be wider or you can use CSS to set the same width for all text input boxes and ensure the hint fits inside it by using:

```

input[type="text"], textarea {
    width:100%;
}
```
