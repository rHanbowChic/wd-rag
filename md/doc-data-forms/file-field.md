# The 'file' field type

This lets the user upload files directly from the data form. It is displayed as a link to the file.

Files are not uploaded to the same page. Instead, a separate page is created for each file in a different category, 'file' by default, with the pagename being the name of the image.

```
[[form]]
fields:
  document:
    type: file
    label: Upload document
    category: alternative-category
[[/form]]
```

The specific properties you can use on a file field:

- **category**: specifies the category that the page will be created in ('file' category if not specified), and the uploaded file is attached to this page.

> Note that images won't be treated like they are when attaching an image to simple (i.e. non-data form enabled) page. This means they won't be displayed by the [[gallery]] tag.
