# Displaying the results

> Documentation > Data Forms > Displaying the results

If you just save the [[form]]..[[/form]] structure then create pages, each page will have simple layout with each field under the previous one in the order the form was structured. With this simple layout any images uploaded won't be displayed, just a link to the image.

But you can layout the fields that are displayed in any way you like and display uploaded images and videos. To do this you need to divide the live template page into 2 areas with ==== separator between them:

The [[form]]..[[/form]] data form goes at the bottom of the page. Above that is a separator, ====, and then above the separator is how you want the form to be displayed on the page. This might be just the fields, it might be a table or it might be a more complex layout using divs, modules, tables and css. You display the data for the form using the following syntax. In place of the word field use

| Variable | Usage |
| --- | --- |
| %%form_data{field}%% | Displays the content of the chosen field. This is used for essentially everything except urls (images, video, email, etc.). |
| %%form_raw{field}%% | Displays unformatted content of the chosen field. This is used for url information (images, video, etc.) and when advanced Wikidot syntax is necessary (includes, modules). |
| %%form_label{field}%% | Displays the field's label if any. |
| %%form_hint{field}%% | Displays the hint used for the field, if any. |

Using the form we created above, the dataform structure, separator and layout are shown below with a very simple layout:

```
[[f<image %%form_raw{bandimage}%% width="150px"]]

++ %%title%%

Band type: %%form_data{type}%%
Band website: %%form_data{bandwebsite}%%
Is the band currently recording?: %%form_data{current}%%

====

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

The result is:

![df_queen.jpg](https://www.wdfiles.com/local--files/doc-data-forms:displaying/df_queen.jpg)
