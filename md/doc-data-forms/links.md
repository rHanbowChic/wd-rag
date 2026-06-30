# Links

> Documentation > Data Forms > Links

## External Links

### Data form field

To upload a url to your data form you need to use a **url** field. It defaults to http:// format so the user just needs to enter the url in the format *www.wikidot.com*

### Layout

To display the link, above the ==== separator use %%form_data{field}%%.

You can have the link open in a new window by adding a * as follows: *%%form_data{file}%%

---

## Internal Links

### Data form field

To include an internal link in to your data form you use a **text** field. The user just enters the name of the page in the box on the form..

### Layout

To display it, above the ==== separator use normal internal link syntax and form_data: [[[%%form_data{field}%%]]]
