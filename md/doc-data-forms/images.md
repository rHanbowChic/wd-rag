# Images in Data Forms

> Documentation > Data Forms > Images in Data Forms

### Data form field

To upload an image to your dataform you need to use a **file** field.

### Layout

You display the image using %%form_raw{field}%%, not %%form_data{field}%%.

As with images on normal pages you can set parameters like a float or the width. For example:

[[f<image %%form_raw{field}%% width="150px"]]

You can also combine data forms with the [image box snippet](http://snippets.wikidot.com/code:image-box) created by [![Timothy Foster](https://www.wikidot.com/avatar.php?userid=197988&amp;size=small&amp;timestamp=1398764050)](http://www.wikidot.com/user:info/timothy-foster)[Timothy Foster](http://www.wikidot.com/user:info/timothy-foster) which will allow you to easily add a header, caption, a float left or float-right, specify the width and add a link for the image. In the data form use a file field for the image, a text field for the header and a text field for the caption.

Then to display them, above the ==== separator use the following snippet code with %%form_raw{field}%% for the image and %%form_data{field}%% for each of the header and caption. You do not need to have a value in each parameter line of the snippet code. An example of how it would look is below.

[[include :snippets:image

|image=%%form_raw{field}%%

|width=150px

|float=right

|heading=%%form_data{field}%%

|caption=%%form_data{field}%%

|link=*%%form_data{bandwebsite}%%

]]

### Where images are stored

On normal wiki pages you can upload an image to the page. This is not the case with data forms. When you upload an image using a data form, it places the image on its own page in the *file* category and the page is called the name of the image. So for example if your user presses the browse button in the data form and uploads an image called **queen.jpg**, that image is saved on the page http://yoursite.wikidot.com/**file:queen**

Although the *file*category is used by default for images, you can change the category the images on a data form are saved in. To do this use the category attribute as follows:

```
[[form]]
fields:
  eventimage:
    label: Image
    type: file
    category: eventimages
[[/form]]
```

If you had specified this in the data form structure in your live template before uploading the queen.jpg image it would have saved it at http://yoursite.wikidot.com/**eventimages:queen**

### Displaying a default image

If you don't upload an image to a file field in a data form, older browsers like IE8 will show a box with a red x or similar. This doesn't look good and makes it seem that a mistake has been made. So, instead you can display a default image which will be displayed instead. This could be a blank image or a general image related to the site. If an image is uploaded to the field in the data form then that image will be used instead..

It needs a css module in the live template and this example also uses the image box snippet from [http://snippets.wikidot.com/code:image-box](http://snippets.wikidot.com/code:image-box) to display the relevant image:

```
[!-- Following CSS module is needed for the default image code below --]
[[module CSS]]
.form-image-default%%form_raw{bandimage}%%{ display: block !important; }
.form-image%%form_raw{bandimage}%%{ display: none !important; }
[[/module]]
```

[[div class="form-image"]]

[[include :snippets:image

|image=%%form_raw{bandimage}%%

|width=150px

|float=right

|heading=

|caption=%%form_data{band_caption}%%

|link=%%form_data{band_link}%%

]]

[[/div]]

[[div class="form-image-default" style="display: none;"]]

[[include :snippets:image

|image=/css:theme/blankjpg

|width=150px

|float=right

|heading=

|caption=

|link=

]]

[[/div]]
