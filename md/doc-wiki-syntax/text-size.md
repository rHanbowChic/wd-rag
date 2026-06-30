# Text Size

> Documentation > Wiki Syntax > Text Size

Text (font) size can be set with the `[[size` …`]]` … `[[/size]]` tags. These tags can be nested.

### Relative text sizes

Relative text sizes are based on the current font — they increase or decrease the current font size. To specify a relative text size use `[[size smaller]]`, `[[size larger]]`, `[[size` *n*`em]]`, or `[[size` *n*`%]]`, where *n* is a 1- to 5-digit number (including an optional decimal point).

| what you type | what you get |
| --- | --- |
| [[size smaller]]smaller text[[/size]] | smaller text |
| [[size larger]]larger text[[/size]] | larger text |
| [[size 80%]]80% of current size[[/size]] | 80% of current size |
| [[size 100%]]100% of current size[[/size]] | 100% of current size |
| [[size 150%]]150% of current size[[/size]] | 150% of current size |
| [[size 0.8em]]80% of current size[[/size]] | 80% of current size |
| [[size 1em]]100% of current size[[/size]] | 100% of current size |
| [[size 1.5em]]150% of current size[[/size]] | 150% of current size |

### Absolute text sizes

Absolute text sizes are *not* based on the current font size. To specify an absolute text size use `[[size xx-small]]`, `[[size x-small]]`, `[[size small]]`, `[[size large]]`, `[[size x-large]]`, `[[size xx-large]]`, or `[[size` *n*`px]]`, where *n* is a 1- to 5-digit number (including an optional decimal point).

| what you type | what you get |
| --- | --- |
| [[size xx-small]]xx-small text[[/size]] | xx-small text |
| [[size x-small]]x-small text[[/size]] | x-small text |
| [[size small]]small text[[/size]] | small text |
| [[size large]]large text[[/size]] | large text |
| [[size x-large]]x-large text[[/size]] | x-large text |
| [[size xx-large]]xx-large text[[/size]] | xx-large text |
| [[size 7px]]text size 7 pixels[[/size]] | text size 7 pixels |
| [[size 18.75px]]text size 18.75 pixels[[/size]] | text size 18.75 pixels |
