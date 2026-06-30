# The 'date' field type

October 2, 2014

This is a work in progress. Some options still need to be tested before being added to this documentation.

Defines a date input field that uses the [jQuery UI Datepicker Widget](http://api.jqueryui.com/datepicker/) to select dates. It uses most of the options available that are of type *String* or *Int*. A basic datepicker can be added using just the *type* property:

```
[[form]]
fields:
  date-1:
    type: date
[[/form]]
```

The specific properties you can use on a text field:

- **width**: specifies the visible field width in columns (fixed spaced characters, more or less). If the *autoSize* option is enabled, it overrides this property setting.
- **options**: specifies the jQuery UI Datepicker Widget options to apply.

Here is an example using a few of the available options:

```
[[form]]
fields:
  mydate:
    type: date
    label: 'My Date Widget'
    options:
      appendText: ' This Demo is Cool!'
      autoSize: true
      changeYear: true
      dateFormat: 'DD, d MM yy'
      firstDay: 1
      showOn: button
      yearRange: '2014:2025'
[[/form]]
```

The above example creates a datepicker calendar widget with the following options:
- **showon: button** adds a button after the input field and it must be clicked to open the datepicker.
- **autoSize: true** automatically sets the width of the input box to fit the date format defined in the *dateFormat* option.
- **changeYear: true** creates a dropdown selector of changing the year. This is useful if you don't want to make users click the previous/next links 12 times to move to another year.
- **dateFormat: 'DD, d MM yy** formats the date selected to something like "Wednesday, 1 October 2014". See the date format reference below for more details on date formats.
- **firstDay: 1** tells the calendar to use Monday as the first day of the week for the widget's calendar instead of the default of Sunday (0=Sunday, 1=Monday, …, 6=Saturday).
- **yearRange: '2014:2025'** limits the year selection to the range specified.

Dates in a date field are stored as a date number and displayed based on the *dateFormat* option you specifiy. add the *altFormat* option to use a different date format for your alternate date. If you want to save and use the date as *text* and not a number, you can use the *altField* option to place a text version of the date into another field in your data form. The example below will place a copy of the date selected in the **mydate** field as text into the **alt-date** field text box on the form. **%%form_data{alt-date}%%** will be stored in the data form as text.

## altDate/altFormat Example

```
[[form]]
fields:
  mydate:
    type: date
    label: 'This date will fill in'
    options:
      appendText: ' altField Demo'
      autoSize: true
      changeYear: true
      dateFormat: 'DD, d MM yy'
      altField: 'input[name=field-alt-date]'
      altFormat: 'm/d/yy'
      yearRange: '2014:2025'
  alt-date:
    type: text
    label: 'Filled in by date above'
    width: 10
[[/form]]
```

## Live Examples

A very comprehensive demo has been created on the [Bootstrap Playground site](http://bootstrap-playground.wikidot.com/dataform-dates:demo).

The ***_template*** page that drives the demo is located [here](http://bootstrap-playground.wikidot.com/dataform-dates:_template).

## Datepicker Widget Options:

| Option | Syntax | Description | Example |
| --- | --- | --- | --- |
| altField | altField: 'input[name=field-<target field name>]' | The alternate field on your form to place a text copy of the date based on the currentdateFormatoption. UsealtFormatto define a different date format. | altField: 'input[name=field-alt-date]' |
| altFormat | altFormat : format string | Used to apply an alternatedateFormatto thealtDateoption | altFormat: 'm/d/yy' |
| appendText | appendText : 'string to display' | The text to display after each date field. | appendText: ' This Demo is Cool!' |
| autoSize | autoSize : true\|false | Set to true to automatically resize the input field to accommodate dates in the current dateFormat. | autoSize: true |
| buttonImage | buttonImage : 'url of image file' | URL of an image to use to display the datepicker when the showOn option is set to "button" or "both". | buttonImage: 'http://community.wikidot.com/local--files/files/calendar-icon.png' |
| buttonImageOnly | buttonImageOnly : true\|false | Whether the button image should be rendered by itself instead of inside a button element. This option is only relevant if the buttonImage option has also been set. | buttonImageOnly: false |
| buttonText | buttonText : 'string to display' | The text to display on the trigger button. Use in conjunction with the showOn option set to "button" or "both". IfbuttonImageis set, the text becomes the alt value and is not directly displayed. | buttonText: 'Pick!' |
| changeMonth | changeMonth : true\|false | Whether the month should be rendered as a dropdown instead of text. | changeMonth: true |
| changeYear | changeYear : true\|false | Whether the year should be rendered as a dropdown instead of text. Use theyearRangeoption to control which years are made available for selection. | changeYear: true |
| closeText | closeText : 'string to display' | The text to display for the close link. Use theshowButtonPanel: trueto display this button. | closeText: 'Abort Mission' |
| currentText | currentText : 'string to display' | The text to display for the close link. UseshowButtonPanel: trueto display this button. | currentText: 'Go to Today' |
| dateFormat | dateFormat : format string | The format for parsed and displayed dates. For a full list of the possible formats see the table below. | dateFormat: 'DD, MM yy' |
| dayNames | dayNames : [array of names] | The list of long day names, starting from Sunday. Useful for languages other than English. Used with theDDdate format option. | dayNames: [Sonntag, Montag, Dienstag, Mittwoch, Donnerstag, Freitag, Samstag] |
| dayNamesMin | dayNamesMin : [array of names] | The list of minimised day names, starting from Sunday, for use as column headers within the datepicker. Useful for languages other than English. | dayNamesMin: [So, Mo, Di, Mi, Do, Fr, Sa] |
| dayNamesShort | dayNamesShort : [array of names] | The list of abbreviated day names, starting from Sunday. Useful for languages other than English. Used with theDdate format option. | dayNamesShort: [Son, Mon, Die, Mit, Don, Fre, Sam] |
| defaultDate | defaultDate : 'date string'\|+/- number of days from today\|string of values and periods | Set the default date on first opening of the widget. Specify either an actual date via a string in the current dateFormat, or a number of days from today (e.g. +7) or a string of values and periods ('y' for years, 'm' for months, 'w' for weeks, 'd' for days, e.g. '+1m +7d'), or null for today. | defaultDate: '+1m -1d' |
| duration | duration : number of milliseconds\|slow\|normal\|fast | Control the speed at which the datepicker appears, it may be a time in milliseconds or a string representing one of the three predefined speeds ("slow", "normal", "fast"). | duration : slow |
| firstDay | firstDay: number | Set the first day of the week: Sunday is 0, Monday is 1, etc. | firstDay: 1 |
| hideIfNoPrevNext | hideIfNoPrevNext : true\|false\|\Normally the previous and next links are disabled (greyed out) when not applicable (as determined by theminDateandmaxDateoptions). You can hide them altogether by setting this attribute to true. | hideIfNoPrevNext: true |
| isRTL | isRTL : true\|false | Whether the current language is drawn from right to left. | isRTL: true |
| maxDate | maxDate : 'date string'\|+/- number of days from today\|string of values and periods. | The maximum selectable date. | - maxDate: '+2y -1m' |
| minDate | minDate : 'date string'\|+/- number of days from today\|string of values and periods. | The minimum selectable date. | minDate: 0 |
| monthNames | monthNames : [array of names] | The list of full month names. Useful for languages other than English. Used with theMMdate format option. | monthNames: [Jannuar, Februar, März, April, Mai, Juni, Juli, August, September, Oktober, November, Dezember] |
| monthNamesShort | monthNamesShort : [array of names] | The list of abbreviated month names, as used in the month header and with theMdate format option. Useful for languages other than English. | monthNamesShort: [Jan, Feb, Mär, Apr, Mai, Jun, Jul, Aug, Sep, Okt, Nov, Dez] |
| nextText | nextText : string | The text to display for the next month link. With the default styling, this value is used as the alt text when hovering over the icon. | nextText: 'Forward' |
| numberOfMonths | numberOfMonths : number\|[rows, columns] | The number of months to show at once.Number: The number of months to display in a single row.Array: An array defining the number of rows and columns to display. | numberOfMonths: [ 2, 3 ] |
| prevText | prevText : 'string' | The text to display for the next month link. With the default styling, this value is used as the alt text when hovering over the icon. | prevText: 'Back' |
| shortYearCutoff | shortYearCutoff : number\|date string | The cutoff year for determining the century for a date (used in conjunction with dateFormat 'y'). Any dates entered with a year value less than or equal to the cutoff year are considered to be in the current century, while those greater than it are deemed to be in the previous century. | shortYearCutoff: '+20' |
| showAnim | showAnim : show\|slideDown\|fadeIn | The name of the animation used to show and hide the datepicker. Use "show" (the default), "slideDown" or "fadeIn"Other effectsneed testing and should be added as they are confirmed to work here. | showAnim: slideDown |
| showButtonPanel | showButtonPanel : true\|false | Whether to display a button pane underneath the calendar. The button pane contains two buttons, a Today button that links to the current day, and a Done button that closes the datepicker. The buttons' text can be customized using the currentText and closeText options respectively. | showButtonPanel: true |
| showCurrentAtPos | showCurrentAtPos : number | When displaying multiple months via thenumberOfMonthsoption, this option defines which position to display the current month in. | showCurrentAtPos: 1 |
| showMonthAfterYear | showMonthAfterYear: true\|false | Whether to show the month after the year in the header. | showMonthAfterYear: true |
| showOn | showOn : focus\|button\|both | When the datepicker should appear. The datepicker can appear when the field receives focus ("focus"), when a button is clicked ("button"), or when either event occurs ("both"). | showOn: both |
| showWeek | showWeek: true\|false | When true, a column is added to show the week of the year. | showWeek: true |
| stepMonths | stepMonths: number | Set how many months to move when clicking the previous/next links. | stepMonths: 3 |
| weekHeader | weekheader: 'string' | Text to display for the week number column header when theshowWeekoption is enabled.) | weekHeader: 'wk#' |
| yearRange | yearRange: 'string' | The range of years displayed in the year drop-down: either relative to today's year ("-nn:+nn"), relative to the currently selected year ("c-nn:c+nn"), absolute ("nnnn:nnnn"), or combinations of these formats ("nnnn:-nn"). Note that this option only affects what appears in the drop-down, to restrict which dates may be selected use theminDateand/ormaxDateoptions. | yearRange: '2010:2020' |
| yearSuffix | yearSuffix: 'string' | Additional text to display after the year in the month headers. | yearSuffix: ' CE' |

## Date Formats Reference

| Datepicker Date Format Options | Wikidot Date Format Options |
| --- | --- |
| The format can be combinations of the following: | Use to display Data Form Datepicker date fields:/[[date%%form_data{datefield}%%format="%b %d, %Y"]] |
| d | day of month (no leading zero) | %a | abbreviated weekday name (3 letters) |
| dd | day of month (two digit) | %A | full weekday name |
| o | day of the year (no leading zeros) | %b | abbreviated month name (3 letters) |
| oo | day of the year (three digit) | %B | full month name |
| D | day name short | %c | local date representation |
| DD | day name long | %d | day of the month (01…31) |
| m | month of year (no leading zero) | %D | is equivalent to "%m/%d/%y" |
| mm | month of year (two digit) | %e | day of the month (1…9, 10…31) |
| M | month name short | %H | hours (00…23) |
| MM | month name long | %I | hours (00…12) |
| y | year (two digit) | %m | month (01…12) |
| yy | year (four digit) | %M | minutes (00…59) |
| @ | Unix timestamp (ms since 01/01/1970) | %O | nnseconds/minutes/hours/days |
| ! | Windows ticks (100ns since 01/01/0001) | %p | AM/PM |
| '…' | literal text | %r | is equivalent to "%I:%M:%S %p" |
| '' | single quote | %R | is equivalent to "%H:%M" |
|  |  | anything else | literal text |
|  |  | %S | seconds (00…59) |
|  |  | %T | is equivalent to "%H:%M:%S" |
|  |  | %y | year (00…99) |
|  |  | %Y | year (1970…2999) |
|  |  | %z/%Z | time zone |
