# Bibliography

> Documentation > Wiki Syntax > Bibliography

The bibliography block is defined by `[[bibliography]]...[[/bibliography]]`. Each bibliography item has the form:

`label : full reference`

To cite a bibliography entry use `((bibcite *label*))`.

```
The first pulsar was observed by J. Bell and A. Hewish [((bibcite bell))]. Another reference [see ((bibcite guy))].

[[bibliography]]
: bell : Bell, J.; Hewish, A.; Pilkington, J. D. H.; Scott, P. F.; and Collins, R. A. //Observation of a Rapidly Pulsating Radio Source.// Nature 217, 709, 1968.
: guy : Guy, R. K. //Modular Difference Sets and Error Correcting Codes.// §C10 in Unsolved Problems in Number Theory, 2nd ed. New York: Springer-Verlag, pp. 118-121, 1994.
[[/bibliography]]
```

The first pulsar was observed by J. Bell and A. Hewish [[1]]. Another reference [see [2]].

**Bibliography**

1. Bell, J.; Hewish, A.; Pilkington, J. D. H.; Scott, P. F.; and Collins, R. A. *Observation of a Rapidly Pulsating Radio Source.* Nature 217, 709, 1968.

2. Guy, R. K. *Modular Difference Sets and Error Correcting Codes.* §C10 in Unsolved Problems in Number Theory, 2nd ed. New York: Springer-Verlag, pp. 118-121, 1994.

If you are not satisfied with the default title ("Bibliography") you can force your own title by using `[[bibliography title="Custom title"]]` or even do not use title at all (`title=""`).
