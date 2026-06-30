# YouTube and other external content

> Documentation > Data Forms > YouTube and other external content

### Data form field

To upload a YouTube video to your data form you need to use a **wiki** field. The user pastes the html embed code into the field on the dat aform.

### Layout

To display it, above the ==== separator use [[html]] tags and form_raw as follows:

```
[[html]]
%%form_raw{field}%%
[[/html]]
```

Example

- add a wiki field to the data form:

```
  bandvideo:
    label: Video
    type: wiki
```

- above the separator you add an [[html]] block and %%form_raw{bandvideo}%% to display the video:

```
[[html]]
%%form_raw{bandvideo}%%
[[/html]]
```

- the user pastes the YouTube embed code into the field:

![df_video.jpg](https://www.wdfiles.com/local--files/doc-data-forms:youtube/df_video.jpg)
- the result is

![df_video2.jpg](https://www.wdfiles.com/local--files/doc-data-forms:youtube/df_video2.jpg)
