# MailForm Module

> Documentation > Modules > MailForm Module

## Description

This module can be used to collect user input via a web form and receive the filled form via email. The email can be sent to any registered Wikidot users.

## Attributes

| attribute | required | allowed values | default | description |
| --- | --- | --- | --- | --- |
| to | no | user names | site admins | comma-delimited list of Wikidot user names |
| button | no | any string | "send" | text displayed within thesendbutton |
| format | no | "csv" | none | chooses alternative format of serializing the form data |
| title | no | text | "Wikidot.com - MailForm form data" | title of the email containing the submitted form |
| successPage | no | valid page name | none | after the form is sent the browser will be redirected to the specified page. put a "thank you" there if you wish ;-) |

The names of the 'to' recipients may not contain spaces: to specify a user name that has spaces, replace each space with a hyphen or underscore. If you do not specify a 'to' argument, the email will be sent to all site admins.

The definition of the form must be enclosed within the [[module … ]] … [[/module]] tags. The full specification of how to do this:

The definition of the fields is a nested list that looks like this:

```
# field1_name
 * option1_name: value
 * option2_name: value2
  * suboption1_nam: value
# field2_name
 * ...
```

where `field_name` is the alphanumeric identifier of the field, e.g. `first_name`. The options are:

| option name | required | allowed values | default | description |
| --- | --- | --- | --- | --- |
| title | no, but recommended! | any string | field_name | title of the field displayed in the same row on the left |
| type | no | text, textarea, select, checkbox | text | type of the input field |
| size | no | integer | 30 | size of the input field |
| default | no | value of the input | none | in case of the "text" or "textarea" fields it is just a string that appears inside the field; in case of "select" it must be one of the option labels |
| hint | no | any text | none |
| options | only for "select", see below |
| rules | validation rules, see below |

### "Select" type

If your field is a "select" field, you must also provide options for it. Do so as shown:

```
# field_name
 * title: Gender
 * type: select
 * default: male
 * options:
  * male: Male
  * female: Female
  * option_name: Displayed value
```

where the "default: …" is not required, but if provided it should match one of the names of the options.

### Validation

This module offers a powerful way to validate the input data. To use validation do:

```
# field_name
 * title: Validated field
 * type: text
 * rules:
  * rule1_name: value
  * rule2_name: value
```

where rules are:

| rule name | allowed values | description |
| --- | --- | --- |
| required | anything, e.g. "true" | if the field is required |
| minLength | integer | does not allow strings shorter than limit |
| maxLength | integer | does not allow strings longer than limit |
| match | perl regular expression | checks the value against expression, e.g./[a-z0-9]+/allows only lowercase letters and numbers |
| number | anything, e.g. "true" | checks if numeric |
| minValue | number | for numerical fields sets the lower limit |
| maxValue | number | for numerical fields sets the upper limit |

## Examples

Ok, suppose you are making some kind of conference registration and want to grab participants' data:

```
[[module MailForm title="New message from MailForm documentation page"]]
# name
 * title: Your name
 * type: text
 * rules:
  * required: true
# affiliation
 * title: Institute/Organization/Company
 * hint: leave blank in none
# address
 * title: Address
 * rules:
  * required: true
  * minLength: 2
# address2
 * title: Address (cont.)
# country
 * title: Country
 * rules:
  * minLength: 2
# phone
 * title: Phone
# email
 * title: Email
 * type: text
 * rules:
  * match: /^[_a-zA-Z0-9-]+(\.[_a-zA-Z0-9-]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+$/
# payment
 * title: I will pay by
 * type: select
 * options:
  * creditcard: Credit card
  * banktransfer: Bank wire transfer
  * desk: At the registration desk
  * na: Not applicable
# logging
 * title: Please find me a hotel
 * type: checkbox
 * hint: we will contact you via email if yes
# comments
 * type: textarea
 * title: Extra comments
 * rules:
  * maxLength: 500
[[/module]]
```

**Note:** The following image depicts the output of the prior MailForm code and is non-interactive.

![Example form requesting for contact information and a message.](https://www.wdfiles.com/local--files/doc-modules:mailform-module/wikidot-form-example.png)
