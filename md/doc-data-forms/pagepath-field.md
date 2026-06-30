# The 'pagepath' field type

Lets the user create and select from a page within a page tree; the 'path' is the list of all parents plus that page. It is visualized as `page / page / page / page` with at each level, the option of viewing that page, changing the page, or adding a new child. This does not affect the actual page parent, and a form can have many pagepath fields. The pagepath field value is stored as a page full name. Hidden pages are invisible to users when selecting and navigating the page tree.

```
 origin:
   label: Origin
   type: pagepath
   category: band-origin
```

The specific properties you can use on a pagepath field:

- **category**: specifies the category that holds the page tree.
- **default**: defines a default value for the field shown on new pages.
- **max-level**: sets the maximum number of levels that can be created in the pagepath tree.
