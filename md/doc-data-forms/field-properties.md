# Field Properties

> Documentation > Data Forms > Field Properties

### Properties that apply to all field types

#### The 'label' property

If you specify a 'label' property then the field gets that text in the left column, or before the field for joined fields. If you do not specify a label then the field has an empty space in the left column, or is squashed up after the previous field, for joined fields. For example:

```
[[form]]
fields:
  address-line-1:
    label: Address
    width: 30
  address-line-2:
    width: 30
  address-line-3:
    width: 30
[[/form]]
```

#### The 'join' property

If you specify 'join: true' then the field is placed after the previous field, if any. This property has no effect if the field is the first in the form. For example:

```
[[form]]
fields:
  city:
    label: City
    width: 20
  postcode:
    label: Postcode
    width: 8
    join: true
[[/form]]
```

#### The 'before' property

Provides a string of plain text that displays before the field value

```
[[form]]
fields:
  phone:
    label: Phone
    width: 10
    before: +(1)
[[/form]]
```

#### The 'after' property

Provides a string of plain text that displays after the field value

```
[[form]]
fields:
  speed:
    label: Car speed
    width: 4
    after: kph
[[/form]]
```

### Properties for specific field types

There are additional properties that only apply to specific field types. These are documented below with the field type(s) they apply to.
