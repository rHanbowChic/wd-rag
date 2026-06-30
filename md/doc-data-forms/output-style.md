# Styling the output of a field

> Documentation > Data Forms > Styling the output of a field

You can set the color and other styles of a field on the form after it is saved. Create the field in your data form in the normal way as follows:

```
[[form]
fields
...
...
  priority:
    label: Priority
    type: select
    values:
      normal: Normal
      urgent: Urgent
      critical: Critical
....
[[/form]]
```

Above the ==== separator add a CSS module:

```
[[module css]]
.normal { color: green; }
.urgent { color: red; }
.critical { color: red; font-weight: bold;}
[[/module]]
```

Then use a css span class and a combination of form_raw and form_data to display the field in the relevant color:

[[span class="%%form_raw{priority}%%"]]%%form_data{priority}%%[[/span]]
