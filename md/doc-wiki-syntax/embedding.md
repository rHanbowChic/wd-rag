# Embedding media

> Documentation > Wiki Syntax > Embedding media

## Video

To embed video directly into the page use `[[embedvideo]] ... [[/embedvideo]]` block.

Between the the "embedding html code" should be placed from any of the following video online galleries:

- [Google Video](http://video.google.com)
- [YouTube](http://www.youtube.com)

E.g.

```
[[embedvideo]]
<embed style="width:400px; height:326px;" id="VideoPlayback" align="middle"
type="application/x-shockwave-flash"
src="http://video.google.com/googleplayer.swf?docId=263244138622602613"
allowScriptAccess="sameDomain" quality="best" bgcolor="#ffffff" scale="noScale" salign="TL"
FlashVars="playerMode=embedded"> </embed>
[[/embedvideo]]
```

## Audio

To embed audio use `[[embedaudio]] ... [[/embedaudio]]` and the html embedding code found on the audio hosting website.

Currently supported are:

- [Odeo.com](http://www.odeo.com)

E.g.

```
[[embedaudio]]
<embed src="http://www.odeo.com/flash/audio_player_standard_gray.swf"
quality="high" width="300" height="52" name="audio_player_standard_gray"
align="middle" allowScriptAccess="always" wmode="transparent"
type="application/x-shockwave-flash" flashvars="audio_id=99133&audio_duration=282.0&valid_sample_rate=true&external_url=http://www.vitalpodcasts.com/FileSystem/podcasts/89/opensource_episode1.mp3" pluginspage="http://www.macromedia.com/go/getflashplayer" />
</embed><br /><a style="font-size: 9px; padding-left: 110px; color: #f39;
letter-spacing: -1px; text-decoration: none" href="http://odeo.com/audio/99133/view">
powered by <strong>ODEO</strong></a>
[[/embedaudio]]
```
