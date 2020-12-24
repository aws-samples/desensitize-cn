# desensitize for chinese policy (5 features:name, id, phone, address, card)

# Using it in full text process
 clean() function would do mask job
 It include two parameters: 
 * text: you processed text
 * replace_with: the replace type:include `identifier` and `compliance`

by default, it would process `card`,`cnaddress`,`cnid`,`cnname`,`credential`,`email`,`name`,`phone`,`url` mode, you can use add_detector() or remove_detector() to add or remove mode in it.
```
import desensitize
de=desensitize.Desensitize()
#de.remove_detector('email')
text=u"13725557496 contact Joe Duffy at joe@example.com 370304197709200630 4401250222189922 王猛住在上海市陆家嘴汤臣一品"
de.clean(text)
#['', 'a16a00b1f7d5e4e1b20a5b7517e17463', ' contact ', 'Joe', ' ', 'Duffy', ' at ', 'joe@example.com', ' ', '370***********0630', ' ', '************9922', ' ', '王*', '住在', '上海市***', '汤臣一品']
```

# Using it in csv process
```
import pandas as pd
df=pd.read_csv("test.csv")
df = df.applymap(str)
pd.save_csv("test1.csv")
```

# Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

# License

This library is licensed under the MIT-0 License. See the LICENSE file.

