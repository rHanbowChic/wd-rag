# How to create a new data form

> Documentation > Data Forms > How to create a new data form

Wikidot stores normal pages in categories and it is exactly the same when you use data forms. Each data form page is one page in a specific category. A category can have only one data form and that data form structure applies to all pages in that category, so you cannot mix data form pages and normal wiki pages in the same category.

To create a new data form you need to do the following:

1) create a live template page for the category the form will be in. For example if your category is *band*, the live template page must be called *band:_template*.

2) add a [[form]] ..[[/form]] section then your fields. The different types of fields you can have (text, select, checkbox, file, wiki, static, hidden and password are described in the reference section at the bottom of this page.

Please note that the indentation shown in the example below is important because if the different rows are not indented correctly the fields will not display. Your structure should look like the example below, but note that you don't have to enter a field type and a width; if you don't enter a field type it will default to a text field type. The width is also not mandatory.

Please note that for all fields you must have a space between the colon and the value, for example **label: Music type** is correct, but if you enter **label:Music type** you will get n error message when you try to save the page.

```
[[form]]
fields:
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
  bandimage:
    label: Image
    type: file
  bandwebsite:
    label: Band website
    type: url
  current:
    label: Currently Recording
    type: select
    values:
      0: "Yes"
      1: "No"
    default: 0
[[/form]]
```

After you define a [[form]] ..[[/form]] structure like the one above, when you edit add or edit any page in the category it shows the form instead of the normal page editor.

## Checking for errors

Wikidot used to be relaxed about whether there were spaces after the colon, but now a more strict version of the code is used which will give you an error if you have built your data form with incorrect spaces. However, there is an app developed by one of our gurus, [![tsangk](https://www.wikidot.com/avatar.php?userid=47197&amp;size=small&amp;timestamp=1398764046)](http://www.wikidot.com/user:info/tsangk)[tsangk](http://www.wikidot.com/user:info/tsangk) to test whether your data form has been built correctly and has the correct spacing. The app is at [http://community.wikidot.com/app:convert](http://community.wikidot.com/app:convert). You just copy and paste your whole page into the app and it will convert the data form to the correct structure if it finds errors.

---

## Setting up your Site Manager

You can configure category permissions for a category with a data form exactly as for normal categories so that, for example, only the author of a page can edit it.

It is sometimes a very good idea to autonumber the category containing the data form. This will remove the risk of duplicate page names. This is setup in the *site manager > autonumbering of pages*.
