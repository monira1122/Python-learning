letter= '''
Dear <|name|>,
you are selected,
<|date|> '''

print(letter.replace("<|name|>","Moni").replace("<|date|> ","24 july 2026"))
