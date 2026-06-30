# FlickrGallery Module

> Documentation > Modules > FlickrGallery Module

## Description

Pulls images from [Flickr](http://www.flickr.com) - online photo management.

## Attributes

| attribute | required | allowed values | default | description |
| --- | --- | --- | --- | --- |
| userName | no | any validflickruser name | none | limits results to a single user |
| tags | no | tags | none | comma-delimited list oftags |
| tagMode | no | "any","all" | "any" | applies OR, AND for tag sellection |
| sort | no | "date-posted-asc"/"date-posted-desc"/"date-taken-asc"/"date-taken-desc"/"interestingness-desc"/"interestingness-asc"/"relevance" | "date-posted-desc" | sets the sort order |
| alternative attributes (do not play with these above) |
| photosetId | no | any validphotoset id | none | gets images from a photoset |
| groupId | no | any validgroup name | none | gets images from a specified group |
| groupUrl | no | URL address of the group main page | none | gets images from a specified group |
| display options |
| perPage | no | any number between 1 and 100 | 30 | how many photos per page |
| limitPages | no | any positive number | none | limits number of pages to navigate; also useful if you do not want to navigate pages at all (limitPages="1") |
| size | no | "square"- 75x75 pixels/"thumbnail"- 100 on longest side/"small"- 240 on longest side/"medium", 500 on longest side | "thumbnail" | size of the images to display |
| other options |
| disableBrowsing | no | "yes"/"true" | none | disables displaying images in overlay windows when clicked |
| contentType | no | photos, screenshots, other, photos-screenshots, screenshots-other, photos-other, all | "all" | sets the type of images retrieved from Flickr |

## Examples

Get pictures that have both "linux" and "sun" tags:

```
[[module FlickrGallery tags="linux,sun" tagMode="all"]]
```

How it works:
