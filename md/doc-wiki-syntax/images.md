# Images

> Documentation > Wiki Syntax > Images

## Single images

To insert an image into the page use the following syntax:

```
[[image image-source attribute1="value1" attribute2="value2" ...]]
```

And here is the list of allowed attributes:

| attribute name | allowed values | example value | description |
| --- | --- | --- | --- |
| link | wiki page name or URL | "wiki-page"/"http://www.example.com"/"#anchor"/"#" | makes image a link to another page or web address; this isignoredwhen using Flickr as a source; prepend the link with '*' to make it open in a new window; can link to anAnchorwithin a page; "#" prevents any actions when image is clicked |
| alt | any string | "a photo of me" | Text substitution when image not available. It is also used by screen readers to describe an image. |
| title | any string | "a photo of me" | Displays mouse-over text for the image. |
| width | number of pixels | "200px" | forces width of a image when displaying |
| height | number of pixels | "200px" | forces height of a image when displaying |
| style | valid CSS style definition | "border: 1px solid red; padding: 2em;" | adds extra CSS style to the image |
| class | CSS class | "mystyle" | forces the image CSS class - suggested use only with customized themes |
| size | "square"- 75x75 pixels/"thumbnail"- 100 on longest side/"small"- 240 on longest side/"medium"- 500 on longest side/"medium640"- 640 on longest side (Flickr only)/"large"- 1024 on longest side (only for Flickr large images)/"original"- original image (Flickr only) | any of allowed ;-) | displays aresizedimage; great for thumbnails/(transparency is lost and clicking the thumbnail opens the original image, unless link parameter is also supplied)/if flickr is the source it pulls required size from a Flickr server;/this option has effect only on local images or Flickr images |

`size` attribute works very well with local files (attached to pages) not only with image files, but with e.g. PDF or PostScript. See [this page](http://www.imagemagick.org/script/formats.php) for more details.

The *image-source* can be one of the following:

| source type | format | example value | description |
| --- | --- | --- | --- |
| URL address | any valid URL address | http://www.example.com/image.jpg | displays image from the web address |
| file attachment (current page) | filename | exampleimage.jpg | displays image attached to the current page |
| :first | :first | :first | displays first image attached to the current page (or nothing at all) |
| file attachment (different page) | /another-page-name/filename | /another-page/exampleimage.jpg | displays image attached to a different page |
| flickrimage | flickr:photoid | flickr:83001279 | displays image from Flickr and links to the original Flickr page |
| flickrimage (private) | flickr:photoid_secret | flickr:149666562_debab08866 | displays image from Flickr and links to the original Flickr page; if thesecretis provided the image is available despite being marked as non-public |

To make the linked document in a new window you can either prepend the `link` attribute with '*' (e.g. `link="*http://www.example.com"` or prepend the `src` element with '*' (e.g. `*flickr:149666562_debab08866`, `**image-file*` etc.) for images that automatically generate links.

To choose horizontal alignment use:

- `[[=image…` - centered image
- `[[<image…` - image on left
- `[[>image…` - image on right
- `[[f<image…` - image on left floating (surrounded by text)
- `[[f>image…` - image on right floating (surrounded by text)

## Gallery of images

To insert a series of images into a page content use the `[[gallery]]` element:

```
[[gallery size="image-size"]]
```

or

```
[[gallery size="image-size"]]
: image-source1 attribute1="value1" attribute2="value2" ...
: image-source2 attribute1="value1" attribute2="value2" ...
...
[[/gallery]]
```

The allowed attributes within the `[[gallery]]` tag are:

| attribute | allowed values | default | description |
| --- | --- | --- | --- |
| size | "square","thumbnail","small","medium" | "thumbnail" | sets the size of preview image/this option has effect only on local images or Flickr images |
| order | "name","name desc","created_at","created_at desc" | "name" | sets order type |
| viewer | "false","no","true","yes" | "yes" | disables LightBox viewer |

Order parameter also takes the following deprecated values: `"nameDesc"`, `"dateAddedDesc"` and `"dateAdded"`. For consistency with ListPages module it also takes the following values: `"name desc desc"` and `"created_at desc desc"` (meaning the same as without the "desc desc").

If the `[[gallery]]` tag is invoked without a list of images it automatically displays rescaled images (thumbnails) of image files attached to the current page (without .pdf and .ps documents as gallery displays only images by default).

If `[[gallery]]` is invoked with a list of images, only these images are displayed. `image-source` must not be a URL in this case. Allowed "per-image attributes are:

- `link` - URL or wiki page name (does not work with Flickr images to be o.k. with Flickr terms)
- `alt` - alternative text when the image is not available

To make a document open in a new window the same rules as with a single image applies.

The gallery by default is using LightBox to view images. It means that if you click on an image in the gallery, a very nice looking pop-up will show up with a possibility to scroll images forward / backward without reloading page / opening new tab or window. To disable LightBox view use parameter:

`[[gallery viewer="no"]]` or `[[gallery viewer="false"]]`

Also see [FlickrGallery module](/doc:flickrgallery-module) if you wish to import images from Flickr.

Put the [[gallery]] tag on its own line or the parser will not recognize it.
